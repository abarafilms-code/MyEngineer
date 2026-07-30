"""
MyEngineer AI Quota Manager

Управление лимитами AI сервисов.

Контролирует:

- количество запросов;
- доступность провайдеров;
- переключение моделей.
"""


import json

import os

from datetime import datetime



class QuotaManager:



    def __init__(self):


        self.file = (

            "database/ai_quota.json"

        )


        self.providers = [

            "OpenRouter",

            "Gemini",

            "GitHub Models"

        ]


        self.create_database()



    def create_database(self):

        """
        Создание файла лимитов,
        если его нет.
        """


        if not os.path.exists(self.file):


            data = {


                "date":

                    str(datetime.now().date()),


                "providers":

                    {}

            }



            for provider in self.providers:


                data["providers"][provider] = {


                    "requests":

                        0,


                    "limit":

                        "unknown",


                    "status":

                        "available"

                }



            with open(

                self.file,

                "w",

                encoding="utf-8"

            ) as f:


                json.dump(

                    data,

                    f,

                    indent=4,

                    ensure_ascii=False

                )



    def load(self):


        with open(

            self.file,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)



    def save(self, data):


        with open(

            self.file,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )



    def add_request(self, provider):


        data = self.load()



        data["providers"][provider]["requests"] += 1



        self.save(data)



    def check_provider(self, provider):

        """
        Проверка доступности.

        Здесь позже подключим:

        - реальные API quota;
        - rate limits.
        """


        data = self.load()



        info = data["providers"].get(

            provider

        )



        if not info:


            return False



        return info["status"] == "available"



    def show_status(self):


        data = self.load()



        print(

            "=== AI QUOTA STATUS ==="

        )



        for name, info in data["providers"].items():


            print(

                name,

                ":",

                info

            )




if __name__ == "__main__":


    quota = QuotaManager()


    quota.show_status()
