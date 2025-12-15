import os
from dotenv import load_dotenv


from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#Design Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

#Design Streamlit Framework
st.title("Langchain Demo with Gemma Model")
input_text = st.text_input("What Question you have in Mind?")

#Design Ollama Model

llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


#To Run   --> streamlit run app.py