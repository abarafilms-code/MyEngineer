"""
MyEngineer Cost Calculator

Расчет себестоимости 3D производства.

Учитывает:

- материал;
- вес детали;
- время печати;
- оборудование;
- прибыль.
"""


class CostCalculator:



    def __init__(self):


        self.name = "Production Cost AI"



        self.material_prices = {


            "PLA": 1800,

            "PETG": 2000,

            "ABS": 2200,

            "ASA": 2800,

            "PA-CF": 6000,

            "SLA Resin": 4500

        }



        self.printer_cost = {


            "QIDI Max4 Combo": 80,

            "Maestro Solo": 60,

            "Apex Maker Mini SLA": 50

        }




    def calculate(

        self,

        material,

        weight,

        hours,

        printer

    ):


        """
        Расчет стоимости.
        
        weight - граммы
        hours - время печати
        """



        material_price = (

            self.material_prices.get(

                material,

                2000

            )

            / 1000

        )



        plastic_cost = (

            material_price *

            weight

        )



        machine_cost = (

            self.printer_cost.get(

                printer,

                70

            )

            *

            hours

        )



        electricity = hours * 10



        total = (

            plastic_cost +

            machine_cost +

            electricity

        )



        sale_price = total * 3



        return {


            "material_cost":

                round(plastic_cost,2),


            "machine_cost":

                round(machine_cost,2),


            "electricity":

                electricity,


            "cost_price":

                round(total,2),


            "recommended_price":

                round(sale_price,2)

        }





if __name__ == "__main__":



    calc = CostCalculator()



    result = calc.calculate(

        "ASA",

        350,

        12,

        "QIDI Max4 Combo"

    )



    print(result)
