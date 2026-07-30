"""
MyEngineer AI Dispatcher

Главный распределитель AI задач.

Выбирает модель
по типу запроса.
"""


from quota_manager import QuotaManager

from router import AIRouter



class AIDispatcher:



    def __init__(self):


        self.router = AIRouter()


        self.quota = QuotaManager()



    def detect_task_type(self, request):

        """
        Определение типа задачи.
        """


        text = request.lower()



        if any(word in text for word in [

            "фото",

            "изображение",

            "деталь",

            "камера"

        ]):

            return "vision"



        if any(word in text for word in [

            "cad",

            "модель",

            "чертеж",

            "stl",

            "step"

        ]):

            return "cad"



        if any(word in text for word in [

            "материал",

            "пластик",

            "прочность"

        ]):

            return "engineering"



        return "general"



    def choose_ai(self, task):


        """
        Выбор AI под задачу.
        """


        if task == "vision":

            return "Gemini"



        if task == "cad":

            return "OpenRouter"



        if task == "engineering":

            return "OpenRouter"



        return "GitHub Models"



    def process(self, request):


        task = self.detect_task_type(

            request

        )


        provider = self.choose_ai(

            task

        )


        print(

            "Task:",

            task

        )


        print(

            "Selected AI:",

            provider

        )



        if self.quota.check_provider(

            provider

        ):


            self.quota.add_request(

                provider

            )


            return {


                "provider":

                    provider,


                "task":

                    task,


                "status":

                    "sent"

            }



        else:


            return {


                "status":

                    "no_available_ai"

            }





if __name__ == "__main__":


    dispatcher = AIDispatcher()



    result = dispatcher.process(

        "Проанализируй фото автомобильной детали"

    )



    print(result)
