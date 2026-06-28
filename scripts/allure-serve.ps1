# Serve an Allure HTML report from allure-results/ via Docker.
# No local Allure CLI or Java required. Run from anywhere in the repo.

$ErrorActionPreference = "Stop"

$AllureImage = "andgineer/allure:2.32.0"
$Port = 5050
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$ResultsDir = Join-Path $RepoRoot "allure-results"

if (-not (Test-Path $ResultsDir)) {
    Write-Error @"
allure-results/ not found at $ResultsDir

Run tests first, for example:
  pytest -m smoke -v --alluredir=allure-results
"@
}

Write-Host "Serving Allure report at http://localhost:$Port (Ctrl+C to stop)"
Write-Host "Results: $ResultsDir"

docker run --rm -p "${Port}:${Port}" `
    -v "${ResultsDir}:/allure-results" `
    $AllureImage `
    allure serve /allure-results -h 0.0.0.0 -p $Port
