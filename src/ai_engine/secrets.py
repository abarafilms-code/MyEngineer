"""
MyEngineer Secrets Manager

Загрузка API ключей.
"""


import os

from dotenv import load_dotenv



load_dotenv()



class Secrets:



    def __init__(self):


        self.openrouter = os.getenv(

            "OPENROUTER_API_KEY"

        )


        self.gemini = os.getenv(

            "GEMINI_API_KEY"

        )


        self.github = os.getenv(

            "GITHUB_TOKEN"

        )



    def status(self):


        return {


            "OpenRouter":

                bool(self.openrouter),


            "Gemini":

                bool(self.gemini),


            "GitHub":

                bool(self.github)

        }




if __name__ == "__main__":


    secrets = Secrets()


    print(

        secrets.status()

    )
