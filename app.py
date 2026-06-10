import streamlit as st
import os
from pypdf import PdfReader
from openai import OpenAI

st.set_page_config(layout="wide")

# This function scans your GitHub files for PDFs and extracts their text
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

# Load the data
knowledge = get_pdf_knowledge()

st.title("Wayne-AI: TxDOT Engineering Engine")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about specs, guides, or project items..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # The AI is now 'fed' the PDF data inside this prompt
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are Wayne-AI. Answer engineers based ONLY on this data: {knowledge}"},
                {"role": "user", "content": prompt}
            ]
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
        st.session_state.messages.append({"role": "assistant", "content": msg})
