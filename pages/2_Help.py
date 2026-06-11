import streamlit as st

# Setup page configuration
st.set_page_config(page_title="Help", layout="wide")

# Your header/title
st.title("ℹ️ Help & Documentation")

# Your content
st.write("Welcome to the Pro-CWII Help Center.")
st.write("Here you can find instructions on how to use the dashboard, understand the metrics, and get the most out of our construction identifier tools.")

# Example of how you can add specific help sections
with st.expander("How to upload sample data"):
    st.write("Navigate to the 'Sample Data' page to upload your CSV files.")
