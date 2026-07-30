"""
MyEngineer Manufacturing Agent

AI производственный инженер.

Назначение:

- выбор технологии производства;
- выбор принтера;
- подбор процесса изготовления;
- подготовка производства.
"""


class ManufacturingAgent:
    """
    AI агент производства.
    """


    def __init__(self):

        self.name = "Manufacturing Agent"


        self.printers = {


            "QIDI Max4 Combo": {

                "type": "FDM Large Format",

                "role": [

                    "инженерные детали",

                    "большие корпуса",

                    "функциональные компоненты",

                    "прочные изделия"

                ],

                "materials": [

                    "ABS",

                    "ASA",

                    "PETG",

                    "PA",

                    "PA-CF",

                    "PC"

                ]

            },


            "Maestro Solo": {

                "type": "FDM Production",

                "role": [

                    "серийное производство",

                    "коммерческие изделия",

                    "запчасти",

                    "аксессуары"

                ],

                "materials": [

                    "PLA",

                    "PETG",

                    "ABS",

                    "ASA",

                    "TPU"

                ]

            },


            "Apex Maker Mini SLA": {

                "type": "SLA Resin",

                "role": [

                    "детальные прототипы",

                    "фигурки",

                    "дизайн",

                    "мастер-модели"

                ],

                "materials": [

                    "Standard Resin",

                    "Tough Resin",

                    "ABS-like Resin"

                ]

            }

        }



    def select_machine(self, product_type):

        """
        Выбор оборудования.

        В будущем:

        - AI анализ геометрии;
        - расчёт стоимости;
        - анализ времени производства.
        """


        product_type = product_type.lower()


        if any(word in product_type for word in [

            "фигур",

            "миниатюр",

            "ювелир",

            "детализация"

        ]):

            machine = "Apex Maker Mini SLA"


        elif any(word in product_type for word in [

            "серия",

            "партия",

            "товар",

            "аксессуар"

        ]):

            machine = "Maestro Solo"


        else:

            machine = "QIDI Max4 Combo"



        return {


            "product":

                product_type,


            "recommended_machine":

                machine,


            "reason":

                self.printers[machine]["role"]

        }



    def show_printers(self):

        print("=== MyEngineer Production Equipment ===")


        for printer in self.printers:

            print("-", printer)



if __name__ == "__main__":


    factory_ai = ManufacturingAgent()


    factory_ai.show_printers()


    result = factory_ai.select_machine(

        "Прочная автомобильная деталь"

    )


    print("\n=== Production Recommendation ===")


    for key, value in result.items():

        print(key, ":", value)
