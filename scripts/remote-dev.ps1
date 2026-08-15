param(
  [Parameter(Mandatory=$true)][ValidateSet('connect','clone','bootstrap','validate','test-unit','test-boundaries','status','doctor')][string]$Action,
  [string]$HostName = $env:UNISON_DEV_NUC_HOST,
  [string]$Workspace = $env:UNISON_DEV_NUC_WORKSPACE,
  [string]$Repository = 'https://github.com/project-unisonOS/unison-workspace.git'
)
$ErrorActionPreference = 'Stop'
if (-not $HostName) { throw 'Set UNISON_DEV_NUC_HOST to the SSH or Tailscale host name.' }
if (-not $Workspace) { $Workspace = '/srv/unison/unison-workspace' }
$commands = @{
  connect = 'uname -a && id && python3 --version && git --version'
  clone = "test -d '$Workspace/.git' || git clone --recurse-submodules '$Repository' '$Workspace'"
  bootstrap = './scripts/bootstrap-dev.sh'
  validate = './scripts/validate-phase0.sh'
  'test-unit' = './scripts/test-unit.sh'
  'test-boundaries' = './scripts/test-boundaries.sh'
  status = 'git status --short --branch && git submodule status'
  doctor = './scripts/doctor.sh'
}
$remote = if ($Action -in @('connect','clone')) { $commands[$Action] } else { "cd '$Workspace' && $($commands[$Action])" }
ssh $HostName $remote
if ($LASTEXITCODE -ne 0) { throw "Remote development command failed with exit code $LASTEXITCODE" }
