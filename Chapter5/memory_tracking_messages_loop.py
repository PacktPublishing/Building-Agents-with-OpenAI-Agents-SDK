from agents import Agent, Runner

# Create the agent
agent = Agent(
    name="QuestionAnswer",
    instructions="You are an AI agents that answers questions.",
)

messages = []
while True:
    question = input("You: ")
    messages = messages + [{"role": "user", "content": question}]
    result = Runner.run_sync(agent, messages)
    print("Agent: ", result.final_output)
    subsequent_input = messages + result.to_input_list()