from pathlib import Path


class CodeWriter:

    def create_file(self, path, content):

        file = Path(path)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "created": str(file)
        }


    def patch_file(self, path, old, new):

        file = Path(path)

        text = file.read_text(
            encoding="utf-8"
        )

        text = text.replace(
            old,
            new
        )

        file.write_text(
            text,
            encoding="utf-8"
        )

        return {
            "patched": str(file)
        }
