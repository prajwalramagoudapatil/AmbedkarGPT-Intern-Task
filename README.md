# AmbedkarGPT-Intern-Task
RAG application using langchain, Ollama, mistral, HaggingFace, 
Here is a **clean, professional, interview-ready `README.md`** specifically tailored for your **AmbedkarGPT-Intern-Task**.
This includes **setup, installation, how to run**, and covers the exact requirements mentioned in the assignment.

You can copy–paste this directly into your repository.

---

# 📄 **README.md**

# **AmbedkarGPT – RAG Q&A System (Intern Assignment)**

A simple **Retrieval-Augmented Generation (RAG)** pipeline built as part of the **AI Intern Hiring Assignment** for Kalpit Pvt Ltd (UK).
The system loads a speech by **Dr. B. R. Ambedkar**, splits it into chunks, creates embeddings, stores them locally using **ChromaDB**, retrieves relevant chunks, and generates answers using **Ollama (Mistral 7B)**.

---

# 🚀 **Tech Stack**

* **Python 3.8+**
* **LangChain** (RAG orchestration)
* **ChromaDB** (local vector store)
* **sentence-transformers/all-MiniLM-L6-v2** (embeddings)
* **Ollama + Mistral 7B** (LLM)
* **CLI-based (Command Line Interface)**

---

# 📁 **Project Structure**

```
AmbedkarGPT-Intern-Task/
│── main.py
│── vectordb.py
│── requirements.txt
│── README.md
│── speech.txt
│── .gitignore
│── venv/ (ignored)
│── chroma_store/ (ignored)
```

---

# ⚙️ **1. Install Dependencies**

## **Create a virtual environment (recommended)**

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## **Install Python packages**

```bash
pip install -r requirements.txt
```

---

# 🤖 **2. Install & Set Up Ollama**

### Download Ollama (Windows/Mac/Linux):

[https://ollama.com/download](https://ollama.com/download)

### Pull the Mistral model:

```bash
ollama pull mistral
```

Ensure Ollama is running before you start the project.

---

# 📄 **3. Add the Speech File**

A file named **speech.txt** is included, containing an excerpt from:

> *Annihilation of Caste* – Dr. B.R. Ambedkar

This text is the only knowledge source used by the Q&A system.

---

# 🧠 **4. How the System Works (RAG Pipeline)**

1. **Load** the speech text
2. **Split** into manageable chunks
3. **Generate embeddings** using HuggingFace
4. **Store vector embeddings** in a local ChromaDB directory
5. **Retrieve relevant chunks** based on the user question
6. **Generate the answer** using Mistral 7B via Ollama
7. **Display final answer** in terminal

---

# ▶️ **5. Run the Application**

Activate virtual environment:

```bash
venv\Scripts\activate       # Windows
source venv/bin/activate   # macOS/Linux
```

Run the script:

```bash
python main.py
```

You will see:

```
AmbedkarGPT — Ask any question (type 'exit' to quit):
```

Example:

```
You: What is the real enemy according to the speech?
Answer: The real enemy is the belief in the shastras.
```

---

# 🧪 **6. Example Questions to Try**

* *What is the real remedy suggested in the speech?*
* *Why can people not get rid of caste, according to the text?*
* *What is the role of social reformers in the problem?*

All answers must come **only from speech.txt**, enforced by the RAG prompt.

---

# 📦 **7. .gitignore Used**

```
venv/
chroma_store/
__pycache__/
*.pyc
```

This ensures unnecessary local files are not pushed to GitHub.

---

# 📝 **8. Notes**

* The system is a **functional prototype** as instructed.
* It uses **create_retrieval_chain()** (modern LangChain approach).
* No external APIs, no cloud services, and no paid models.

---

# 🙌 **9. Credits**

Developed for:
**Kalpit Pvt Ltd — AI Intern Assignment Phase 1**
Based on the excerpt from: **Annihilation of Caste – Dr. B. R. Ambedkar**

---

If you want, I can also produce:

✅ A professional-looking **main.py**
✅ A polished **requirements.txt**
✅ A stronger prompt for correction
Just tell me!
