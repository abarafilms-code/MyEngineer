"""
MyEngineer Knowledge Base

Инженерная база знаний.

Хранит:

- материалы;
- оборудование;
- технологии;
- правила проектирования;
- производственный опыт.
"""


import json

import os




class KnowledgeBase:



    def __init__(self):


        self.file = "database/knowledge.json"


        self.create_database()




    def create_database(self):


        if not os.path.exists(self.file):


            knowledge = {


                "materials": {},


                "printers": {},


                "engineering_rules": []

            }



            with open(

                self.file,

                "w",

                encoding="utf-8"

            ) as f:


                json.dump(

                    knowledge,

                    f,

                    indent=4,

                    ensure_ascii=False

                )





    def load(self):


        with open(

            self.file,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)





    def save(self, data):


        with open(

            self.file,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )





    def add_rule(self, rule):


        data = self.load()



        data["engineering_rules"].append(

            rule

        )



        self.save(data)





    def add_material(

        self,

        name,

        properties

    ):


        data = self.load()



        data["materials"][name] = properties



        self.save(data)





    def add_printer(

        self,

        name,

        capabilities

    ):


        data = self.load()



        data["printers"][name] = capabilities



        self.save(data)





    def show(self):


        data = self.load()



        print(

            "=== MyEngineer Knowledge Base ==="

        )


        print(data)





if __name__ == "__main__":


    kb = KnowledgeBase()



    kb.add_material(

        "ASA",

        {

            "UV":

                "high",


            "outdoor":

                True,


            "car_parts":

                True

        }

    )



    kb.add_printer(

        "QIDI Max4 Combo",

        {

            "large_parts":

                True,


            "engineering_materials":

                True

        }

    )



    kb.add_rule(

        "Для наружных автомобильных деталей использовать ASA"

    )



    kb.show()
