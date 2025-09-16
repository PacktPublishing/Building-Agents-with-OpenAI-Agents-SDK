from agents import Agent, Runner, SQLiteSession

# Number of messages
WINDOW_SIZE = 3

# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agents that answers questions.",
)

# Create a session
session = SQLiteSession("first_session")

while True:
    question = input("You: ")
    result = Runner.run_sync(agent, question, session=session)
    print("Agent: ", result.final_output)