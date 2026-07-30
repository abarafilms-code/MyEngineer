"""
MyEngineer Material AI Agent

AI инженер по выбору материалов.

Учитывает:

- нагрузку;
- температуру;
- окружающую среду;
- технологию производства;
- доступное оборудование.
"""


from ai_engine.client import AIClient




class MaterialAIEngine:



    def __init__(self):


        self.name = "Material AI Engineer"


        self.ai = AIClient()



    def analyze_material(self, task):


        """
        Подбор материала.
        """


        prompt = f"""

Ты инженер по полимерам и 3D производству.


Задача:

{task}


Проанализируй требования.


Определи:


1. Условия эксплуатации:

- температура
- влажность
- UV
- химические воздействия
- вибрации


2. Требуемые свойства:


- прочность
- ударостойкость
- гибкость
- точность
- внешний вид


3. Сравни материалы:


PLA

PETG

ABS

ASA

TPU

PA6-CF

PA12

PC

SLA Resin


4. Выбери лучший материал.


5. Объясни почему.


6. Выбери оборудование:


QIDI Max4 Combo

Maestro Solo

Apex Maker Mini SLA


7. Дай рекомендации по печати:


- температура сопла
- температура стола
- ориентация
- заполнение


Ответ оформить:


MATERIAL ENGINEERING REPORT

"""



        return self.ai.ask(

            prompt

        )




    def quick_selection(self, usage):


        """
        Быстрый выбор материала.
        """


        materials = {


            "автомобильный внешний":

                "ASA",


            "силовая деталь":

                "PA-CF",


            "гибкая деталь":

                "TPU",


            "прототип":

                "PETG",


            "модель":

                "SLA Resin"

        }



        return materials.get(

            usage,

            "PETG"

        )





if __name__ == "__main__":


    material = MaterialAIEngine()



    result = material.analyze_material(

        """

Создать наружный элемент

автомобильного тюнинга.

Деталь будет использоваться

на солнце и под дождем.

"""

    )


    print(result)
