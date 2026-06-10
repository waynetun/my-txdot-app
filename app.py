import streamlit as st
import os
from pypdf import PdfReader
import google.generativeai as genai

# 1. SETUP: Configure the Free Google Brain
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. DATA: PDF Reading Engine (The "Brain")
@st.cache_data
def get_pdf_knowledge():
    full_text = ""
    for file in os.listdir("."):
        if file.endswith(".pdf"):
            try:
                reader = PdfReader(file)
                for page in reader.pages:
                    full_text += page.extract_text() + "\n"
            except: continue
    return full_text

knowledge = get_pdf_knowledge()

# 3. LAYOUT: Your Custom TxDOT Dashboard
st.set_page_config(layout="wide")

# ... (Keep all your existing CSS and Custom HTML blocks here) ...

# 4. INTEGRATION: When the user asks a question
if "messages" not in st.session_state:
    st.session_state.messages = []

# When the user interacts with your TxDOT interface, send the data to the brain
if user_input := st.chat_input("Ask about your TxDOT specs..."):
    # Send user_input + knowledge to the Gemini AI
    prompt = f"Use this TxDOT data: {knowledge}\n\nUser Question: {user_input}"
    response = model.generate_content(prompt)
    
    # Display result
    st.markdown(response.text)
