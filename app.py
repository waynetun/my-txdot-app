import streamlit as st

st.set_page_config(layout="wide")

# Title
st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")

# Buttons row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Home")

with col2:
    st.button("Help")

with col3:
    st.button("Sample")

with col4:
    st.button("Identify Missing Items")

with col5:
    st.button("Verify Major Quantities")

# Welcome section
st.markdown("## Welcome")

st.write("""
This is your custom TxDOT app.
You will build your functions here.
""")
``
