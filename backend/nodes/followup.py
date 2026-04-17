from llm.engine import generate

def followup_node(state):
    content = "\n".join(state["summaries"])

    prompt = f"Generate 3 follow-up questions:\n{content}"
    output = generate(prompt)

    state["followups"] = [q.strip() for q in output.split("\n") if q.strip()][:3]
    return state