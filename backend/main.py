from fastapi import FastAPI
from graph import graph
from exports.exporter import export_pdf, export_markdown

app = FastAPI()

@app.post("/research")
async def research(data: dict):
    state = {
        "query": data["query"],
        "search_queries": [],
        "results": [],
        "filtered_results": [],
        "summaries": [],
        "final_report": "",
        "errors": []
    }

    result = graph.invoke(state)

    return result


@app.post("/export/pdf")
async def export_pdf_api(data: dict):
    file = export_pdf(data["text"])
    return {"file": file}


@app.post("/export/md")
async def export_md_api(data: dict):
    file = export_markdown(data["text"])
    return {"file": file}