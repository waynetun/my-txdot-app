import streamlit as st
import base64
import os

# 1. Page Configuration
st.set_page_config(layout="wide")

# 2. State Initialization
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# --- HELP PAGE FUNCTION ---
def show_help_page():
    left, container, right = st.columns([0.5, 5, 0.5])
    with container:
        st.title("📘 Pro-CWII Help Center")
        st.write("Welcome to the Pro-CWII Help Center. Find guidance below.")
        
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("""
            **Step 1: Prepare Your Data**
            - Ensure your Excel file contains columns: `ItemCode`, `Quantity`, `UnitPrice`.
            - Save in `.xlsx` format.
            
            **Step 2: Choose Your Analysis**
            - Select: Similar Projects, Missing Items, or Verify Quantities.
            
            **Step 3: Get Results**
            - Upload, review results, and download your report.
            """)
            
        with st.expander("🔧 Common Issues & Solutions"):
            st.error("Invalid Format: Use .xlsx files only.")
            st.warning("Analysis: Try adjusting your filters if no projects are found.")
            
        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "Dashboard"
            st.rerun()

# --- DASHBOARD FUNCTION ---
def show_dashboard():
    # ... [YOUR EXISTING DASHBOARD LOGIC GOES HERE] ...
    # IMPORTANT: Locate your 'Help' icon and wrap it in a button:
    if st.button("Help"):
        st.session_state.current_page = "Help"
        st.rerun()
    st.write("Welcome to the Pro-CWII Dashboard.")

# --- ROUTER ---
if st.session_state.current_page == "Dashboard":
    show_dashboard()
elif st.session_state.current_page == "Help":
    show_help_page()

# --- GLOBAL CSS ---
st.markdown("""
<style>
.block-container { padding-top: 2rem !important; }
/* ... [KEEP YOUR EXISTING CSS HERE] ... */
</style>
""", unsafe_allow_html=True)
