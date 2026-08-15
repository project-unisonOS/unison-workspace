param(
  [Parameter(Mandatory=$true)][ValidateSet('bootstrap','validate','test-unit','test-boundaries','status')][string]$Action,
  [string]$HostName = $env:UNISON_DEV_NUC_HOST,
  [string]$Workspace = $env:UNISON_DEV_NUC_WORKSPACE
)
$ErrorActionPreference = 'Stop'
if (-not $HostName) { throw 'Set UNISON_DEV_NUC_HOST to the SSH or Tailscale host name.' }
if (-not $Workspace) { $Workspace = '/srv/unison/unison-workspace' }
$commands = @{
  bootstrap = './scripts/bootstrap-dev.sh'
  validate = './scripts/validate-phase0.sh'
  'test-unit' = './scripts/test-unit.sh'
  'test-boundaries' = './scripts/test-boundaries.sh'
  status = 'git status --short --branch && git submodule status'
}
$remote = "cd '$Workspace' && $($commands[$Action])"
ssh $HostName $remote
if ($LASTEXITCODE -ne 0) { throw "Remote development command failed with exit code $LASTEXITCODE" }
