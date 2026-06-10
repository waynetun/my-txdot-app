import streamlit as st
import os
from pypdf import PdfReader
import google.generativeai as genai

# 1. PAGE SETUP
st.set_page_config(layout="wide")
st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")

# 2. SETUP: Securely connect to Google Gemini
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # gemini-1.5-flash is currently a highly stable and supported model
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Please set your GOOGLE_API_KEY in the Streamlit Cloud Secrets settings.")
    st.stop()

# 3. DATA: Robust Reading Engine (Reads ALL PDFs in directory)
@st.cache_data
def get_pdf_knowledge():
    full_text = ""
    # Scans the current folder for any PDF files
    for file in os.listdir("."):
        if file.lower().endswith(".pdf"):
            try:
                reader = PdfReader(file)
                file_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        file_text += text + "\n"
                # Label content from each file so the AI knows where info comes from
                full_text += f"--- Content from {file} ---\n" + file_text + "\n\n"
            except Exception:
                continue
    # Combine content and limit size to ensure performance
    return full_text[:40000] 

# Load the consolidated knowledge base
knowledge = get_pdf_knowledge()

# 4. CHAT INTERFACE
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt area
if prompt := st.chat_input("Ask Wayne-AI about your TxDOT specs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing all uploaded TxDOT documents..."):
            try:
                full_prompt = f"Use this collective TxDOT data to answer the engineer:\n{knowledge}\n\nQuestion: {prompt}"
                response = model.generate_content(full_prompt)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error communicating with AI: {e}")
