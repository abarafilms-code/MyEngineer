from automation.orchestration.workflow_graph import WorkflowGraph


class AgentRouter:

    def __init__(self):
        self.workflow = WorkflowGraph()
        self.workflow.build_cad_workflow()


    def route(self, task):

        task = task.lower()

        pipeline = []

        if "cad" in task or "design" in task:
            pipeline += [
                "requirements_agent",
                "architect_agent",
                "cad_engineer_agent",
                "cad_generator_agent",
                "stress_analysis_agent",
                "thermal_analysis_agent",
                "manufacturing_agent"
            ]

        if "factory" in task or "production" in task:
            pipeline += [
                "digital_twin_agent",
                "predictive_maintenance_agent",
                "production_optimizer_agent",
                "factory_manager_agent"
            ]

        if "sell" in task or "order" in task:
            pipeline += [
                "customer_order_agent",
                "sales_agent",
                "order_to_factory_agent"
            ]

        if "cad" in task or "design" in task:
            return self.workflow.resolve(
                "requirements_agent"
            )

        return pipeline
