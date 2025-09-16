from agents import Agent, Runner, SQLiteSession, trace, function_tool
from agents.extensions.visualization import draw_graph

# Create tools
@function_tool
def calculate_physics_equation(equation):
    pass

@function_tool
def perform_culture_survey(goal):
    pass

# Create our agents
# Specialized science agents
physics_agent = Agent(name="Physics Agent", instructions="Answer questions about physics.", tools=[calculate_physics_equation])
chemistry_agent = Agent(name="Chemistry Agent", instructions="Answer questions about chemistry.")
medical_agent = Agent(name="Medical Agent", instructions="Answer questions about medical science.")

# Specialized history agents
politics_agent = Agent(name="Politics Agent", instructions="Answer questions about political history.")
warfare_agent = Agent(name="Warfare Agent", instructions="Answer questions about wars and military history.")
culture_agent = Agent(name="Culture Agent", instructions="Answer questions about cultural history.", tools=[perform_culture_survey])

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

# Draw agent graph
draw_graph(triage_agent, filename="graph_visualization")