# Required imports
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, ModelSettings

# Load environment variables from the .env file
load_dotenv()

@function_tool
def calculate_mortgage(principal_amount: float, annualized_rate: float, number_of_years: int) -> str:
    """
    This function calculates the mortgage payment.
    
    Args:
        principal_amount: The mortgage amount.
        annual_rate: The annualized interest rate in percent form.
        years: The loan term in years.
    Returns:
        A message stating the monthly payment amount.
    """
    monthly_rate = (annualized_rate / 100) / 12
    months = number_of_years * 12
    payment = principal_amount * (monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    print(payment)
    return f"${payment:,.2f}."

# Define an agent that uses the mortgage calculator tool
mortgage_agent = Agent(
    name="MortgageAdvisor",
    instructions=("You are a mortgage assistant"),
    tools=[calculate_mortgage],
    tool_use_behavior="stop_on_first_tool",
    model_settings=ModelSettings(
        tool_choice="required"
    )
)

# Run the agent with an example question
result = Runner.run_sync(mortgage_agent, "What is my monthly payments if I borrow $800,000 at 6% interest for 30 years?")
print(result.final_output)
