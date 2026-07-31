class DecisionEngine:

    def analyze(self, task):

        task = task.lower()


        decision = {
            "task": task,
            "route": None,
            "agents": []
        }


        if "cad" in task or "design" in task or "3d" in task:

            decision["route"] = "cad_manufacturing"

            decision["agents"] = [
                "requirements_agent",
                "architect_agent",
                "material_agent",
                "cad_engineer_agent",
                "cad_generator_agent",
                "stress_analysis_agent",
                "thermal_analysis_agent",
                "manufacturing_agent"
            ]


        elif "product" in task or "idea" in task:

            decision["route"] = "product_rnd"

            decision["agents"] = [
                "product_intelligence_agent",
                "rd_agent",
                "prototype_agent"
            ]


        elif "factory" in task or "production" in task:

            decision["route"] = "factory_operation"

            decision["agents"] = [
                "factory_manager_agent",
                "production_optimizer_agent",
                "printer_farm_agent"
            ]


        else:

            decision["route"] = "general_engineering"

            decision["agents"] = [
                "analyzer_agent",
                "planner_agent"
            ]


        return decision
