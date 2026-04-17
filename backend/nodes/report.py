from llm.engine import generate

def report_node(state):
    summaries = state["summaries"]

    combined = "\n".join(summaries)

    prompt = f"""
    You are an expert research assistant.

    Using the summaries below, write a detailed and well-structured report.

    Summaries:
    {combined}

    Structure the report with clear headings:

    1. Introduction
    2. Key Benefits of AI in Healthcare
    3. Challenges and Limitations
    4. Conclusion

    Write in paragraph form. Do NOT repeat the summaries.
    """

    report = generate(prompt)

    state["final_report"] = report
    return state