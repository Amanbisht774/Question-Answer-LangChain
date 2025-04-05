# 🧠 Question and Answer Bot Project

This project is a simple **AI-powered Q&A chatbot** built with **Streamlit** and **LangChain**. It reads FAQs from a CSV file, generates a vector database using **FAISS**, and leverages **OpenAI’s GPT** to answer questions based on relevant data chunks.

---

## 🔧 Features

- ✅ Interactive Streamlit interface for question answering  
- 📂 Loads CSV data using LangChain's `CSV Loader`  
- 🧠 Uses OpenAI Embeddings for semantic understanding  
- ⚡ Creates a FAISS vector database for fast similarity search  
- 🔄 Retrieves top 5 context-relevant documents  
- 💬 Provides context-aware answers using OpenAI LLM  
- 💾 Saves and loads the vector DB locally  

---

## 🚀 How It Works

1. Click the **"Create Database"** button to load data and generate the FAISS vector store.
2. Ask your question in the input box.
3. The app retrieves the top 5 relevant chunks based on similarity.
4. OpenAI LLM generates a short and precise answer from the context.




---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/) – Web App UI
- [LangChain](https://www.langchain.com/) – LLM Framework
- [OpenAI API](https://platform.openai.com/) – Embeddings + LLM
- [FAISS](https://github.com/facebookresearch/faiss) – Vector similarity search
- CSV – Source of FAQ data

---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/qna-bot.git
   cd qna-bot

