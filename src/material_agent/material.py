"""
MyEngineer Material Agent

AI специалист по выбору материалов.

Назначение:

- анализировать требования детали;
- подбирать материал;
- учитывать условия эксплуатации;
- связывать материал с оборудованием производства.
"""


class MaterialAgent:
    """
    AI агент материаловедения.
    """


    def __init__(self):

        self.name = "Material Agent"


        self.materials = {


            "PETG": {

                "strength": "средняя",

                "temperature": "80°C",

                "printer": [

                    "Maestro Solo",

                    "QIDI Max4 Combo"

                ]

            },


            "ASA": {

                "strength": "высокая",

                "temperature": "100°C",

                "features": [

                    "UV стойкость",

                    "наружное применение"

                ],

                "printer": [

                    "QIDI Max4 Combo"

                ]

            },


            "PA-CF": {

                "strength": "очень высокая",

                "temperature": "150°C+",

                "features": [

                    "углеволокно",

                    "жёсткость",

                    "износостойкость"

                ],

                "printer": [

                    "QIDI Max4 Combo"

                ]

            },


            "ABS": {

                "strength": "высокая",

                "temperature": "100°C",

                "printer": [

                    "QIDI Max4 Combo",

                    "Maestro Solo"

                ]

            },


            "SLA Resin": {

                "strength": "зависит от типа смолы",

                "temperature": "разная",

                "features": [

                    "высокая детализация",

                    "гладкая поверхность"

                ],

                "printer": [

                    "Apex Maker Mini SLA"

                ]

            }

        }



    def recommend_material(self, requirements):

        """
        Подбор материала.

        В будущем:

        - подключение AI;
        - расчёт нагрузок;
        - база испытаний.
        """


        result = {


            "requirements":

                requirements,


            "recommended_material":

                "PA-CF",


            "reason":

                [

                    "Высокая прочность",

                    "Подходит для инженерных деталей",

                    "Совместим с QIDI Max4 Combo"

                ],


            "recommended_printer":

                "QIDI Max4 Combo"


        }


        return result



    def show_materials(self):

        print("=== Available Materials ===")


        for material in self.materials:

            print("-", material)



if __name__ == "__main__":


    material_ai = MaterialAgent()


    material_ai.show_materials()


    result = material_ai.recommend_material(

        "Прочная автомобильная деталь с нагрузкой"

    )


    print("\n=== Recommendation ===")


    for key, value in result.items():

        print(key, ":", value)
