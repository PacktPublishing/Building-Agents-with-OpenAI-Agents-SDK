from agents import Agent, Runner, SQLiteSession, trace
import concurrent.futures

# Create our agents
roles = [
    "Urban Planner", "Artist", "Chef", "Engineer", "Teacher",
    "Doctor", "Mechanic", "Lawyer", "Historian", "Environmentalist"
]

city_agents = [
    Agent(
        name=f"{role} Agent",
        instructions=f"You are a {role.lower()}. Answer the question: 'If you were to design your dream city from scratch, what would it have?' Be creative and imaginative, but concise"
    ) for role in roles
]

# Define the summary agent
summary_agent = Agent(
    name="City Design Aggregator",
    instructions="You are a city designer. You’ve just received 10 creative responses from different citizens. Read all of their responses and consolidate them into a cohesive, imaginative, and well-rounded city plan."
)

# Create a session
session = SQLiteSession("swarm")
conversation_history = []

with trace("Swarm system"):
    prompt = "Design your dream city from scratch. What would it have?"

    # Collect individual responses one by one
    for agent in city_agents:
        result = Runner.run_sync(agent, prompt, session=session)
        print(f"{agent.name}: {result.final_output}\n")
        conversation_history.append(f"{agent.name}: {result.final_output}")

    # Combine responses into one prompt
    combined_responses = "\n\n".join(conversation_history)
    final_result = Runner.run_sync(summary_agent, combined_responses, session=session)

    # Output the final city plan
    print("\nFinal City Design Summary:")
    print(final_result.final_output)