"""
MyEngineer AI Client

Единая точка доступа к AI.

Автоматически выбирает:
- OpenRouter
- Gemini
- GitHub Models
"""


from providers.openrouter import OpenRouterProvider

from providers.gemini import GeminiProvider

from providers.github_models import GitHubModelsProvider


from secrets import Secrets




class AIClient:



    def __init__(self):


        keys = Secrets()


        self.providers = {


            "OpenRouter":

                OpenRouterProvider(

                    keys.openrouter

                ),


            "Gemini":

                GeminiProvider(

                    keys.gemini

                ),


            "GitHub":

                GitHubModelsProvider(

                    keys.github

                )

        }



    def select_provider(self, task):


        """
        Выбор AI по типу задачи.
        """


        task = task.lower()



        if any(word in task for word in [

            "фото",

            "изображение",

            "камера",

            "скан"

        ]):


            return "Gemini"



        if any(word in task for word in [

            "деталь",

            "инженер",

            "cad",

            "конструкция",

            "прочность"

        ]):


            return "OpenRouter"



        return "GitHub"




    def ask(self, prompt):


        provider_name = self.select_provider(

            prompt

        )


        provider = self.providers.get(

            provider_name

        )


        print(

            "AI Provider:",

            provider_name

        )


        if provider is None:


            return {


                "error":

                "Provider unavailable"

            }



        try:


            response = provider.send(

                prompt

            )


            return {


                "provider":

                    provider_name,


                "response":

                    response

            }



        except Exception as error:


            print(

                "Ошибка:",

                error

            )


            return {


                "error":

                    str(error)

            }





if __name__ == "__main__":


    ai = AIClient()



    result = ai.ask(

        "Проанализируй фото автомобильной детали и предложи материал для 3D печати"

    )


    print(result)
