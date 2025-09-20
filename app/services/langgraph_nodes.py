from typing import List, TypedDict

from app.config import settings
from app.services import get_retrieval_qa, LLaMAWrapper


# Define a state type
class State(TypedDict):
    query: str
    docs: List[str]
    summary: str

def retrieve_documents(state: State) -> State:
    """Retrieve relevant documents for a query."""
    qa = get_retrieval_qa()
    docs = qa.retriever.invoke(state["query"])
    state["docs"] = docs
    return state

def summarize_documents(state: State) -> State:
    llm = LLaMAWrapper(endpoint=settings.LLM_SERVER_URL)

    if state.get("docs"):
        context = "\n".join([d.page_content for d in state["docs"]])
        prompt = f"Summarize the following:\n{context}"
    else:
        prompt = f"Answer the following query:\n{state['query']}"
    summary = llm._call(prompt)
    state["summary"] = summary
    return state


def multiline_step_qa(query: str) -> State:
    state: State = {"query": query, "docs": [], "summary": ""}
    state = retrieve_documents(state)
    state = summarize_documents(state)
    return state
