from core.orchestrator.orchestrator import CoreOrchestrator, EngineeringRequest
from agents.research_agent.agent import ResearchAgent
from agents.engineering_agent.agent import EngineeringAgent


request = EngineeringRequest(
    "Create mobile RO system 400 l/h for high rise cleaning"
)

orchestrator = CoreOrchestrator()
orchestrator.register_agent(ResearchAgent())
orchestrator.register_agent(EngineeringAgent())

result = orchestrator.process(request)

print(result)
