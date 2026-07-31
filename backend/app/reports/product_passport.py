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
