"""
MyEngineer RO System Demo

Runs the first complete engineering pipeline.
"""

from core.orchestrator.orchestrator import CoreOrchestrator, EngineeringRequest
from agents.research_agent.agent import ResearchAgent
from agents.engineering_agent.agent import EngineeringAgent
from agents.supply_chain_agent.agent import SupplyChainAgent
from agents.manufacturing_agent.agent import ManufacturingAgent
from core.report_generator.engineering_report import build_report


request = EngineeringRequest(
    "Create mobile RO system 400 l/h for high rise cleaning"
)

orchestrator = CoreOrchestrator()

orchestrator.register_agent(ResearchAgent())
orchestrator.register_agent(EngineeringAgent())
orchestrator.register_agent(SupplyChainAgent())
orchestrator.register_agent(ManufacturingAgent())

results = orchestrator.process(request)

report = build_report(
    request.description,
    results["results"]
)

print(report)
