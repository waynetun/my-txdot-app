import streamlit as st
import base64
import os

# 1. Setup
st.set_page_config(layout="wide")

# 2. Page Controller State
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# 3. Help Page Function
def show_help_page():
    # Maintain your dashboard's column-based layout
    _, container, _ = st.columns([0.5, 5, 0.5])
    with container:
        st.markdown("<h1 style='color: #000000;'>📘 Pro-CWII Help Center</h1>", unsafe_allow_html=True)
        
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("""
            **Step 1: Data Prep** - Use `ItemCode`, `Quantity`, `UnitPrice` in .xlsx.
            **Step 2: Analysis** - Choose your desired tool from the main menu.
            **Step 3: Results** - Upload, review, and download.
            """)
        
        with st.expander("🔧 Common Issues"):
            st.error("Format error: Only .xlsx files allowed.")
            st.warning("Analysis error: Verify your item codes.")
            
        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "Dashboard"
            st.rerun()

# 4. Dashboard Function (Your Existing Logic)
def show_dashboard():
    # (Put all your current dashboard layout code here)
    st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")
    
    # Navigation Buttons Example:
    if st.button("Open Help"):
        st.session_state.current_page = "Help"
        st.rerun()

# 5. Router Logic
if st.session_state.current_page == "Dashboard":
    show_dashboard()
elif st.session_state.current_page == "Help":
    show_help_page()

# 6. Global CSS (Must be flush left to avoid blank page)
st.markdown("""
<style>
.block-container { padding-top: 2rem !important; }
.chat-header { background: #0f172a; padding: 20px; border-radius: 12px; color: white; }
</style>
""", unsafe_allow_html=True)
