from e2b_code_interpreter import Sandbox
from openevals.code.e2b.execution import create_e2b_execution_evaluator
from dotenv import load_dotenv

load_dotenv()
# E2B template with uv and pyright preinstalled
sandbox = Sandbox("OpenEvalsPython")
evaluator = create_e2b_execution_evaluator(
    sandbox=sandbox,
)


CODE = """
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("start", lambda state: state)
builder.add_edge(START,"start")
builder.add_edge("start",END)

graph = builder.compile()
graph.invoke({})
"""

eval_result = evaluator(outputs=CODE)

print(eval_result)