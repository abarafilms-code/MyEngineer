"""
MyEngineer Database Agent

Инженерная память системы.

Назначение:

- загрузка данных;
- поиск деталей;
- хранение проектов;
- накопление опыта производства.
"""


import json

import os



class DatabaseAgent:
    """
    AI агент инженерной базы знаний.
    """


    def __init__(self):

        self.name = "Database Agent"


        self.parts_file = (
            "database/parts.json"
        )


        self.products_file = (
            "database/products.json"
        )



    def load_database(self, file_path):

        """
        Загрузка JSON базы.
        """


        if not os.path.exists(file_path):

            return {}


        with open(
            file_path,
            "r",
            encoding="utf-8"

        ) as file:

            return json.load(file)



    def get_parts(self):

        """
        Получить все детали.
        """

        database = self.load_database(

            self.parts_file

        )


        return database.get(

            "parts",

            []

        )



    def search_part(self, keyword):

        """
        Поиск детали по названию.
        """


        parts = self.get_parts()


        results = []


        for part in parts:

            name = part.get(

                "name",

                ""

            ).lower()


            if keyword.lower() in name:

                results.append(part)


        return results



    def get_products(self):

        """
        Получить список продуктов.
        """


        database = self.load_database(

            self.products_file

        )


        return database.get(

            "products",

            []

        )



    def show_memory(self):

        """
        Показать состояние памяти.
        """


        parts = self.get_parts()

        products = self.get_products()


        print(

            "=== MyEngineer Memory ==="

        )


        print(

            "Parts:",

            len(parts)

        )


        print(

            "Products:",

            len(products)

        )



if __name__ == "__main__":


    database = DatabaseAgent()


    database.show_memory()



    result = database.search_part(

        "Automotive"

    )


    print(

        "\nSearch result:"

    )


    for item in result:

        print(item["name"])
