from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os

CHROMA_PERSIST_DIR = "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
add_documents = not os.path.exists(CHROMA_PERSIST_DIR)


embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device': 'cpu'}
    )

if add_documents:
    loader = TextLoader("speech.txt")
    documents = loader.load()

    print("Splitting document into chunks...")
    text_splitter = CharacterTextSplitter(
        chunk_size=300,  
        chunk_overlap=50,
        separator="\n"
    )
    docs = text_splitter.split_documents(documents)

    # Create the Embeddings object
    print(f"Initializing HuggingFace Embeddings with model: {EMBEDDING_MODEL}...")
    

    # Store the embeddings in a local vector store (ChromaDB) 
    print(f"Creating and persisting ChromaDB at {CHROMA_PERSIST_DIR}...")

    # If the directory exists, it will load the existing database.
    # If it doesn't, it will create a new one.
    vectordb = Chroma.from_documents(
        documents=docs, 
        embedding=embeddings, 
        persist_directory=CHROMA_PERSIST_DIR
    )

    # Save the index to disk
    vectordb.persist() 
    print(f"ChromaDB creation complete. Total chunks indexed: {len(docs)}")
else:

    vectordb = Chroma(
        persist_directory=CHROMA_PERSIST_DIR,
        embedding_function=embeddings
    )


retriever = vectordb.as_retriever()


if __name__ == "__main__":

    while True:
        question = input('Enter query(type "e" to exit): ')

        if question.lower() in ['q', 'e', 'quit', 'exit']:
            break

        result = retriever.invoke(question)

        print(result, '\n', len(result))