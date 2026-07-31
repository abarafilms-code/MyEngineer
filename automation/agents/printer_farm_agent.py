class PrinterFarmAgent:


    name = "printer_farm_agent"



    def run(
        self,
        context
    ):

        queue = context.get(
            "production_queue",
            []
        )


        printers = 10


        jobs = []


        for item in queue:

            jobs.append({

                "printer":
                    f"Printer-{len(jobs)+1}",

                "product":
                    item["product"],

                "status":
                    "PRINTING"

            })


        context["printer_farm"] = {

            "printers":
                printers,

            "active_jobs":
                jobs

        }


        print(
            "Printer Farm:"
        )

        print(
            context["printer_farm"]
        )


        return context
