"""
MyEngineer Main System

Главное ядро инженерного AI.

Поток:

Фото объекта
        ↓
Vision Agent
        ↓
Database Agent
        ↓
Engineering Agent
        ↓
CAD Agent
        ↓
Material Agent
        ↓
Manufacturing Agent
        ↓
Product Agent
"""


from vision_agent.vision import VisionAgent

from engineering_agent.engineering import EngineeringAgent

from cad_agent.cad import CADAgent

from material_agent.material import MaterialAgent

from manufacturing_agent.manufacturing import ManufacturingAgent

from product_agent.product import ProductAgent

from database_agent.database import DatabaseAgent



class MyEngineerSystem:


    def __init__(self):

        self.vision = VisionAgent()

        self.database = DatabaseAgent()

        self.engineering = EngineeringAgent()

        self.cad = CADAgent()

        self.material = MaterialAgent()

        self.manufacturing = ManufacturingAgent()

        self.product = ProductAgent()



    def run(self, request):


        print("\n======================")

        print(" MYENGINEER AI ")

        print("======================\n")



        print("Задача:")

        print(request)



        # 1. Анализ изображения

        print("\n1. Vision Agent")

        vision_result = self.vision.describe_object(

            "object_photo.jpg"

        )

        print(vision_result)



        # 2. Поиск в памяти

        print("\n2. Database Agent")


        self.database.show_memory()



        # 3. Инженерный анализ

        print("\n3. Engineering Agent")


        engineering_result = self.engineering.analyze_part(

            request

        )

        print(engineering_result)



        # 4. CAD

        print("\n4. CAD Agent")


        cad_result = self.cad.create_model_plan(

            request

        )

        print(cad_result)



        # 5. Материал

        print("\n5. Material Agent")


        material_result = self.material.recommend_material(

            request

        )

        print(material_result)



        # 6. Производство

        print("\n6. Manufacturing Agent")


        manufacturing_result = self.manufacturing.select_machine(

            request

        )

        print(manufacturing_result)



        # 7. Продукт

        print("\n7. Product Agent")


        product_result = self.product.create_product_card(

            request

        )

        print(product_result)



        print("\n======================")

        print("MYENGINEER COMPLETE")

        print("======================")




if __name__ == "__main__":


    my_engineer = MyEngineerSystem()



    my_engineer.run(

        "Создать улучшенную автомобильную деталь для 3D печати"

    )
