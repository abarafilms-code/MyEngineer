"""
MyEngineer CAD AI Agent

AI конструктор.

Создает инженерное задание
для CAD моделирования.
"""


from ai_engine.client import AIClient




class CADAIEngine:



    def __init__(self):


        self.name = "CAD AI Engineer"


        self.ai = AIClient()




    def create_cad_spec(self, engineering_task):


        """
        Создание ТЗ для CAD.
        """


        prompt = f"""

Ты главный инженер-конструктор.


Задача:

{engineering_task}


Подготовь техническое задание
для создания CAD модели.


Укажи:


1. Название детали.


2. Назначение.


3. Геометрию:

- форма
- основные элементы
- поверхности


4. Размеры:

- обязательные размеры
- критические размеры
- допуски


5. Конструктивные элементы:

- отверстия
- крепления
- резьбы
- защелки
- ребра жесткости


6. Требуемый формат:

STEP
STL
3MF


7. Рекомендации для 3D печати.


8. Ориентация печати.


9. Поддержки.


10. Проверка готовой детали.


Оформить как:

CAD ENGINEERING SPECIFICATION

"""



        return self.ai.ask(

            prompt

        )





    def printer_recommendation(self, material):


        """
        Выбор оборудования.
        """


        printers = {


            "SLA":

                "Apex Maker Mini SLA",


            "Large FDM":

                "QIDI Max4 Combo",


            "Production FDM":

                "Maestro Solo"

        }


        return printers.get(

            material,

            "QIDI Max4 Combo"

        )





if __name__ == "__main__":


    cad = CADAIEngine()



    result = cad.create_cad_spec(

        """

Создать усиленный

кронштейн крепления

для автомобиля.

Материал ASA.

"""

    )


    print(result)
