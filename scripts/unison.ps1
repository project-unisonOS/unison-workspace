param(
    [ValidateSet("bootstrap", "doctor", "test-unit", "validate-phase0", "up", "down", "status")]
    [string]$Command = "doctor"
)

$ErrorActionPreference = "Stop"
$WorkspaceWindows = $PSScriptRoot -replace '[\\/]+[^\\/]+$', ''

if (-not (Get-Command wsl.exe -ErrorAction SilentlyContinue)) {
    throw "WSL2 is required. Install WSL and an Ubuntu distribution first."
}

if ($WorkspaceWindows -match '^\\\\wsl(?:\.localhost|\$)\\Ubuntu\\(?<LinuxPath>.*)$') {
    $WorkspaceLinux = "/" + $Matches.LinuxPath.Replace("\", "/")
}
else {
    $WorkspaceLinux = (& wsl.exe -d Ubuntu -- wslpath -a -- $WorkspaceWindows).Trim()
}
if (-not $WorkspaceLinux) {
    throw "Could not translate the workspace path into WSL."
}

$commands = @{
    "bootstrap"       = "./scripts/bootstrap-dev.sh"
    "doctor"          = "./scripts/doctor.sh"
    "test-unit"       = "./scripts/test-unit.sh"
    "validate-phase0" = "./scripts/validate-phase0.sh"
    "up"              = "./scripts/up.sh"
    "down"            = "./scripts/down.sh"
    "status"          = "./scripts/status.sh"
}

Write-Host "[unison] Delegating '$Command' to WSL2 Ubuntu."
& wsl.exe -d Ubuntu --cd $WorkspaceLinux -- bash -lc $commands[$Command]
if ($LASTEXITCODE -ne 0) {
    throw "Unison command failed with exit code $LASTEXITCODE."
}
