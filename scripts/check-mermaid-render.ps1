# Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet

param(
    [string[]]$Path = @(
        "documents/research_documents/vvv-qmrf",
        "documents/research_documents/category",
        "documents/research_documents/mapping",
        "SYSTEM_Buddhist_Epistemology"
    ),

    [string]$OutputDir = "build/mermaid-preview",

    [ValidateSet("svg", "png")]
    [string]$Format = "svg",

    [switch]$UseNpx,

    [switch]$IncludeArchives,

    [switch]$KeepMmd
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-RepoPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$InputPath,

        [Parameter(Mandatory = $true)]
        [string]$RepoRoot
    )

    if ([System.IO.Path]::IsPathRooted($InputPath)) {
        return [System.IO.Path]::GetFullPath($InputPath)
    }

    return [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $InputPath))
}

function Get-RelativePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$BasePath,

        [Parameter(Mandatory = $true)]
        [string]$TargetPath
    )

    $baseFullPath = [System.IO.Path]::GetFullPath($BasePath)
    if (-not $baseFullPath.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $baseFullPath += [System.IO.Path]::DirectorySeparatorChar
    }

    $targetFullPath = [System.IO.Path]::GetFullPath($TargetPath)
    $baseUri = New-Object System.Uri($baseFullPath)
    $targetUri = New-Object System.Uri($targetFullPath)

    return [System.Uri]::UnescapeDataString($baseUri.MakeRelativeUri($targetUri).ToString()).Replace('/', [System.IO.Path]::DirectorySeparatorChar)
}

function Get-SafeName {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Value
    )

    $safe = $Value -replace '[:\\/]+', '__'
    $safe = $safe -replace '[^A-Za-z0-9_.-]+', '_'
    return $safe.Trim('_')
}

function Get-MarkdownFiles {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$InputPaths,

        [Parameter(Mandatory = $true)]
        [string]$RepoRoot,

        [Parameter(Mandatory = $true)]
        [bool]$IncludeArchivePaths
    )

    $files = New-Object System.Collections.Generic.List[string]

    foreach ($inputPath in $InputPaths) {
        $fullPath = Resolve-RepoPath -InputPath $inputPath -RepoRoot $RepoRoot

        if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
            if ([System.IO.Path]::GetExtension($fullPath) -ieq ".md") {
                $files.Add($fullPath)
            }
            continue
        }

        if (Test-Path -LiteralPath $fullPath -PathType Container) {
            Get-ChildItem -LiteralPath $fullPath -Recurse -File -Filter "*.md" | ForEach-Object {
                $files.Add($_.FullName)
            }
            continue
        }

        throw "Path not found: $inputPath"
    }

    $uniqueFiles = $files | Sort-Object -Unique
    $filteredFiles = New-Object System.Collections.Generic.List[string]

    foreach ($file in $uniqueFiles) {
        $relativePath = Get-RelativePath -BasePath $RepoRoot -TargetPath $file
        if ((-not $IncludeArchivePaths) -and ($relativePath -match '(^|\\)(achives|archives)(\\|$)')) {
            continue
        }
        $filteredFiles.Add($file)
    }

    return $filteredFiles
}

function Get-MermaidBlocks {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )

    $lines = [System.IO.File]::ReadAllLines($FilePath)
    $blocks = New-Object System.Collections.Generic.List[object]
    $content = New-Object System.Collections.Generic.List[string]
    $inBlock = $false
    $startLine = 0
    $blockIndex = 0

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]

        if (-not $inBlock) {
            if ($line -match '^\s*```\s*mermaid\b.*$') {
                $inBlock = $true
                $startLine = $i + 1
                $content.Clear()
            }
            continue
        }

        if ($line -match '^\s*```\s*$') {
            $blockIndex++
            $blocks.Add([pscustomobject]@{
                Index = $blockIndex
                StartLine = $startLine
                Content = [string]::Join([Environment]::NewLine, $content)
                IsTerminated = $true
            })
            $inBlock = $false
            continue
        }

        $content.Add($line)
    }

    if ($inBlock) {
        $blockIndex++
        $blocks.Add([pscustomobject]@{
            Index = $blockIndex
            StartLine = $startLine
            Content = [string]::Join([Environment]::NewLine, $content)
            IsTerminated = $false
        })
    }

    return $blocks
}

