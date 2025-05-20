#!/bin/bash
# Install project dependencies
set -e

if [ ! -f requirements.txt ]; then
  echo "requirements.txt not found" >&2
  exit 1
fi

python -m pip install --upgrade pip
pip install -r requirements.txt
