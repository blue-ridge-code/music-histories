param(
    [int]$Port = 0,
    [switch]$NoDispatch
)

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$config = Get-Content -Raw (Join-Path $repoRoot 'review-queue\config.json') | ConvertFrom-Json
if ($Port -le 0) {
    $Port = [int]$config.server.port
}
$url = "http://127.0.0.1:${Port}/review-queue/"

Write-Host "$($config.project.name) human review queue"
Write-Host "Open: $url"

$listener = Get-NetTCPConnection -LocalAddress 127.0.0.1 -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($listener) {
    # Something is already bound to this port. Confirm it is THIS project's review
    # queue before treating it as "already running" -- fail closed on an unclear or
    # foreign identity instead of silently no-op'ing against someone else's service.
    $identityUrl = "http://127.0.0.1:${Port}/api/review-queue/identity"
    $identity = $null
    try {
        $identity = Invoke-RestMethod -Uri $identityUrl -Method Get -TimeoutSec 3 -ErrorAction Stop
    } catch {
        $identity = $null
    }
    if ($null -eq $identity -or $identity.service -ne 'human-review-queue') {
        Write-Error "Port $Port is occupied by something that did not answer as this project's review queue. Refusing to proceed -- choose a different -Port or stop the other process."
        exit 1
    }
    if ($identity.project_id -ne $config.project.id) {
        Write-Error "Port $Port is already running a DIFFERENT project's review queue ('$($identity.project_name)', id '$($identity.project_id)'). Refusing to proceed -- choose a different -Port."
        exit 1
    }
    Write-Host 'This project''s review queue is already running.'
    return
}

Write-Host 'Stop: press Ctrl+C in this terminal.'
$arguments = @((Join-Path $repoRoot 'scripts\human_review_queue_server.py'), '--port', $Port)
if ($NoDispatch) {
    $arguments += '--no-dispatch'
}
python @arguments
