# Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$InputPath,

    [Parameter(Mandatory = $true, Position = 1)]
    [string]$OutputPath,

    [ValidateSet("latex", "weasyprint")]
    [string]$Engine = "latex",

    [string]$DefaultsPath = "defaults/pdf-latex.yaml"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-RelativePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$BasePath
    )

    if ([System.IO.Path]::IsPathRooted($Path)) {
        return $Path
    }

    return [System.IO.Path]::GetFullPath((Join-Path $BasePath $Path))
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$inputFullPath = Resolve-RelativePath -Path $InputPath -BasePath (Get-Location).Path
$outputFullPath = Resolve-RelativePath -Path $OutputPath -BasePath (Get-Location).Path
$defaultsFullPath = Resolve-RelativePath -Path $DefaultsPath -BasePath $repoRoot

if (-not (Test-Path -LiteralPath $inputFullPath -PathType Leaf)) {
    throw "Input Markdown file not found: $inputFullPath"
}

if (-not (Test-Path -LiteralPath $defaultsFullPath -PathType Leaf)) {
    throw "Pandoc defaults file not found: $defaultsFullPath"
}

$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if ($null -eq $pandoc) {
    throw "Pandoc is not available in PATH. Install Pandoc before exporting PDF."
}

$pdfEngine = "xelatex"
if ($Engine -eq "latex") {
    $xelatex = Get-Command xelatex -ErrorAction SilentlyContinue
    if ($null -eq $xelatex) {
        throw "XeLaTeX is not available in PATH. Install MiKTeX or TeX Live, or run with -Engine weasyprint."
    }
} elseif ($Engine -eq "weasyprint") {
    $weasyprint = Get-Command weasyprint -ErrorAction SilentlyContinue
    if ($null -eq $weasyprint) {
        throw "WeasyPrint is not available in PATH. Install WeasyPrint, or run with -Engine latex."
    }
    $pdfEngine = "weasyprint"
}

$outputDirectory = Split-Path -Parent $outputFullPath
if ($outputDirectory -and -not (Test-Path -LiteralPath $outputDirectory -PathType Container)) {
    $null = [System.IO.Directory]::CreateDirectory($outputDirectory)
}

$inputDirectory = Split-Path -Parent $inputFullPath
$resourcePath = $inputDirectory + [System.IO.Path]::PathSeparator + $repoRoot

& $pandoc.Source --defaults $defaultsFullPath --pdf-engine $pdfEngine --resource-path $resourcePath --output $outputFullPath $inputFullPath
if ($LASTEXITCODE -ne 0) {
    throw "Pandoc failed with exit code $LASTEXITCODE."
}

if (-not (Test-Path -LiteralPath $outputFullPath -PathType Leaf)) {
    throw "Pandoc completed but output PDF was not created: $outputFullPath"
}

Write-Output "PDF exported: $outputFullPath"
