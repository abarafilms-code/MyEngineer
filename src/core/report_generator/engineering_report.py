"""
Engineering Report Generator v0.1
Creates a unified engineering document from agent outputs.
"""


class EngineeringReport:
    def __init__(self, request):
        self.request = request
        self.sections = {}

    def add_section(self, name, data):
        self.sections[name] = data

    def export(self):
        return {
            "project_request": self.request,
            "report": self.sections
        }


def build_report(request, agent_results):
    report = EngineeringReport(request)

    for result in agent_results:
        agent_name = result.get("agent", "unknown")
        report.add_section(agent_name, result)

    return report.export()
