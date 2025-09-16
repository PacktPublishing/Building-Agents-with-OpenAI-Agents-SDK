from agents import Agent, Runner, ImageGenerationTool
from agents.tool import ImageGeneration

# Instantiate the tool
tool_config = ImageGeneration(
    type="image_generation",       
)
imagetool = ImageGenerationTool(tool_config=tool_config)

# Create an agent
agent = Agent(
    name="ImageTool",
    instructions="You are an AI agent that generates images.",
    tools=[imagetool]
)

result = Runner.run_sync(agent, "Generate an image of an elephant.")
print(result.final_output)