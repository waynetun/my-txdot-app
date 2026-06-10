import streamlit as st
import os
from pypdf import PdfReader
import google.generativeai as genai

st.set_page_config(layout="wide")

# 1. ROBUST SETUP
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Missing GOOGLE_API_KEY in Streamlit Secrets!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Using gemini-1.5-flash as it is fast and handles context well
model = genai.GenerativeModel('gemini-1.5-flash')

@st.cache_data
def get_pdf_knowledge():
    full_text = ""
    for file in os.listdir("."):
        if file.endswith(".pdf"):
            try:
                reader = PdfReader(file)
                for page in reader.pages:
                    text = page.extract_text()
                    if text: full_text += text + "\n"
            except Exception: continue
    # Safeguard: Send only the first 20,000 characters to avoid InvalidArgument (too long)
    return full_text[:20000] 

# Load the knowledge
try:
    knowledge = get_pdf_knowledge()
except Exception as e:
    st.error(f"Error reading PDFs: {e}")
    knowledge = ""

st.title("Wayne-AI: TxDOT Engineering Engine")

# Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your TxDOT specs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Combined context + question
            full_prompt = f"Context: {knowledge}\n\nQuestion: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"AI Engine Error: {e}")
