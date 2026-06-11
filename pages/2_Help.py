import streamlit as st
import base64
import os

# 1. Page Configuration
st.set_page_config(layout="wide", page_title="Pro-CWII")

# 2. State Initialization
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# 3. Help Page Content
def show_help_page():
    # Keep the same layout columns as your dashboard
    _, container, _ = st.columns([0.5, 5, 0.5])
    with container:
        st.title("📘 Pro-CWII Help Center")
        
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("1. Prepare Data... 2. Analyze... 3. Get Results.")
        
        with st.expander("🔧 Troubleshooting"):
            st.error("Format error: Use .xlsx only.")

        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "Dashboard"
            st.rerun()

# 4. Main Dashboard (Keep your existing layout code here)
def show_dashboard():
    # --- YOUR EXISTING DASHBOARD CODE ---
    st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")
    
    # Navigation example: 
    if st.button("Help"):
        st.session_state.current_page = "Help"
        st.rerun()

# 5. Routing Logic (The "Brain" of your app)
if st.session_state.current_page == "Dashboard":
    show_dashboard()
elif st.session_state.current_page == "Help":
    show_help_page()

# 6. GLOBAL CSS (CRITICAL: MUST BE FLUSH LEFT)
st.markdown("""
<style>
.block-container { padding-top: 2rem !important; }
.chat-header { background: #0f172a; padding: 20px; border-radius: 12px; color: white; }
</style>
""", unsafe_allow_html=True)
