# Usage: pwsh scripts/check-evidence-links.ps1 [-DocsFile <path>]
# Verifies every markdown link in a decisions/doc file resolves to a real file.
# Supports #L<line> fragments: the requested line must exist in the target file.
# Fenced code blocks are skipped (the Format examples are illustrative, not links).
# Exit codes: 0 = clean, 1 = broken links found, 2 = usage error.

[CmdletBinding()]
param(
    [string]$DocsFile
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Resolve the default in the body: $PSScriptRoot is unreliable inside a param
# default expression in some invocation modes.
if ([string]::IsNullOrWhiteSpace($DocsFile)) {
    $ScriptRoot = $PSScriptRoot
    if ([string]::IsNullOrWhiteSpace($ScriptRoot)) {
        $ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
    }
    $DocsFile = Join-Path (Split-Path -Parent $ScriptRoot) 'docs\decisions.md'
}

if (-not (Test-Path -LiteralPath $DocsFile -PathType Leaf)) {
    Write-Error "File not found: $DocsFile"
    exit 2
}

$DocDir = Split-Path -Parent $DocsFile
if ([string]::IsNullOrEmpty($DocDir)) {
    # A bare filename with no directory component (e.g. -DocsFile AGENTS.md, run from
    # the repo root) resolves to an empty string here, and Join-Path rejects an empty
    # -Path below. Treat it as "current directory" instead of failing.
    $DocDir = '.'
}
$lines = Get-Content -LiteralPath $DocsFile
$problems = @()
$checked = 0

$linkPattern   = '\[([^\]]*)\]\(([^)]+)\)'
$lineFragment  = '^L(\d+)'
$inFence = $false

foreach ($line in $lines) {
    $trimmed = $line.TrimStart()
    if ($trimmed.StartsWith('```')) { $inFence = -not $inFence; continue }
    if ($inFence) { continue }

    foreach ($m in [regex]::Matches($line, $linkPattern)) {
        $label  = $m.Groups[1].Value
        $target = $m.Groups[2].Value.Trim()

        # Skip external URLs, email links, and bare anchors
        if ($target -match '^(https?|ftp|mailto):' -or $target.StartsWith('#') -or $target -eq '') { continue }

        # Split off an optional #L<line> fragment
        $fragment = $null
        if ($target.Contains('#')) {
            $target, $fragment = $target -split '#', 2
        }
        if ($target.Trim() -eq '') { continue }

        $resolved = [System.IO.Path]::GetFullPath((Join-Path $DocDir $target.Trim()))
        $checked++
        if (-not (Test-Path -LiteralPath $resolved -PathType Leaf)) {
            $problems += "BROKEN     : [$label]($($m.Groups[2].Value)) -> $resolved"
            continue
        }

        if ($fragment -and $fragment -match $lineFragment) {
            $requestedLine = [int]$Matches[1]
            $actualLines   = (Get-Content -LiteralPath $resolved).Count
            if ($requestedLine -gt $actualLines) {
                $problems += "LINE-RANGE : [$label]($($m.Groups[2].Value)) #L$requestedLine exceeds $actualLines line(s) in $resolved"
            }
        }
    }
}

if ($problems.Count -gt 0) {
    Write-Host "Evidence-link check failed for $DocsFile ($($problems.Count) problem(s)):"
    foreach ($problem in $problems) { Write-Host "  $problem" }
    exit 1
}

Write-Host "Evidence links clean: $checked link(s) in $DocsFile resolve."
exit 0
