#!/bin/bash
# LocalStack init hook (ready.d): seed Secrets Manager from seed_data.json.
# Runs automatically every time LocalStack reaches the "ready" state, so the
# secrets exist after `docker compose up` with no manual bootstrap step.
set -euo pipefail

SEED_FILE="/etc/localstack/seed/seed_data.json"
echo "[init] seeding secrets from ${SEED_FILE}"

# Parse the JSON with the bundled python3 (stdlib only) and create/update each
# secret via awslocal. Idempotent: create first, fall back to put on conflict.
python3 - "$SEED_FILE" <<'PY'
import json
import subprocess
import sys

with open(sys.argv[1], encoding="utf-8") as fh:
    secrets = json.load(fh)

for name, payload in secrets.items():
    secret_string = json.dumps(payload)
    created = subprocess.run(
        ["awslocal", "secretsmanager", "create-secret",
         "--name", name, "--secret-string", secret_string],
        capture_output=True, text=True,
    )
    if created.returncode == 0:
        print(f"[init] created {name}")
    else:
        subprocess.run(
            ["awslocal", "secretsmanager", "put-secret-value",
             "--secret-id", name, "--secret-string", secret_string],
            check=True, capture_output=True, text=True,
        )
        print(f"[init] updated {name}")
PY

echo "[init] secret seeding complete"
