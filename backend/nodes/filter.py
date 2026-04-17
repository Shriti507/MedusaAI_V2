import re

def clean_text(text):
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)   
    text = re.sub(r'<.*?>', '', text)          
    text = re.sub(r'\s+', ' ', text)           
    return text.strip()

def filter_node(state):
    clean_results = []

    for r in state["results"]:
        body = r["body"]

        if "DOI" in body or "PMC" in body:
            continue

        if len(body.strip()) < 100:
            continue

        clean_results.append(r)

    state["filtered_results"] = clean_results
    return state