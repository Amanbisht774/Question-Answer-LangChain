import streamlit as st
import langchain
from langchain_community.document_loaders import CSVLoader
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

os.environ["OPENAI_API_KEY"]=
llm=OpenAI(temperature=0.7,max_tokens=500)
embeddings=OpenAIEmbeddings()
st.header("Question and Answer Bot Project")
btn=st.button("create Database")
comment=st.empty()
if btn:
    #Loading the data
    comment.text("Starting Creating the Vector DB...")
    loader=CSVLoader(file_path="E:\Projects 2025\QNA project\codebasics_faqs.csv",source_column="prompt",encoding="Latin-1")
    data=loader.load()
    vector_db=FAISS.from_documents(data,embeddings)
    comment.text("DB created...")
    vector_db.save_local("FAISS")
    comment.text("DB Saved...")

vector_db= FAISS.load_local("FAISS",embeddings, allow_dangerous_deserialization=True)
reteriver=vector_db.as_retriever(search_kwargs={"k":5,"score_threshold":0.7})
Prompt="""You are a customer service agent. With the given chunk of context and input by human, analize the data in the chunk and answer the input accordingly, try to keep the 
answer short and precised. If you dont find the relevant answer in the chunk, Just reply I am now aware of the answer.
context: {context} 
input: {input} """

prompt_template= PromptTemplate(template=Prompt,input_variables=["context,input"])

question=st.text_input("Question:")
question_chain= create_stuff_documents_chain(llm=llm,prompt=prompt_template)
chain=create_retrieval_chain(reteriver,question_chain)

if question:
    comment.text("Starting to fetch the data from the DB")
    result=chain.invoke({"input":question})
    st.write(result["answer"])







