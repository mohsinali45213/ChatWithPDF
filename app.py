import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from htmlTempletes import bot_template, user_template, css

GEMINI_API_KEY = None

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=200,
    )
    return text_splitter.split_text(text)


def get_vectorstore(text_chunks):
    docs = [Document(page_content=t) for t in text_chunks]

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=(GEMINI_API_KEY or os.getenv("GEMINI_API_KEY"))
        )

    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = GoogleGenerativeAI(
        model="models/gemini-2.5-flash", 
        google_api_key=(GEMINI_API_KEY or os.getenv("GEMINI_API_KEY"))
    )

    # 🔹 FIXED PROMPT — Now matches expected variable names
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant. Use ONLY the provided document context.",
            ),
            ("human", "Question: {input}\n\nContext: {context}"),
        ]
    )

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    rag_chain = create_retrieval_chain(
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        combine_docs_chain=combine_docs_chain,
    )

    return rag_chain


def handle_user_input(user_question):
    if user_question:
        if st.session_state.conversation is None:
            st.warning("Please upload PDFs and click Process first.")
        else:
            response = st.session_state.conversation.invoke({"input": user_question})
            st.session_state.chat_history.append(("user", user_question))
            st.session_state.chat_history.append(("assistant", response["answer"]))
            for message in st.session_state.chat_history:
                if message[0] == "user":
                    st.write(user_template.replace("{{message}}", message[1]), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace("{{message}}", message[1]), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("Chat with multiple PDFs 📚")
    user_question = st.text_input("Ask a question about your documents...")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        GEMINI_API_KEY = st.text_input("Enter Your Gemini API KEY", type="password")
        pdf_docs = st.file_uploader(
            "Upload PDFs and click on 'Process'", accept_multiple_files=True
        )

        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
        


if __name__ == "__main__":
    main()
