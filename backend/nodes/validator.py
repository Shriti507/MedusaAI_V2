def validator_node(state):
    if len(state["summaries"]) < 2:
        state["errors"].append("Insufficient data")

    return state