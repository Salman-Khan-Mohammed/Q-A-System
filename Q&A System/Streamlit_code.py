import streamlit as st
from Main_code import get_qa_chain, create_vector_db

# Set page configuration
st.set_page_config(page_title="Codebasics Q&A", page_icon="🌱", layout="centered")

# Page Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Codebasics Q&A 🌱</h1>", unsafe_allow_html=True)

# Introduction Text
st.markdown("""
<div style='text-align: center; color: grey;'>
    Welcome to the Codebasics Q&A system! Ask any question related to our knowledge base, and we will provide you with the best answer.
</div>
""", unsafe_allow_html=True)

# Button to Create Knowledgebase
st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Build Your Knowledgebase</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Click the button below to create or update the knowledgebase.</div>", unsafe_allow_html=True)

btn = st.button("Create Knowledgebase", key="create_kb")
if btn:
    with st.spinner("Creating knowledgebase..."):
        create_vector_db()
    st.success("Knowledgebase created successfully!")

st.markdown("---")

# User Question Input
st.markdown("<h2 style='text-align: center;'>Ask a Question</h2>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Type your question below and get an instant answer.</div>", unsafe_allow_html=True)

question = st.text_input("", placeholder="Type your question here...")

# Display Answer
if question:
    with st.spinner("Searching for the answer..."):
        chain = get_qa_chain()
        response = chain(question)
        answer = response["result"]

    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Answer</h3>", unsafe_allow_html=True)

    if answer.strip().lower() == "i don't know.":
        st.markdown("<p style='text-align: center; color: grey;'>Sorry, I don't have an answer to that question.</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='text-align: center; color: white;'>{answer}</p>", unsafe_allow_html=True)
