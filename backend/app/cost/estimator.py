class CostEstimator:

    name = "cost_estimator"

    def run(self, idea: str):

        return {
            "material": "ASA",
            "estimated_weight": "850g",
            "print_time": "18h",
            "material_cost": "850 ₽",
            "machine_cost": "900 ₽",
            "energy_cost": "100 ₽",
            "post_processing": "300 ₽",
            "total_cost": "2150 ₽",
            "recommended_price": "4500-6000 ₽",
            "idea": idea
        }
