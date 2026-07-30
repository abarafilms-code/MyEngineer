"""
MyEngineer Main System

Главная точка запуска AI-инженера.

Объединяет все инженерные агенты:
- Vision
- Engineering
- CAD
- Material
- Manufacturing
- Product
"""


from orchestrator.main import MyEngineerOrchestrator

from vision_agent.vision import VisionAgent

from engineering_agent.engineering import EngineeringAgent

from cad_agent.cad import CADAgent

from material_agent.material import MaterialAgent

from manufacturing_agent.manufacturing import ManufacturingAgent

from product_agent.product import ProductAgent



class MyEngineerSystem:
    """
    Главная система MyEngineer.
    """


    def __init__(self):

        self.orchestrator = MyEngineerOrchestrator()

        self.vision = VisionAgent()

        self.engineering = EngineeringAgent()

        self.cad = CADAgent()

        self.material = MaterialAgent()

        self.manufacturing = ManufacturingAgent()

        self.product = ProductAgent()



    def run(self, request):

        print("\n======================")

        print(" MYENGINEER AI SYSTEM ")

        print("======================\n")


        print("TASK:")

        print(request)



        print("\n--- Vision Analysis ---")

        vision_result = self.vision.describe_object(

            "input_image.jpg"

        )

        print(vision_result)



        print("\n--- Engineering Analysis ---")

        engineering_result = self.engineering.analyze_part(

            request

        )

        print(engineering_result)



        print("\n--- Material Selection ---")

        material_result = self.material.recommend_material(

            "Инженерная деталь с нагрузкой"

        )

        print(material_result)



        print("\n--- Manufacturing Selection ---")

        manufacturing_result = self.manufacturing.select_machine(

            request

        )

        print(manufacturing_result)



        print("\n--- CAD Planning ---")

        cad_result = self.cad.create_model_plan(

            request

        )

        print(cad_result)



        print("\n--- Product Creation ---")

        product_result = self.product.create_product_card(

            request

        )

        print(product_result)



        print("\n======================")

        print(" ENGINEERING COMPLETE ")

        print("======================")





if __name__ == "__main__":


    system = MyEngineerSystem()


    system.run(

        "Создать улучшенную автомобильную деталь методом 3D печати"

    )
