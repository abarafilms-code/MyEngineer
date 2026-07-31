class FactoryDigitalTwin:


    def __init__(self):

        self.printers = []
        self.jobs = []
        self.materials = []


    def add_printer(
        self,
        name
    ):

        self.printers.append(
            {
                "name": name,
                "status": "idle"
            }
        )


    def add_job(
        self,
        job
    ):

        self.jobs.append(job)


    def state(self):

        return {

            "printers": self.printers,

            "jobs": self.jobs,

            "materials": self.materials

        }
