#!/bin/bash

set -e

echo "=== MyEngineer v0.6 Context Integration ==="

echo "Checking python..."

python -m py_compile automation/workflows/autonomous_pipeline.py

echo "Running pipeline..."

python -m automation.core.controller

echo "Git status..."

git status

echo "=== v0.6 CHECK COMPLETE ==="
