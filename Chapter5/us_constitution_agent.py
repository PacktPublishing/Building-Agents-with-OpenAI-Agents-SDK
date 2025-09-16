from agents import Agent, Runner, FileSearchTool, SQLiteSession

# Instantiate the tool
filesearchtool = FileSearchTool(vector_store_ids=['vs_687ed4bb479c81919b530ab152f373d8']) # replace with your own vector store ID

# Create an agent
agent = Agent(
    name="USConstitutionTool",
    instructions="You are an AI agent that answers questions from the listed vector store, which has the US Constitution. Answer in one sentence.",
    tools=[filesearchtool]
)

# Create a session
session = SQLiteSession("first_session")

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print("Agent: ", result.final_output)