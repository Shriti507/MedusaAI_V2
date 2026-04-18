from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from graph import graph
from exports.exporter import export_pdf, export_markdown
from auth import get_current_user
from supabase_client import supabase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/research")
async def research(data: dict, user_id: str = Depends(get_current_user)):
    state = {
        "query": data["query"],
        "search_queries": [],
        "results": [],
        "filtered_results": [],
        "summaries": [],
        "final_report": "",
        "followups": [],
        "expanded_topics": [],
        "errors": []
    }

    result = graph.invoke(state)

    # Save to Supabase
    supabase.table("conversations").insert({
        "user_id": user_id,
        "query": data["query"],
        "report": result["final_report"]
    }).execute()

    return result

@app.get("/history")
async def get_history(user_id: str = Depends(get_current_user)):
    rows = supabase.table("conversations") \
        .select("*") \
        .eq("user_id", user_id) \
        .order("created_at", desc=True) \
        .execute()

    return rows.data

@app.post("/export/pdf")
async def pdf(data: dict, user_id: str = Depends(get_current_user)):
    return {"file": export_pdf(data["text"])}

@app.post("/export/md")
async def md(data: dict, user_id: str = Depends(get_current_user)):
    return {"file": export_markdown(data["text"])}