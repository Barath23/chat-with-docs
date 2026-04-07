from huggingface_hub import InferenceClient
from langchain_core.runnables import RunnableLambda
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

PROMPT_TEMPLATE = """
Use ONLY the context below to answer the question.
If the answer isn't in the context, say "I don't know based on the documents."

Context:
{context}

Question: {question}

Answer:
"""

def build_qa_chain(vectorstore):

    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

    def hf_llm(prompt):
        if hasattr(prompt, "to_string"):
            prompt = prompt.to_string()
        else:
            prompt = str(prompt)

        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.2
        )

        return response.choices[0].message.content

    # ✅ ONLY CHANGE HERE
    llm = RunnableLambda(lambda x, **kwargs: hf_llm(x))

    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain


def ask(qa_chain, question: str):
    result = qa_chain.invoke({"query": question})
    answer = result["result"]
    sources = set(
        doc.metadata.get("source", "Unknown")
        for doc in result["source_documents"]
    )
    return answer, sources