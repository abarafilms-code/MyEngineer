class ThermalAnalysisAgent:

    name = "thermal_analysis_agent"


    def run(self, context):

        thermal = {

            "operating_temperature_c": 60,

            "material_limit_c": 80,

            "thermal_margin": 20,

            "result": "APPROVE"

        }


        context["thermal_analysis"] = thermal


        print(
            "Thermal Analysis:",
            thermal
        )


        return context
