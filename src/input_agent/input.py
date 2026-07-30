"""
MyEngineer Input Agent

Универсальный вход инженерной системы.

Принимает:

- изображение;
- описание;
- тюнинг;
- идею продукта;
- производственную задачу.
"""


class InputAgent:


    def __init__(self):

        self.name = "Input Agent"



    def detect_request_type(self, request):

        """
        Определение типа входного запроса.
        """


        text = request.lower()



        # Тюнинг

        if any(word in text for word in [

            "тюнинг",

            "улучшить",

            "модернизировать",

            "upgrade",

            "performance"

        ]):

            return "tuning"



        # Ремонт

        if any(word in text for word in [

            "сломалась",

            "замена",

            "нет детали",

            "восстановить"

        ]):

            return "repair"



        # Новое изделие

        if any(word in text for word in [

            "создать",

            "придумать",

            "новый продукт",

            "изделие"

        ]):

            return "product"



        # Фото

        if any(word in text for word in [

            "фото",

            "изображение",

            "скан"

        ]):

            return "vision"



        return "engineering"



    def analyze(self, request):


        request_type = self.detect_request_type(

            request

        )


        result = {


            "input":

                request,


            "type":

                request_type,


            "next_agents":

                []

        }



        if request_type == "vision":


            result["next_agents"] = [

                "Vision AI",

                "Engineering AI"

            ]



        elif request_type == "tuning":


            result["next_agents"] = [

                "Engineering AI",

                "CAD Agent",

                "Material Agent",

                "Manufacturing Agent"

            ]



        elif request_type == "repair":


            result["next_agents"] = [

                "Reverse Engineering",

                "CAD Agent",

                "Manufacturing Agent"

            ]



        elif request_type == "product":


            result["next_agents"] = [

                "Product Agent",

                "CAD Agent",

                "Manufacturing Agent"

            ]



        else:


            result["next_agents"] = [

                "Engineering Agent"

            ]



        return result




if __name__ == "__main__":


    agent = InputAgent()



    test = agent.analyze(

        "Улучшить воздухозаборник BMW E46 для тюнинга и напечатать новую деталь"

    )


    print(test)
