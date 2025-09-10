from langgraph import Node

from app.services import get_retrieval_qa


class RetrieveNode(Node):
    def run(self, input_text: str):
        qa = get_retrieval_qa()
        docs = qa.retriever.get_relevant_documents(input_text)
        return docs


class SummerizeNode(Node):
    def run(self, docs):
        context = "\n".join([d.page_content for d in docs])
        qa = get_retrieval_qa()
        summary = qa.llm(f"Summarize the following:\n {context}")
        return summary


class MultilineStepQA(Node):
    def run(self, query):
        docs = RetrieveNode().run(query)
        summary = SummerizeNode().run(docs)
        return summary
