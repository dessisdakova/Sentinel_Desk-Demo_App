#!/usr/bin/env bash
# Serve an Allure HTML report from allure-results/ via Docker.
# No local Allure CLI or Java required.

set -euo pipefail

ALLURE_IMAGE="andgineer/allure:2.32.0"
PORT=5050
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RESULTS_DIR="${REPO_ROOT}/allure-results"

if [[ ! -d "${RESULTS_DIR}" ]]; then
  echo "allure-results/ not found at ${RESULTS_DIR}" >&2
  echo "Run tests first, for example:" >&2
  echo "  pytest -m smoke -v --alluredir=allure-results" >&2
  exit 1
fi

echo "Serving Allure report at http://localhost:${PORT} (Ctrl+C to stop)"
echo "Results: ${RESULTS_DIR}"

docker run --rm -p "${PORT}:${PORT}" \
  -v "${RESULTS_DIR}:/allure-results" \
  "${ALLURE_IMAGE}" \
  allure serve /allure-results -h 0.0.0.0 -p "${PORT}"
