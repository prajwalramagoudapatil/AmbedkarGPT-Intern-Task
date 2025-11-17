from langchain_ollama.llms import OllamaLLM
# Use the main 'langchain' package namespace for RetrievalQA
# from langchain.chains import RetrievalQA

# from langchain_classic.chains import RetrievalQA
# from langchain_community.chains import RetrievalQA
# create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from vectordb import retriever


print("Raama")


llm = OllamaLLM(model="mistral")

# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever,
#     return_source_documents=True
# )

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert Q&A system. Answer the user's question ONLY based on the following context."
     "Context: {context}"
    ),
    ("human", "{input}"),
])

document_chain = create_stuff_documents_chain(
    llm, 
    prompt
)

qa_chain = create_retrieval_chain(
    retriever, 
    document_chain
)

print("AmbedkarGPT — Ask any question (type 'exit' to quit):")

while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = qa_chain.invoke({"input": query})

    print("\nAnswer:", result["result"])
    print("\nRelated lines from speech:", result['source_documents'])
    print("-" * 50)

