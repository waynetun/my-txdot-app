import streamlit as st

st.set_page_config(layout="wide")

st.title("📘 Pro-CWII Help Center")
st.write("Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance on using the tool effectively.")

with st.expander("📘 User Manual"):
    st.write("Our comprehensive user manual contains detailed information about...")

with st.expander("🚀 Quick Start Guide"):
    st.markdown("""
    **Step 1: Prepare Your Data**
    - Ensure columns: ItemCode, Quantity, UnitPrice.
    - Save as .xlsx format.
    """)

with st.expander("🔧 Common Issues and Solutions"):
    st.error("Invalid file format: Ensure it is .xlsx (not .xls or Strict Open XML).")

with st.expander("💡 Best Practices"):
    st.write("Use the latest version of Excel and remove any formatting or formulas.")

st.divider()
st.subheader("📞 Need More Help?")
st.write("Email us at: **txdottamu@gmail.com**")
