"""
MyEngineer Reverse Engineering Agent

AI инженер восстановления деталей.


Функции:

- анализ отсутствующих деталей;
- план измерений;
- подготовка CAD задания;
- выбор технологии производства.
"""


from ai_engine.client import AIClient




class ReverseEngineeringAgent:



    def __init__(self):


        self.name = "Reverse Engineering Agent"


        self.ai = AIClient()




    def analyze_part(self, description):


        """
        Анализ детали по описанию.
        """


        prompt = f"""

Ты инженер по обратному проектированию.


Исходные данные:

{description}


Проведи анализ:


1. Определи назначение детали.


2. Какие размеры необходимо снять?


3. Какие поверхности критичны?


4. Какие соединения учитывать:

- защёлки
- резьба
- посадки
- крепления


5. Предложи способ восстановления:

- CAD моделирование
- 3D сканирование
- измерение вручную


6. Выбери материал:


PETG

ABS

ASA

PA-CF

PC


7. Выбери оборудование:


QIDI Max4 Combo

Maestro Solo

Apex Maker Mini SLA


8. Создай техническое задание для конструктора CAD.


Ответ:

ОТЧЁТ REVERSE ENGINEERING

"""



        return self.ai.ask(

            prompt

        )





    def create_measure_plan(self, part):


        """
        План снятия размеров.
        """


        return {


            "part":

                part,


            "measurement":

                [

                    "Габаритные размеры",

                    "Толщина стенок",

                    "Отверстия",

                    "Посадочные места",

                    "Радиусы",

                    "Крепления"

                ],


            "next":

                "CAD reconstruction"

        }





if __name__ == "__main__":



    agent = ReverseEngineeringAgent()



    result = agent.analyze_part(

        """

Сломана пластиковая крышка

мотоцикла.

Оригинал больше не выпускается.

Есть только фотография и остатки детали.

"""

    )


    print(result)
