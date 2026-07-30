"""
MyEngineer Configuration

Настройки оборудования,
материалов и производства.
"""


PROJECT_NAME = "MyEngineer"


VERSION = "0.1"



# Производственное оборудование

PRINTERS = {


    "QIDI Max4 Combo": {

        "technology": "FDM",

        "role": "Engineering Production",

        "materials": [

            "ASA",

            "ABS",

            "PA",

            "PA-CF",

            "PC"

        ]

    },


    "Maestro Solo": {

        "technology": "FDM",

        "role": "Serial Production",

        "materials": [

            "PLA",

            "PETG",

            "ABS",

            "ASA",

            "TPU"

        ]

    },


    "Apex Maker Mini SLA": {

        "technology": "SLA",

        "role": "High Detail Prototype",

        "materials": [

            "Standard Resin",

            "Tough Resin",

            "ABS-like Resin"

        ]

    }

}



# Производственные направления

PRODUCT_LINES = [

    "Engineering",

    "Automotive",

    "Industrial",

    "ShowDesign",

    "Collectibles"

]



# Форматы CAD

CAD_FORMATS = [

    "STEP",

    "STL",

    "3MF",

    "OBJ",

    "IGES"

]
