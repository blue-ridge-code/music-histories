# Usage: pwsh scripts/sync-skills.ps1 [-Verify]
# Mirrors canonical .agents/skills/ -> .claude/skills/ additively (never deletes extras).
# -Verify compares SHA-256 of each canonical file against its mirror; exit 1 on drift/missing, 0 when clean.

[CmdletBinding()]
param(
    [switch]$Verify
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Resolve the repo root (parent of scripts/) so the script works from any CWD.
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Source = Join-Path $RepoRoot '.agents\skills'
$Mirror = Join-Path $RepoRoot '.claude\skills'

if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
    Write-Host "ERROR: canonical skills directory not found: $Source"
    exit 1
}

function Get-FileSha256 {
    param([string]$Path)
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToUpperInvariant()
}

$canonicalFiles = @(Get-ChildItem -LiteralPath $Source -Recurse -File)

if ($Verify) {
    $problems = @()
    foreach ($file in $canonicalFiles) {
        $relative = $file.FullName.Substring($Source.Length + 1)
        $mirrorFile = Join-Path $Mirror $relative
        if (-not (Test-Path -LiteralPath $mirrorFile -PathType Leaf)) {
            $problems += "MISSING: $relative"
            continue
        }
        if ((Get-FileSha256 $file.FullName) -ne (Get-FileSha256 $mirrorFile)) {
            $problems += "DRIFT:   $relative"
        }
    }
    if ($problems.Count -gt 0) {
        Write-Host "Skill mirror drift detected ($($problems.Count) problem(s)):"
        foreach ($problem in $problems) { Write-Host "  $problem" }
        exit 1
    }
    Write-Host "Skill mirror clean: $($canonicalFiles.Count) canonical file(s) verified."
    exit 0
}

if (-not (Test-Path -LiteralPath $Mirror -PathType Container)) {
    New-Item -ItemType Directory -Path $Mirror -Force | Out-Null
}

$copied = 0
$skipped = 0
foreach ($file in $canonicalFiles) {
    $relative = $file.FullName.Substring($Source.Length + 1)
    $destination = Join-Path $Mirror $relative
    $destinationDir = Split-Path -Parent $destination
    if (-not (Test-Path -LiteralPath $destinationDir -PathType Container)) {
        New-Item -ItemType Directory -Path $destinationDir -Force | Out-Null
    }
    if ((Test-Path -LiteralPath $destination -PathType Leaf) -and
        ((Get-FileSha256 $file.FullName) -eq (Get-FileSha256 $destination))) {
        $skipped++
        continue
    }
    Copy-Item -LiteralPath $file.FullName -Destination $destination -Force
    $copied++
}

Write-Host "Skill sync complete: $copied copied, $skipped unchanged (skipped). Extras in .claude/skills left untouched."
exit 0
