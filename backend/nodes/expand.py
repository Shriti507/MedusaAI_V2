from llm.engine import generate

def expand_node(state):
    prompt = f"Expand into 5 related topics:\n{state['query']}"
    output = generate(prompt)

    state["expanded_topics"] = [t.strip() for t in output.split("\n") if t.strip()][:5]
    return state