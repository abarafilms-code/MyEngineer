from datetime import datetime


class EngineeringContext:

    def __init__(self, task):

        self.data = {

            "project": {
                "task": task,
                "created": str(datetime.now())
            },

            "requirements": {},

            "geometry": {
                "parameters": {},
                "volume_mm3": None,
                "mass_grams": None
            },

            "material": {
                "name": None,
                "strength": None,
                "temperature_limit": None
            },

            "manufacturing": {
                "process": None,
                "printer": None,
                "print_time_hours": None,
                "cost": None
            },

            "validation": {
                "stress": None,
                "thermal": None,
                "tolerance": None
            },

            "decisions": [],

            "history": []

        }


    def update(self, section, values):

        if section not in self.data:

            self.data[section] = {}


        self.data[section].update(
            values
        )


    def add_decision(self, agent, decision):

        self.data["decisions"].append(
            {
                "agent": agent,
                "decision": decision,
                "timestamp": str(datetime.now())
            }
        )


    def add_history(self, event):

        self.data["history"].append(
            {
                "event": event,
                "timestamp": str(datetime.now())
            }
        )


    def get(self):

        return self.data


    def summary(self):

        return {

            "task":
                self.data["project"]["task"],

            "requirements":
                bool(self.data["requirements"]),

            "geometry":
                bool(self.data["geometry"]["parameters"]),

            "material":
                self.data["material"]["name"],

            "manufacturing":
                self.data["manufacturing"],

            "validation":
                self.data["validation"]

        }
