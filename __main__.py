import uvicorn
from a2a.server.tasks import InMemoryTaskStore
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.apps import A2AStarletteApplication
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agent_executor import GreetingAgentExecutor

# TODO: 
'''
- create a .venv and pip install all the dependencies
- ensure that when you hover over an imported function it will show the description and inputs, etc. 
- draw a flow diagram of the inputs to the server that we create. We use A2AStarletteApplication to create a simple server.
    - can we use other functions to start servers?
    - how do I put multiple agents to start up on a server?
    - what kind of information is being passed through port 9999
'''

def main():
    # Add the skill of the specific agent
    skill = AgentSkill(
        id = "hello_world",
        name = "Greet",
        description = "Return a greeting",
        tags = ["greeting", "hello","world"],
        examples = ["Hey", "Hello", "Hi"], 
    )
# this is what the agent can do,
    agent_card = AgentCard(
        name = "Greeting Agent",
        description= "A simple agent that returns a greeting",
        url = "http://localhost:9999/",
        defaultInputModes = ["text"],
        defaultOutputModes = ["text"],
        skills = [skill],
        version= "1.0.0",
        capabilities= AgentCapabilities(),
    )

    request_handler = DefaultRequestHandler(
        agent_executor = GreetingAgentExecutor(),
        task_store = InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        http_handler = request_handler,
        agent_card = agent_card,
    )

    uvicorn.run(server.build(), host ="0.0.0.0", port = 9999)

if __name__ =="__main__":
        main()