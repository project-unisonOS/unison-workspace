"""One explicitly approved experiment, not a production inference provider.

Fixed official artifacts, no automatic model acquisition during inference.
Missing isolation/dependencies or exceeded limits fail; never relax the limits.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import time
import urllib.request

MODEL_REV = "91cad51170dc346986eccefdc2dd33a9da36ead9"
MODEL_FILE = "qwen2.5-1.5b-instruct-q4_k_m.gguf"
MODEL_SIZE = 1117320736
MODEL_HASH = "6a1a2eb6d15622bf3c96857206351ba97e1af16c30d7a74ee38970e434e9407e"
RUNTIME_FILE = "llama-b11988-bin-ubuntu-x64.tar.gz"
RUNTIME_SIZE = 22694353
RUNTIME_HASH = "e7eeafcaf514c44d658d0620c5f8b7e3c2acd928e83118d5fc4ecd7643ecd8dc"
MODEL_BASE = f"https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/{MODEL_REV}/"
RUNTIME_BASE = "https://github.com/ggml-org/llama.cpp/releases/download/b11988/"
RUNTIME_REV = "abb76ab380c7f3f731e365a859fb4cc64e939bb8"
DOWNLOAD_CAP = 1500000000
DISK_CAP = 4 * 1024**3
EVIDENCE = Path("model-evidence")
downloaded = 0


def download(url, target, expected_size=None, expected_hash=None):
    global downloaded
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(url, timeout=120) as response, target.open("wb") as out:
        while chunk := response.read(1024 * 1024):
            downloaded += len(chunk)
            size += len(chunk)
            if downloaded > DOWNLOAD_CAP or (expected_size and size > expected_size):
                raise RuntimeError("approved download budget exceeded")
            digest.update(chunk)
            out.write(chunk)
    if expected_size is not None and size != expected_size:
        raise RuntimeError("artifact size mismatch")
    if expected_hash and digest.hexdigest() != expected_hash:
        raise RuntimeError("artifact digest mismatch")
    return {"url": url, "bytes": size, "sha256": digest.hexdigest()}


def command(args, timeout=30):
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f"command failed ({result.returncode}): {result.stdout[-6000:]}")
    return result.stdout


def run():
    EVIDENCE.mkdir(exist_ok=True)
    report = {"status": "failed", "synthetic_only": True, "model_revision": MODEL_REV,
              "runtime_revision": RUNTIME_REV, "limits": {"memory_bytes": DISK_CAP, "disk_bytes": DISK_CAP,
              "cpu_threads": 2, "context": 2048, "output_tokens": 64, "inference_seconds": 600}}
    root = Path(tempfile.mkdtemp(prefix="approved-model-"))
    root.chmod(0o755)
    image_id = None
    try:
        if os.name != "posix" or not shutil.which("docker"):
            raise RuntimeError("approved disposable Linux Docker isolation unavailable")
        # No external base image or installed host dependency. The first run
        # stopped because ubuntu:24.04 was not cached. An empty disposable image
        # needs no download; runner libraries below remain mounted read-only.
        empty_tar = root / "empty-rootfs.tar"
        with tarfile.open(empty_tar, "w"):
            pass
        image_id = command(["docker", "image", "import", str(empty_tar)]).strip()
        report["isolation_image_id"] = image_id
        report["isolation_base"] = "locally generated empty filesystem; no base-image download"
        runtime = root / "runtime"
        runtime.mkdir()
        artifacts = [download(MODEL_BASE + MODEL_FILE, root / MODEL_FILE, MODEL_SIZE, MODEL_HASH),
                     download(RUNTIME_BASE + RUNTIME_FILE, root / RUNTIME_FILE, RUNTIME_SIZE, RUNTIME_HASH)]
        report["artifacts"] = artifacts
        report["licenses"] = [download(MODEL_BASE + "LICENSE", EVIDENCE / "Qwen-LICENSE.txt"),
            download(f"https://raw.githubusercontent.com/ggml-org/llama.cpp/{RUNTIME_REV}/LICENSE", EVIDENCE / "llama-LICENSE.txt")]
        if "Apache" not in (EVIDENCE / "Qwen-LICENSE.txt").read_text() or "MIT" not in (EVIDENCE / "llama-LICENSE.txt").read_text():
            raise RuntimeError("approved license text unavailable")
        report["provenance_limit"] = "Official HTTPS metadata SHA-256 verified; no independent signature/attestation claimed."
        with tarfile.open(root / RUNTIME_FILE) as archive:
            if sum(member.size for member in archive.getmembers()) + MODEL_SIZE + RUNTIME_SIZE > DISK_CAP:
                raise RuntimeError("approved extraction disk budget exceeded")
            archive.extractall(runtime, filter="data")
        # The pinned release separates its interactive CLI from completion.
        # tools/completion/README.md at RUNTIME_REV documents this entrypoint.
        candidates = list(runtime.rglob("llama-completion"))
        if len(candidates) != 1:
            raise RuntimeError("approved runtime has no unique llama-completion")
        binary = "/qualification/" + candidates[0].relative_to(root).as_posix()
        library_dirs = sorted({"/qualification/" + p.parent.relative_to(root).as_posix() for p in runtime.rglob("*.so*")})
        base = ["docker", "run", "--rm", "--network=none", "--read-only", "--user=65534:65534",
                "--cpus=2", "--memory=4g", "--memory-swap=4g", "--pids-limit=64", "--cap-drop=ALL",
                "--security-opt=no-new-privileges", "--tmpfs=/tmp:rw,noexec,nosuid,size=64m",
                "--mount", f"type=bind,source={root},target=/qualification,readonly",
                "--env=HOME=/tmp", "--env=" + "LD_LIBRARY_PATH=" + ":".join(library_dirs)]
        # Runner-installed dynamic libraries are read-only. No home, workspace,
        # credentials, sockets or repository token enter the inference container.
        for path in ("/usr", "/bin", "/lib", "/lib64", "/etc/ld.so.cache"):
            if Path(path).exists():
                base += ["--mount", f"type=bind,source={path},target={path},readonly"]
        base += [image_id]
        dependencies = command(base + ["/usr/bin/ldd", binary])
        (EVIDENCE / "runtime-dependencies.txt").write_text(dependencies)
        if "not found" in dependencies:
            raise RuntimeError("runtime dependency unavailable in approved isolation")
        help_text = command(base + [binary, "--help"])
        for option in ("--no-conversation", "--no-display-prompt"):
            if option not in help_text:
                raise RuntimeError("approved bounded CLI option unavailable: " + option)
        started = time.monotonic()
        output = command(base + [binary, "-m", "/qualification/" + MODEL_FILE, "-c", "2048", "-n", "64",
                                "-t", "2", "-tb", "2", "--no-conversation", "--no-display-prompt",
                                "-p", "Synthetic test only. Return the word READY and explain that missing measurements are unknown, not zero."], timeout=600)
        (EVIDENCE / "synthetic-output.txt").write_text(output)
        report.update(status="completed", elapsed_inference_seconds=round(time.monotonic()-started, 2),
                      downloaded_bytes=downloaded, isolation="network-none; read-only; unprivileged; no credentials",
                      qualification_limit="Single CPU synthetic smoke only; not Ollama binding, production integration or clinical qualification.")
    except Exception as error:
        report["error"] = str(error)
        raise
    finally:
        (EVIDENCE / "result.json").write_text(json.dumps(report, indent=2))
        print(json.dumps(report, indent=2))
        if image_id:
            subprocess.run(["docker", "image", "rm", image_id], check=False, stdout=subprocess.DEVNULL)
        # Only the uniquely created disposable directory is removed.
        shutil.rmtree(root)


if __name__ == "__main__":
    run()
