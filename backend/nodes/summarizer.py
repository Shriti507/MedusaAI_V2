from llm.engine import generate

def summarizer_node(state):
    summaries = []

    for doc in state["filtered_results"]:
        content = doc["body"]

        content = content.replace("\n", " ")
        content = content.replace("[", "").replace("]", "")
        content = content.replace("(", "").replace(")", "")

        content = content[:1000]

        prompt = f"""
        Summarize the following content in 2-3 clear sentences.
        Ignore links, references, and metadata.

        Content:
        {content}
        """

        summary = generate(prompt)
        summaries.append(summary)

    state["summaries"] = summaries
    return state