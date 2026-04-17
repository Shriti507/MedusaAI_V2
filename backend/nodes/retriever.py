def filter_node(state):
    seen = set()
    filtered = []

    for r in state["results"]:
        url = r.get("href") + r.get("title", "")
        if url and url not in seen:
            filtered.append(r)
            seen.add(url)

    state["filtered_results"] = filtered[:5]
    return state