import os
import subprocess
from pathlib import Path


PROJECT = Path("/workspaces/MyEngineer")


def run(cmd):
    print(">", cmd)
    subprocess.run(
        cmd,
        cwd=PROJECT,
        shell=True,
        check=True
    )


def create_file(path, content):

    file = PROJECT / path

    file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file.write_text(
        content,
        encoding="utf-8"
    )

    print("CREATED:", path)



# пример задачи

create_file(
"backend/app/cad_engine/geometry/solid.py",
'''
class SolidGenerator:

    name="solid_generator"

    def run(self, geometry):

        return {
            "solid_model": True,
            "format":[
                "STEP",
                "STL"
            ],
            "geometry": geometry
        }
'''
)


run(
"git add ."
)

run(
'git commit -m "feat: add CAD solid generator agent"'
)

run(
"git push"
)


print(
"MYENGINEER DEVELOPER AGENT COMPLETE"
)