function ConvertTo-ProcessArgument {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string]$Value
    )

    if ($Value -notmatch '[\s"]') {
        return $Value
    }

    $builder = New-Object System.Text.StringBuilder
    $null = $builder.Append('"')
    $backslashCount = 0

    foreach ($character in $Value.ToCharArray()) {
        if ($character -eq '\') {
            $backslashCount++
            continue
        }

        if ($character -eq '"') {
            $null = $builder.Append('\' * (($backslashCount * 2) + 1))
            $null = $builder.Append('"')
            $backslashCount = 0
            continue
        }

        if ($backslashCount -gt 0) {
            $null = $builder.Append('\' * $backslashCount)
            $backslashCount = 0
        }
        $null = $builder.Append($character)
    }

    if ($backslashCount -gt 0) {
        $null = $builder.Append('\' * ($backslashCount * 2))
    }

    $null = $builder.Append('"')
    return $builder.ToString()
}

function Invoke-ExternalProcess {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,

        [Parameter(Mandatory = $true)]
        [string[]]$ArgumentList
    )

    $processInfo = New-Object System.Diagnostics.ProcessStartInfo
    $processInfo.FileName = $FilePath
    $processInfo.Arguments = ($ArgumentList | ForEach-Object { ConvertTo-ProcessArgument -Value $_ }) -join " "
    $processInfo.UseShellExecute = $false
    $processInfo.RedirectStandardOutput = $true
    $processInfo.RedirectStandardError = $true
    $processInfo.CreateNoWindow = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $processInfo

    try {
        $null = $process.Start()
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()
        $process.WaitForExit()
        $stdout = $stdoutTask.Result
        $stderr = $stderrTask.Result

        return [pscustomobject]@{
            ExitCode = $process.ExitCode
            Output = ($stdout + $stderr).Trim()
        }
    }
    finally {
        $process.Dispose()
    }
}

function Get-MermaidRenderer {
    param(
        [Parameter(Mandatory = $true)]
        [bool]$UseNpxRenderer
    )

    if ($UseNpxRenderer) {
        $npx = Get-Command npx.cmd -ErrorAction SilentlyContinue
        if ($null -eq $npx) {
            $npx = Get-Command npx -ErrorAction SilentlyContinue
        }
        if ($null -eq $npx) {
            throw "npx is not available in PATH. Install Node.js/npm or install Mermaid CLI as mmdc."
        }

        return [pscustomobject]@{
            Executable = $npx.Source
            PrefixArguments = @("--yes", "@mermaid-js/mermaid-cli")
            Name = "npx @mermaid-js/mermaid-cli"
        }
    }

    $mmdc = Get-Command mmdc.cmd -ErrorAction SilentlyContinue
    if ($null -eq $mmdc) {
        $mmdc = Get-Command mmdc -ErrorAction SilentlyContinue
    }
    if ($null -eq $mmdc) {
        throw "mmdc is not available in PATH. Install @mermaid-js/mermaid-cli globally, or rerun this script with -UseNpx."
    }

    return [pscustomobject]@{
        Executable = $mmdc.Source
        PrefixArguments = @()
        Name = "mmdc"
    }
}

function Write-ReportFiles {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Results,

        [Parameter(Mandatory = $true)]
        [string]$OutputDirectory,

        [Parameter(Mandatory = $true)]
        [string]$RepoRoot
    )

    $jsonPath = Join-Path $OutputDirectory "report.json"
    $markdownPath = Join-Path $OutputDirectory "report.md"

    $json = $Results | ConvertTo-Json -Depth 8
    [System.IO.File]::WriteAllText($jsonPath, $json, [System.Text.Encoding]::UTF8)

    $passed = @($Results | Where-Object { $_.Status -eq "passed" })
    $failed = @($Results | Where-Object { $_.Status -eq "failed" })

    $reportLines = New-Object System.Collections.Generic.List[string]
    $reportLines.Add("Author: VietVunVut (Viet - Nguyen Xuan); GitHub: https://github.com/AIhugART/; Facebook: https://www.facebook.com/xuanviet")
    $reportLines.Add("")
    $reportLines.Add("# Mermaid Render Report")
    $reportLines.Add("")
    $reportLines.Add("- Checked blocks: $($Results.Count)")
    $reportLines.Add("- Passed: $($passed.Count)")
    $reportLines.Add("- Failed: $($failed.Count)")
    $reportLines.Add("")

    if ($failed.Count -gt 0) {
        $reportLines.Add("## Failed")
        $reportLines.Add("")
        foreach ($result in $failed) {
            $errorOneLine = $result.Error -replace "`r?`n", " "
            $reportLines.Add("- $($result.SourcePath) block $($result.BlockIndex), line $($result.StartLine)")
            $reportLines.Add("  - Error: $errorOneLine")
            if ($result.MmdPath) {
                $reportLines.Add("  - Extracted source: $($result.MmdPath)")
            }
        }
        $reportLines.Add("")
    }

    if ($passed.Count -gt 0) {
        $reportLines.Add("## Passed")
        $reportLines.Add("")
        foreach ($result in $passed) {
            $previewPath = Get-RelativePath -BasePath $OutputDirectory -TargetPath (Resolve-RepoPath -InputPath $result.OutputPath -RepoRoot $RepoRoot)
            $previewPath = $previewPath.Replace([System.IO.Path]::DirectorySeparatorChar, '/')
            $reportLines.Add("- $($result.SourcePath) block $($result.BlockIndex), line $($result.StartLine) -> [$($result.OutputFile)]($previewPath)")
        }
        $reportLines.Add("")
    }

    [System.IO.File]::WriteAllLines($markdownPath, $reportLines, [System.Text.Encoding]::UTF8)
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$outputFullPath = Resolve-RepoPath -InputPath $OutputDir -RepoRoot $repoRoot
$mmdOutputDir = Join-Path $outputFullPath "mmd"
$previewOutputDir = Join-Path $outputFullPath "preview"

$null = [System.IO.Directory]::CreateDirectory($outputFullPath)
$null = [System.IO.Directory]::CreateDirectory($mmdOutputDir)
$null = [System.IO.Directory]::CreateDirectory($previewOutputDir)

$renderer = Get-MermaidRenderer -UseNpxRenderer ([bool]$UseNpx)
$markdownFiles = @(Get-MarkdownFiles -InputPaths $Path -RepoRoot $repoRoot -IncludeArchivePaths ([bool]$IncludeArchives))
$results = New-Object System.Collections.Generic.List[object]

foreach ($markdownFile in $markdownFiles) {
    $relativePath = Get-RelativePath -BasePath $repoRoot -TargetPath $markdownFile
    $blocks = @(Get-MermaidBlocks -FilePath $markdownFile)

    foreach ($block in $blocks) {
        $safeBaseName = Get-SafeName -Value $relativePath
        $outputBaseName = "$safeBaseName.block-$($block.Index).line-$($block.StartLine)"
        $mmdPath = Join-Path $mmdOutputDir "$outputBaseName.mmd"
        $previewPath = Join-Path $previewOutputDir "$outputBaseName.$Format"

        [System.IO.File]::WriteAllText($mmdPath, $block.Content, [System.Text.Encoding]::UTF8)

        if (-not $block.IsTerminated) {
            $results.Add([pscustomobject]@{
                SourcePath = $relativePath
                BlockIndex = $block.Index
                StartLine = $block.StartLine
                Status = "failed"
                OutputFile = $null
                OutputPath = $null
                MmdPath = Get-RelativePath -BasePath $repoRoot -TargetPath $mmdPath
                Error = "Mermaid fenced code block is not terminated."
            })
            continue
        }

        $arguments = @($renderer.PrefixArguments + @("-i", $mmdPath, "-o", $previewPath, "-b", "transparent"))
        $renderResult = Invoke-ExternalProcess -FilePath $renderer.Executable -ArgumentList $arguments

        if (($renderResult.ExitCode -eq 0) -and (Test-Path -LiteralPath $previewPath -PathType Leaf)) {
            $results.Add([pscustomobject]@{
                SourcePath = $relativePath
                BlockIndex = $block.Index
                StartLine = $block.StartLine
                Status = "passed"
                OutputFile = [System.IO.Path]::GetFileName($previewPath)
                OutputPath = Get-RelativePath -BasePath $repoRoot -TargetPath $previewPath
                MmdPath = if ($KeepMmd) { Get-RelativePath -BasePath $repoRoot -TargetPath $mmdPath } else { $null }
                Error = $null
            })

            if (-not $KeepMmd) {
                Remove-Item -LiteralPath $mmdPath -Force
            }
            continue
        }

        $errorText = $renderResult.Output
        if ([string]::IsNullOrWhiteSpace($errorText)) {
            $errorText = "Renderer exited with code $($renderResult.ExitCode) and did not create output."
        }

        $results.Add([pscustomobject]@{
            SourcePath = $relativePath
            BlockIndex = $block.Index
            StartLine = $block.StartLine
            Status = "failed"
            OutputFile = $null
            OutputPath = $null
            MmdPath = Get-RelativePath -BasePath $repoRoot -TargetPath $mmdPath
            Error = $errorText
        })
    }
}

$resultArray = $results.ToArray()
Write-ReportFiles -Results $resultArray -OutputDirectory $outputFullPath -RepoRoot $repoRoot

$passedCount = @($resultArray | Where-Object { $_.Status -eq "passed" }).Count
$failedCount = @($resultArray | Where-Object { $_.Status -eq "failed" }).Count

Write-Output "Renderer: $($renderer.Name)"
Write-Output "Markdown files scanned: $($markdownFiles.Count)"
Write-Output "Mermaid blocks checked: $($results.Count)"
Write-Output "Passed: $passedCount"
Write-Output "Failed: $failedCount"
Write-Output "Report: $(Get-RelativePath -BasePath $repoRoot -TargetPath (Join-Path $outputFullPath "report.md"))"

if ($failedCount -gt 0) {
    throw "$failedCount Mermaid block(s) failed render check. See report for details."
}
