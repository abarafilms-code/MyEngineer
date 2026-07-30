"""
MyEngineer Main Core

Главное ядро системы.

Подключает:

- AI Dispatcher
- Vision Agent
- Engineering Agent
- CAD Agent
- Material Agent
- Manufacturing Agent
- Product Agent
"""


from ai_engine.dispatcher import AIDispatcher


from vision_agent.vision import VisionAgent

from engineering_agent.engineering import EngineeringAgent

from cad_agent.cad import CADAgent

from material_agent.material import MaterialAgent

from manufacturing_agent.manufacturing import ManufacturingAgent

from product_agent.product import ProductAgent




class MyEngineerSystem:



    def __init__(self):


        self.ai = AIDispatcher()


        self.vision = VisionAgent()


        self.engineering = EngineeringAgent()


        self.cad = CADAgent()


        self.material = MaterialAgent()


        self.manufacturing = ManufacturingAgent()


        self.product = ProductAgent()




    def run(self, request):


        print("\n====================")

        print(" MYENGINEER AI ")

        print("====================")



        print("\nЗапрос:")

        print(request)



        # Выбор AI


        print("\nAI Dispatcher:")


        ai_result = self.ai.process(

            request

        )


        print(ai_result)



        # Инженерный процесс


        print("\nEngineering Pipeline")



        print(

            "1. Анализ объекта"

        )



        print(

            "2. Инженерное решение"

        )



        print(

            "3. CAD подготовка"

        )



        print(

            "4. Материал"

        )



        print(

            "5. Производство"

        )



        print(

            "6. Продукт"

        )



        return ai_result





if __name__ == "__main__":



    system = MyEngineerSystem()



    system.run(

        "Создать автомобильную деталь по фотографии и подготовить производство на QIDI Max4 Combo"

    )
