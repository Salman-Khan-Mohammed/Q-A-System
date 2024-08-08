import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db
from sentence_transformers import SentenceTransformer


st.title("Codebasics Q&A 🌱")
btn = st.button("Create Knowledgebase")
if btn:
    # create_vector_db()
    pass

question = st.text_input("Question: ")

if question:
    pass
#     chain = get_qa_chain()
#     response = chain(question)

#     st.header("Answer")
#     st.write(response["result"])






