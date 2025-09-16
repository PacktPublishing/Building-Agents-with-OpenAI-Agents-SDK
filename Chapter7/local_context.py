from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool

@dataclass
class OrderContext:
    customer_name: str
    order_id: str
    shipping_status: str

order_context = OrderContext(
    customer_name="Henry Habib",
    order_id="123",
    shipping_status="Delayed"
)

@function_tool
def get_shipping_status(wrapper: RunContextWrapper[OrderContext]) -> str:
    """Provide the shipping status for the current order."""
    ctx = wrapper.context
    return (
        f"Hi {ctx.customer_name}, your order {ctx.order_id} is currently: "
        f"{ctx.shipping_status}."
    )

agent = Agent[OrderContext](
    name="Shipping Support Agent",
    instructions="You are a helpful support agent who can check the shipping status of a user's order.",
    tools=[get_shipping_status]
)

question = "Where is my order?"
result = Runner.run_sync(agent, input=question, context=order_context)
print(result.final_output)
