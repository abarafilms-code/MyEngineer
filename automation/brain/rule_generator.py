class EngineeringRuleGenerator:


    def generate(
        self,
        failures
    ):

        rules=[]


        for failure in failures:


            if failure=="stress_failure":

                rules.append(
                    {
                    "condition":
                    "stress_failure",

                    "action":
                    "increase_wall_thickness",

                    "value":
                    2
                    }
                )


            if failure=="thermal_failure":

                rules.append(
                    {
                    "condition":
                    "thermal_failure",

                    "action":
                    "change_material",

                    "value":
                    "ASA"
                    }
                )


        return rules
