"""
OpenRouter Provider

Подключение AI моделей
через OpenRouter API.
"""


import requests



class OpenRouterProvider:



    def __init__(self, api_key):


        self.api_key = api_key


        self.url = (

            "https://openrouter.ai/api/v1/chat/completions"

        )



    def send(self, prompt):


        headers = {


            "Authorization":

                f"Bearer {self.api_key}",


            "Content-Type":

                "application/json"

        }



        data = {


            "model":

                "openrouter/free",


            "messages":

                [

                    {

                        "role":

                            "user",


                        "content":

                            prompt

                    }

                ]

        }



        response = requests.post(

            self.url,

            headers=headers,

            json=data

        )



        return response.json()
