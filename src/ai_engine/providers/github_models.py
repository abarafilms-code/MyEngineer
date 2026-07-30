"""
GitHub Models Provider

AI модели через GitHub API.
"""


import requests



class GitHubModelsProvider:



    def __init__(self, token):


        self.token = token



    def send(self, prompt):


        url = (

        "https://models.inference.ai.azure.com/chat/completions"

        )


        headers = {


            "Authorization":

                f"Bearer {self.token}",


            "Content-Type":

                "application/json"

        }



        data = {


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

            url,

            headers=headers,

            json=data

        )


        return response.json()
