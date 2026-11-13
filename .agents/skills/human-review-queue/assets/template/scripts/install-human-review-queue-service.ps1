param(
    [int]$Port = 0,
    [switch]$NoDispatch
)

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$config = Get-Content -Raw (Join-Path $repoRoot 'review-queue\config.json') | ConvertFrom-Json
if ($Port -le 0) {
    $Port = [int]$config.server.port
}
$taskName = [string]$config.server.task_name
$serverScript = Join-Path $repoRoot 'scripts\human_review_queue_server.py'
$pythonw = (Get-Command pythonw.exe -ErrorAction Stop).Source
$userId = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name

$argumentText = '"{0}" --port {1}' -f $serverScript, $Port
if ($NoDispatch) {
    $argumentText += ' --no-dispatch'
}
$action = New-ScheduledTaskAction -Execute $pythonw -Argument $argumentText
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $userId
$principal = New-ScheduledTaskPrincipal -UserId $userId -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 3650)

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force | Out-Null
Start-ScheduledTask -TaskName $taskName

Write-Host "Installed and started Task Scheduler task: $taskName"
Write-Host "Review queue: http://127.0.0.1:${Port}/review-queue/"
Write-Host "Remove later: Unregister-ScheduledTask -TaskName '$taskName' -Confirm:`$false"
