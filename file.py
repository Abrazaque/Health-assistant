from langchain.prompts import PromptTemplate
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
import streamlit as st
from pathlib import Path
import os
import pickle 

KEY = os.environ.get("GOOGL_API_KEY")
llm=
file_path = Path(r"D:\Data science\Data sample\Disease symptoms\symptom_Description.csv")
loader = CSVLoader(file_path=file_path, encoding='utf-8')
data = loader.load()

embeddings = OpenAIEmbeddings()

vectdb = FAISS.from_documents(documents=data, embedding=embeddings)
retriever = vectdb.as_retriever()

prompt_template = """
given the following context and a question, generate an answer based on this context 
in the answer try to provide as much text as possible from "response" section in the source documents 
if query is related to symptoms, causes, treatment of diseases, health related issues, food nutrition related etc. you have to answer it in your own words if the answer is not found in the context.
If the answer is not found in the context, kindly provide answer by your own words if the question is medical-related field. If it's not, state "I'm sorry, I can't provide information related to your query."
Answer the every query that is related to health, food, nutrition, diseases, symptoms, causes, treatment, etc.
Covid-19 is a new disease, caused by a novel (or new) coronavirus that has not previously been seen in humans. Because it is a new virus, scientists are learning more each day. Although most people who have COVID-19 have mild symptoms, COVID-19 can also cause severe illness and even death. Some groups, including older adults and people who have certain underlying medical conditions, are at increased risk of severe illness.
CONTEXT:{context}
QUESTION:{question}
"""

PROMPT = PromptTemplate(
    template=prompt_template, 
    input_variables=['context', 'question']
)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=retriever,
    input_key='query',
    chain_type_kwargs={'prompt': PROMPT}
)

st.title("Health Assistant 💊🩺")
question = st.text_input("Question: ")
if question:
    try:
        response = chain(question)
        
        st.header('Response Structure')
        st.write(response)
        
        # Display only the answer
        # st.header('Answer')
        # answer = response.get('Answer', 'No answer found.')
        # st.write(answer)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

