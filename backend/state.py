from typing import List, NotRequired, TypedDict

class AgentState(TypedDict):
    query: str
    search_queries: List[str]
    results: List[dict]
    filtered_results: List[dict]
    summaries: List[str]
    final_report: str
    errors: List[str]
    is_valid: NotRequired[bool]
    iteration_count: NotRequired[int]
    critique: NotRequired[str]
