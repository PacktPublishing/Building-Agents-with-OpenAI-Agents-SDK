from agents import Agent, Runner, WebSearchTool, CodeInterpreterTool
from agents.tool import CodeInterpreter

# Instantiate the tool
websearchtool = WebSearchTool()

# Create a worker agent
location_agent = Agent(
    name="LocationAgent",
    instructions="You are an AI agent that searches the web and gets latitude and longitude numbers for a particular city.",
    tools=[websearchtool]
)

# Instantiate the tool
tool_config = CodeInterpreter(
    container={"type":"auto"},
    type="code_interpreter"       
)
codetool = CodeInterpreterTool(tool_config=tool_config)

# Create another worker agent
distance_calculator_agent = Agent(
    name="DistanceCalculatorAgent",
    instructions="You are an AI agent that writes and runs Python code to calculate the distance in KM between two latitude/longitude points.",
    tools=[codetool]
)

# Create the orchestrator agent
agent = Agent(
    name="Agent",
    instructions="You are an AI agent that calculates the distance between two locations. Use the Location Agent to get the latitude / longitude. Use the Distance Calculator agent to calculate the distance.",
    tools=[
        location_agent.as_tool(
            tool_name="LocationAgent",
            tool_description="Returns the latitude and longitude for a particular location"
        ), 
        distance_calculator_agent.as_tool(
            tool_name="DistanceCalculatorAgent",
            tool_description="Calculates the distance between two latitude/longitude points"
        )]
)

result = Runner.run_sync(agent, "What's the straight-line distance between Toronto and Vancouver?")
print(result.final_output)