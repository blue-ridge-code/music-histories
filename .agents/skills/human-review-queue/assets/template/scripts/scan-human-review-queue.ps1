param(
    [switch]$Json,
    [string]$Reviewer
)

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$arguments = @((Join-Path $repoRoot 'scripts\human_review_queue.py'), 'scan')
if ($Json) {
    $arguments += '--json'
}
if ($Reviewer) {
    $arguments += @('--reviewer', $Reviewer)
}
python @arguments
