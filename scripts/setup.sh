#!/bin/bash
# Install Python dependencies for SwiftGenie
set -euo pipefail

if [ ! -f requirements.txt ]; then
  echo "requirements.txt not found" >&2
  exit 1
fi

python -m pip install --upgrade pip
pip install -r requirements.txt
