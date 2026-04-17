from llm.engine import generate

def planner_node(state):
    query = state["query"]

    state["search_queries"] = [
        f"{query} benefits",
        f"{query} challenges",
        f"{query} applications"
    ]

    return state