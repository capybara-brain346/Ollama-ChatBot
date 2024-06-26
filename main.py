from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please repond to user queries"),
        ("user", "Question:{question}"),
    ]
)

st.title("Langchain Chatbot")
input_text = st.text_input("Chat here: ")
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if st.text_input:
    st.write(chain.invoke({"question": input_text}))
