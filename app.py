import streamlit as st
import os
from pypdf import PdfReader
import google.generativeai as genai

# 1. PAGE SETUP (Keep your existing design settings here)
st.set_page_config(layout="wide")
st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")

# 2. SETUP: Securely connect to Google Gemini
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Please set your GOOGLE_API_KEY in the Streamlit Cloud Secrets settings.")
    st.stop()

# 3. DATA: PDF Reading Engine (The "Brain")
@st.cache_data
def get_pdf_knowledge():
    full_text = ""
    # Scans the current folder for any PDF files
    for file in os.listdir("."):
        if file.endswith(".pdf"):
            try:
                reader = PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text: full_text += text + "\n"
            except Exception: continue
    # Return a snippet to avoid exceeding token limits
    return full_text[:20000] 

# Load the knowledge base once
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
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing TxDOT specs..."):
            try:
                # Combine the PDF knowledge with the user's specific question
                full_prompt = f"Use this TxDOT data: {knowledge}\n\nQuestion: {prompt}"
                response = model.generate_content(full_prompt)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error communicating with AI: {e}")
