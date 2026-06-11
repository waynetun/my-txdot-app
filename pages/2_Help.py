import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

# Initialize State
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --- REUSABLE NAVIGATION ---
def render_navigation():
    # Use your base64 logic here to display the icons
    # Example: col1, col2, col3, col4, col5, col6 = st.columns(6)
    # col1.image("HomeCopilot.png") ... etc
    st.markdown("---") # Visual separator

# --- HELP PAGE VIEW ---
def show_help_page():
    left, container, right = st.columns([0.5, 5, 0.5])
    with container:
        render_navigation()
        st.title("📘 Pro-CWII Help Center")
        st.write("Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance...")

        with st.expander("📘 User Manual"):
            st.write("Our comprehensive user manual contains detailed information about...")
        
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("""
            **Step 1: Prepare Your Data**
            - Download the sample template.
            - Ensure columns: `ItemCode`, `Quantity`, `UnitPrice`.
            - Save as `.xlsx`.
            """)
            
        with st.expander("🔧 Common Issues & Solutions"):
            st.error("Invalid file format: Ensure it is .xlsx (not .xls or Strict Open XML).")
            st.warning("No similar projects: Try adjusting your filters.")
            
        with st.expander("💡 Best Practices"):
            st.write("Use the latest version of Excel and remove formulas.")
            
        st.divider()
        st.subheader("📞 Need More Help?")
        st.write("Email us at: **txdottamu@gmail.com**")
        
        if st.button("← Back to Dashboard"):
            st.session_state.page = "Dashboard"
            st.rerun()

# --- DASHBOARD VIEW ---
def show_dashboard():
    # Keep your existing logic here
    st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")
    render_navigation()
    if st.button("Go to Help"):
        st.session_state.page = "Help"
        st.rerun()

# --- ROUTER ---
if st.session_state.page == "Dashboard":
    show_dashboard()
else:
    show_help_page()

# --- GLOBAL CSS (FLUSH LEFT) ---
st.markdown("""
<style>
.block-container { padding-top: 2rem !important; }
</style>
""", unsafe_allow_html=True)
