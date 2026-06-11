import streamlit as st

# 1. Page Config
st.set_page_config(layout="wide")

# 2. Page Router
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# 3. Views
def show_dashboard():
    st.title("TxDOT - Pro-CWII Dashboard")
    st.write("Welcome to the main engine.")
    if st.button("Go to Help Page"):
        st.session_state.page = "Help"
        st.rerun()

def show_help():
    st.title("📘 Help Center")
    st.write("This is your help page.")
    if st.button("Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

# 4. Routing
if st.session_state.page == "Dashboard":
    show_dashboard()
else:
    show_help()
