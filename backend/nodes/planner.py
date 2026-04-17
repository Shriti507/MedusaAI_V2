from llm.engine import generate


def planner_node(state):
    raw_iteration_count = state.get("iteration_count")
    iteration_count = (raw_iteration_count or 0) + 1
    critique = (state.get("critique") or "").strip()
    query = state.get("query") or ""

    if critique:
        prompt = (
            f"Previous attempt was insufficient: {critique}\n"
            f"Refine the search strategy. Generate 3 targeted queries for: {query}\n"
            "STRICT: Focus on factual, technical sources and avoid marketing content."
        )
    else:
        prompt = (
            f"Research Topic: {query}\n"
            "Generate 3 distinct search queries.\n"
            "STRATEGY: Break the topic into (1) Historical Context, (2) Current Implementation, and (3) Future Challenges.\n"
            "STRICT: Ensure queries are optimized for technical documentation and academic results."
        )

    output = generate(prompt)

    queries = [q.strip("- ").strip() for q in output.split("\n") if q.strip()]

    return {
        "search_queries": queries[:3],
        "iteration_count": iteration_count,
        "is_valid": True,
        "critique": "",
    }
