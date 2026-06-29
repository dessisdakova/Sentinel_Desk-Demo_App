#!/usr/bin/env bash
# Build a static Allure HTML report in allure-report/ via Docker.
# No local Allure CLI or Java required.

set -euo pipefail

ALLURE_IMAGE="andgineer/allure:2.32.0"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RESULTS_DIR="${REPO_ROOT}/allure-results"
REPORT_DIR="${REPO_ROOT}/allure-report"

if [[ ! -d "${RESULTS_DIR}" ]]; then
  echo "allure-results/ not found at ${RESULTS_DIR}" >&2
  echo "Run tests first, for example:" >&2
  echo "  pytest -m smoke -v --alluredir=allure-results" >&2
  exit 1
fi

mkdir -p "${REPORT_DIR}"

docker run --rm \
  -v "${RESULTS_DIR}:/allure-results" \
  -v "${REPORT_DIR}:/allure-report" \
  "${ALLURE_IMAGE}" \
  allure generate /allure-results -o /allure-report --clean

echo "Report written to ${REPORT_DIR}"
echo "Open allure-report/index.html in a browser."
