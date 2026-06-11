import streamlit as st

st.set_page_config(layout="wide")

st.title("TxDOT - Proactive Construction Work Item Identifier")

# Navigation buttons
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.page_link("pages/1_Help.py", label="Help", icon="ℹ️")
with col2: st.page_link("pages/2_Sample_Data.py", label="Sample Data", icon="📊")
# Add the rest of your page links here...
