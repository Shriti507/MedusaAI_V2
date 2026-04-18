from langgraph.graph import StateGraph, END
from langgraph.graph import StateGraph, END
from state import AgentState

from nodes.planner import planner_node
from nodes.search import search_node
from nodes.retriever import filter_node
from nodes.summarizer import summarizer_node
from nodes.validator import validator_node
from nodes.report import report_node


def make_router(next_node):
    """Factory for creating routing functions that check for hard errors early.
    
    Args:
        next_node: The default next node if no error or retryable condition.
    
    Returns:
        A router function that:
        - Routes to "report" immediately on hard error (errors list non-empty).
        - Routes to "planner" if soft failure detected (is_valid=False, retries < 3).
        - Routes to next_node otherwise (healthy path continues).
    """
    def router(state):
        it_count = state.get("iteration_count", 0)
        errors = state.get("errors", [])

        # Hard Error Stop: if there's a system error, skip to report immediately.
        if errors:
            print(f"---LOG: System Error detected: {errors[-1]}---")
            return "report"

        # Agentic Loop: retry only for soft failures and bounded attempts.
        if not state.get("is_valid", True) and it_count < 3:
            print(f"---LOG: Insufficient data (Attempt {it_count}), re-planning...---")
            return "planner"

        return next_node

    return router


builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("search", search_node)
builder.add_node("filter", filter_node)
builder.add_node("summarize", summarizer_node)
builder.add_node("validate", validator_node)
builder.add_node("report", report_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "search")
builder.add_conditional_edges(
    "search",
    make_router("filter"),
    {
        "planner": "planner",
        "report": "report",
        "filter": "filter",
    },
)
builder.add_conditional_edges(
    "filter",
    make_router("summarize"),
    {
        "planner": "planner",
        "report": "report",
        "summarize": "summarize",
    },
)
builder.add_edge("summarize", "validate")
builder.add_conditional_edges(
    "validate",
    make_router("report"),
    {
        "planner": "planner",
        "report": "report",
    },
)

builder.add_edge("report", END)

graph = builder.compile()