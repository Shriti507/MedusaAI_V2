from llm.engine import generate

def summarize_node(state):
    summaries = []

    for doc in state["filtered_results"]:
        text = doc.get("body", "")[:500]
        prompt = f"Summarize in 3 bullet points:\n{text}"
        summaries.append(generate(prompt))

    state["summaries"] = summaries
    return state