param(
    [Parameter(Mandatory = $true)]
    [string]$Source,

    [Parameter(Mandatory = $true)]
    [string]$Workspace
)

$ErrorActionPreference = 'Stop'

$compiler = 'C:\msys64\ucrt64\bin\g++.exe'
$compilerDirectory = Split-Path -Parent $compiler
$inputFile = Join-Path $Workspace 'input.txt'
$outputFile = Join-Path $Workspace 'output.txt'
$buildDirectory = Join-Path $Workspace '.cp-build'
$executable = Join-Path $buildDirectory 'solution.exe'

if (-not (Test-Path -LiteralPath $compiler)) {
    throw "C++ compiler not found at $compiler"
}

# Also works in VS Code windows opened before the Windows PATH was corrected.
$env:Path = "$compilerDirectory;$env:Path"

if ([IO.Path]::GetExtension($Source) -notin @('.cpp', '.cc', '.cxx', '.c++')) {
    throw 'Open a C++ source file before running this command.'
}

New-Item -ItemType Directory -Force -Path $buildDirectory | Out-Null
if (-not (Test-Path -LiteralPath $inputFile)) {
    New-Item -ItemType File -Path $inputFile | Out-Null
}
if (-not (Test-Path -LiteralPath $outputFile)) {
    New-Item -ItemType File -Path $outputFile | Out-Null
} else {
    # Never leave results from the previous run visible after a new run starts.
    Clear-Content -LiteralPath $outputFile
}

Write-Host "Compiling $Source"
& $compiler '-std=c++17' '-O2' '-Wall' '-Wextra' $Source '-o' $executable
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host 'Running with input.txt...'
$runCommand = '"{0}" < "{1}" > "{2}"' -f $executable, $inputFile, $outputFile
& $env:ComSpec '/d' '/c' $runCommand
if ($LASTEXITCODE -ne 0) {
    throw "Program exited with code $LASTEXITCODE."
}

Write-Host 'Done. Results are in output.txt.' -ForegroundColor Green
