class OrchestratorV2Agent:

    name = "orchestrator_v2_agent"


    def run(self, context):

        task = context.get(
            "task",
            ""
        ).lower()


        pipeline = []


        if "cad" in task or "design" in task:

            pipeline = [
                "requirements_agent",
                "architect_agent",
                "design_review_agent",
                "failure_prediction_agent",
                "stress_analysis_agent",
                "thermal_analysis_agent",
                "tolerance_agent",
                "cad_generator_agent",
                "material_agent",
                "manufacturing_agent",
                "cost_engine_agent",
                "factory_planner_agent"
            ]


        elif "production" in task:

            pipeline = [
                "production_queue_agent",
                "printer_farm_agent",
                "quality_control_agent"
            ]


        elif "product" in task:

            pipeline = [
                "rd_agent",
                "market_intelligence_agent",
                "customer_agent",
                "ceo_agent"
            ]


        else:

            pipeline = [
                "analyzer_agent",
                "decision_agent"
            ]


        result = {

            "task": task,

            "recommended_pipeline": pipeline,

            "stages": len(pipeline)

        }


        context["orchestration_plan"] = result


        print(
            "Orchestrator V2:",
            result
        )


        return context
