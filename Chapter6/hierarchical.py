from agents import Agent, Runner, SQLiteSession, trace

# Create our agents
# Specialized science agents
physics_agent = Agent(name="Physics Agent", instructions="Answer questions about physics.")
chemistry_agent = Agent(name="Chemistry Agent", instructions="Answer questions about chemistry.")
medical_agent = Agent(name="Medical Agent", instructions="Answer questions about medical science.")

# Specialized history agents
politics_agent = Agent(name="Politics Agent", instructions="Answer questions about political history.")
warfare_agent = Agent(name="Warfare Agent", instructions="Answer questions about wars and military history.")
culture_agent = Agent(name="Culture Agent", instructions="Answer questions about cultural history.")

# Manager agents with handoffs to their respective domains
science_manager = Agent(
    name="Science Manager",
    instructions="Manage science-related queries and route them to the appropriate subdomain agent.",
    handoffs=[physics_agent, chemistry_agent, medical_agent]
)

history_manager = Agent(
    name="History Manager",
    instructions="Manage history-related queries and route them to the appropriate subdomain agent.",
    handoffs=[politics_agent, warfare_agent, culture_agent]
)

# Top-level triage agent
triage_agent = Agent(
    name="Research Triage Agent",
    instructions="Triage the user's question and decide whether it's science or history related, and route accordingly.",
    handoffs=[science_manager, history_manager]
)

# Create a session
session = SQLiteSession("hierarchy")
last_agent = triage_agent

with trace("Hierarchical system"):
    while True:
        question = input("You: ")
        result = Runner.run_sync(last_agent, question, session=session)
        print("Agent: ", result.final_output)
        last_agent = result.last_agent