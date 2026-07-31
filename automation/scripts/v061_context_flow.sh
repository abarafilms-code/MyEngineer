#!/bin/bash

set -e

echo "=== MyEngineer v0.6.1 Context Data Flow ==="


echo "1. Create Product Passport generator"

cat > backend/app/reports/product_passport.py <<'PY'
import json
from pathlib import Path


class ProductPassport:

    def save(self, context):

        path = Path(
            "backend/app/reports/product_passport.json"
        )

        path.write_text(
            json.dumps(
                context.get(),
                indent=4,
                ensure_ascii=False,
                default=str
            )
        )

        print(
            "Product Passport:",
            path
        )
PY


echo "2. Patch pipeline for passport"

python - <<'PY'

from pathlib import Path

p = Path(
"automation/workflows/autonomous_pipeline.py"
)

text = p.read_text()


if "ProductPassport" not in text:

    text = text.replace(
        "from automation.orchestration.agent_router import AgentRouter",
        "from automation.orchestration.agent_router import AgentRouter\nfrom backend.app.reports.product_passport import ProductPassport"
    )


    text = text.replace(
        "print(\n            \"\\nPipeline finished\"",
        """
passport = ProductPassport()

passport.save(
    self.context
)


print(
    "\\nPipeline finished"
"""
    )


p.write_text(text)

PY


echo "3. Compile"

python -m py_compile \
automation/workflows/autonomous_pipeline.py \
backend/app/reports/product_passport.py


echo "4. Run pipeline"

python -m automation.core.controller


echo "5. Check report"

cat backend/app/reports/product_passport.json


echo "=== v0.6.1 COMPLETE ==="

