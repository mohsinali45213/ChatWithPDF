import streamlit as st
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
load_dotenv()
# LangChain Imports (2025 Standard)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from htmlTempletes import bot_template, user_template, css

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            extract = page.extract_text()
            if extract:
                text += extract
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=1000,
        chunk_overlap=200,
    )
    return text_splitter.split_text(text)

def get_vectorstore(text_chunks, api_key):
    # Convert string chunks to Document objects
    docs = [Document(page_content=t) for t in text_chunks]

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def format_docs(docs):
    """Helper to join retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)

def get_conversation_chain(vectorstore, api_key):
    # 1. Initialize the Chat Model (Switching to ChatGoogleGenerativeAI for Gemini Flash)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )

    # 2. Define the Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    # 3. Define the Prompt
    template = """You are a helpful assistant for analyzing PDF documents.
    Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    
    Context:
    {context}
    
    Question: {input}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 4. Construct the Chain using LCEL (LangChain Expression Language)
    # The pipe '|' connects components:
    # Input -> (Retriever + Passthrough) -> Prompt -> LLM -> OutputParser
    rag_chain = (
        {
            "context": retriever | format_docs,  # Pipe retrieved docs through format function
            "input": RunnablePassthrough()       # Pass user question through unchanged
        }
        | prompt
        | llm
        | StrOutputParser() # Converts message object to pure string
    )

    return rag_chain

def handle_user_input(user_question):
    if st.session_state.conversation is None:
        st.warning("Please upload PDFs and click Process first.")
        return

    # Invoke the chain with the user question
    # Note: LCEL allows us to pass the string directly because of RunnablePassthrough
    response_text = st.session_state.conversation.invoke(user_question)

    # Update history
    st.session_state.chat_history.append(("user", user_question))
    st.session_state.chat_history.append(("assistant", response_text))

    # Render Chat
    # We iterate in reverse or standard order depending on preference. 
    # Here we stick to your standard order but use a container for better UX.
    chat_container = st.container()
    with chat_container:
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write(user_template.replace("{{message}}", message), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{message}}", message), unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("Chat with multiple PDFs 📚 (LCEL 2025 Edition)")
    
    # User Input
    user_question = st.text_input("Ask a question about your documents...")
    if user_question:
        handle_user_input(user_question)

    # Sidebar
    with st.sidebar:
        st.subheader("Configuration")
        
        api_key = st.text_input("Enter your Google Gemini API Key", type="password")
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload PDFs here and click on 'Process'", accept_multiple_files=True
        )

        if st.button("Process"):
            if not api_key: 
                api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                st.error("Please enter your API Key first.")
                return
            elif not pdf_docs:
                st.error("Please upload at least one PDF.")
            else:
                with st.spinner("Processing..."):
                    # 1. Get PDF Text
                    raw_text = get_pdf_text(pdf_docs)
                    
                    # 2. Split Text
                    text_chunks = get_text_chunks(raw_text)
                    
                    # 3. Create Vector Store (Pass API Key)
                    vectorstore = get_vectorstore(text_chunks, api_key)
                    
                    # 4. Create Conversation Chain (Pass API Key)
                    st.session_state.conversation = get_conversation_chain(vectorstore, api_key)
                    
                    st.success("Done! You can now ask questions.")
        if st.button("Clear Conversation"):
            st.session_state.chat_history = []
            st.success("Conversation cleared.")
if __name__ == "__main__":
    main()