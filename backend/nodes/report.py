from llm.engine import generate

def report_node(state):
    content = "\n".join(state["summaries"])

    prompt = f"""
Generate structured report:

Title:
Abstract:
Key Findings:
Sources:
Conclusion:

Content:
{content}
"""

    state["final_report"] = generate(prompt)
    return state