"""
Google Gemini Provider

Используется для:

- изображений;
- документов;
- анализа объектов.
"""


import requests



class GeminiProvider:



    def __init__(self, api_key):


        self.api_key = api_key



    def send(self, prompt):


        url = (

        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

        )


        headers = {


            "Content-Type":

                "application/json"

        }



        params = {


            "key":

                self.api_key

        }



        data = {


            "contents":

                [

                    {

                        "parts":

                            [

                                {

                                    "text":

                                    prompt

                                }

                            ]

                    }

                ]

        }



        response = requests.post(

            url,

            headers=headers,

            params=params,

            json=data

        )



        return response.json()
