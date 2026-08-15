#!/usr/bin/env python3
"""Validate that a clean agent can discover authority and exact entrypoints."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = ["AGENTS.md", "docs/agent-contributor-model.md", "docs/repo-map.md",
            "docs/development-topology.md", "docs/developer-guide.md",
            "scripts/bootstrap-dev.sh", "scripts/remote-dev.ps1", "tasks/task-packet.schema.json"]
missing = [item for item in required if not (ROOT / item).is_file()]
if missing: raise SystemExit(f"missing agent onboarding artifacts: {', '.join(missing)}")
for document in required[:5]:
    text = (ROOT / document).read_text(encoding="utf-8")
    if "—" in text: raise SystemExit(f"em dash prohibited in documentation: {document}")
print(f"validated {len(required)} agent onboarding artifacts")
