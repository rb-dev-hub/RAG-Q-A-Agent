import streamlit as st
from src.chunking import chunk_text
from src.ingestion import extract_text_from_pdf
from src.context import get_context
from src.llm import ask_ai

# --- Streamlit UI ---
st.title("RAG Q&A Demo 📄🤖")
st.write("Upload a PDF and ask a question about it.")

# File upload
pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

# User question
user_question = st.text_input("Enter your question:")

if pdf_file and user_question:
    # 1. Extract text
    extracted_text_from_file = extract_text_from_pdf(pdf_file)

    # 2. Chunk text
    chunks_from_file = chunk_text(extracted_text_from_file, 5)

    # 3. Get context string
    context = get_context(user_question, chunks_from_file)

    # 4. Call GPT with context
    output = ask_ai(user_question, context)

    # 5. Show answer
    st.subheader("Answer:")
    st.write(output)
