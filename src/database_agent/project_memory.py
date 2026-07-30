"""
MyEngineer Project Memory

База инженерного опыта.

Хранит:

- проекты;
- детали;
- материалы;
- производство;
- результаты тестов.
"""


import json

import os

from datetime import datetime




class ProjectMemory:



    def __init__(self):


        self.file = "database/projects.json"


        self.create_database()




    def create_database(self):


        if not os.path.exists(self.file):


            with open(

                self.file,

                "w",

                encoding="utf-8"

            ) as f:


                json.dump(

                    [],

                    f,

                    indent=4,

                    ensure_ascii=False

                )




    def load_projects(self):


        with open(

            self.file,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)




    def save_projects(self, projects):


        with open(

            self.file,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                projects,

                f,

                indent=4,

                ensure_ascii=False

            )




    def add_project(

        self,

        name,

        category,

        material,

        printer

    ):


        projects = self.load_projects()



        project = {


            "id":

                len(projects) + 1,


            "date":

                str(datetime.now()),


            "name":

                name,


            "category":

                category,


            "material":

                material,


            "printer":

                printer,


            "status":

                "prototype"

        }



        projects.append(project)



        self.save_projects(

            projects

        )



        return project




    def show_history(self):


        projects = self.load_projects()



        print(

            "=== PROJECT MEMORY ==="

        )



        for project in projects:


            print(project)





if __name__ == "__main__":


    memory = ProjectMemory()



    memory.add_project(

        "BMW E46 air intake",

        "Tuning",

        "ASA",

        "QIDI Max4 Combo"

    )


    memory.show_history()
