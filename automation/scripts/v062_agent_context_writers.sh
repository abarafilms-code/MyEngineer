#!/bin/bash

set -e

echo "=== MyEngineer v0.6.2 Agent Context Writers ==="

echo "Compile agents"

python -m py_compile automation/agents/stress_analysis_agent.py
python -m py_compile automation/agents/thermal_analysis_agent.py
python -m py_compile automation/agents/cad_generator_agent.py
python -m py_compile automation/agents/manufacturing_agent.py
python -m py_compile automation/agents/material_agent.py

echo "Run pipeline"

python -m automation.core.controller

echo "Show passport"

cat backend/app/reports/product_passport.json

echo "=== v0.6.2 CHECK COMPLETE ==="
