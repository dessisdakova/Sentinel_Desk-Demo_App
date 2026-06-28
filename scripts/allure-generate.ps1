# Build a static Allure HTML report in allure-report/ via Docker.
# No local Allure CLI or Java required. Run from anywhere in the repo.

$ErrorActionPreference = "Stop"

$AllureImage = "andgineer/allure:2.32.0"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$ResultsDir = Join-Path $RepoRoot "allure-results"
$ReportDir = Join-Path $RepoRoot "allure-report"

if (-not (Test-Path $ResultsDir)) {
    Write-Error @"
allure-results/ not found at $ResultsDir

Run tests first, for example:
  pytest -m smoke -v --alluredir=allure-results
"@
}

New-Item -ItemType Directory -Force -Path $ReportDir | Out-Null

docker run --rm `
    -v "${ResultsDir}:/allure-results" `
    -v "${ReportDir}:/allure-report" `
    $AllureImage `
    allure generate /allure-results -o /allure-report --clean

Write-Host "Report written to $ReportDir"
Write-Host "Open allure-report/index.html in a browser."
