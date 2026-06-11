import streamlit as st

# 1. Page Setup
st.set_page_config(layout="wide")

# 2. Main Container (Matching your Dashboard's width)
left, container, right = st.columns([0.5, 5, 0.5])

with container:
    st.title("📘 Pro-CWII Help Center")
    st.markdown("""
    Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance on using the tool effectively. Whether you're a first-time user or need a quick refresher, you'll find all the information you need here.
    """)

    st.header("📘 User Manual")
    st.markdown("""
    Our comprehensive user manual contains detailed information about:
    - Tool features and capabilities
    - Step-by-step usage instructions
    - Best practices for data preparation
    - Understanding and interpreting results
    - Troubleshooting common issues
    """)

    st.header("🚀 Quick Start Guide")
    st.subheader("Step 1: Prepare Your Data")
    st.markdown("""
    - Download the sample template to understand the required format.
    - Ensure your Excel file contains these columns: `ItemCode` (8-digit TxDOT item code), `Quantity` (numeric value), `UnitPrice` (numeric value).
    - Save your file in standard Excel format aka `.xlsx` format (not Strict Open XML).
    """)
    st.subheader("Step 2: Choose Your Analysis")
    st.markdown("""
    - Find Similar Projects
    - Identify Missing Work Items
    - Verify Quantities for Major Pay Items
    """)
    st.subheader("Step 3: Get Results")
    st.markdown("""
    - Upload your prepared Excel file.
    - Review the analysis results.
    - Download the detailed report.
    - Optionally, receive results via email.
    """)

    st.header("🔧 Common Issues and Solutions")
    st.subheader("File Upload Issues")
    st.markdown("""
    - **Problem:** "Invalid file format" error. **Solution:** Ensure your file is saved as `.xlsx` (not `.xls` or Strict Open XML).
    - **Problem:** "Incorrect column format" error. **Solution:** Verify your columns are named exactly: `ItemCode`, `Quantity`, `UnitPrice`.
    - **Problem:** "Empty file" error. **Solution:** Check that your file contains data and is not corrupted.
    """)
    st.subheader("Analysis Issues")
    st.markdown("""
    - **Problem:** No similar projects found. **Solution:** Try adjusting the district or project type filters.
    - **Problem:** Unexpected results. **Solution:** Verify your item codes match TxDOT's 2014 specifications.
    """)
    st.subheader("Email Issues")
    st.markdown("""
    - **Problem:** Results email not received. **Solution:** Check your spam folder and verify the email address.
    """)

    st.header("💡 Best Practices")
    st.subheader("Data Preparation")
    st.markdown("""
    - Use the latest version of Excel.
    - Remove any formatting or formulas from your data.
    - Ensure all item codes are correct.
    - Verify quantities and unit prices are numeric values.
    """)
    st.subheader("Analysis Tips")
    st.markdown("""
    - When searching for similar projects, start with a broad search, then narrow down using filters.
    - When identifying missing work items, prioritize work items with a high probability of being missed.
    - Review similar projects to understand common patterns.
    - Use the email feature or the download button to save results for future reference.
    """)

    st.header("📞 Need More Help?")
    st.markdown("""
    If you're still experiencing issues or have questions not covered here:
    - Review the comprehensive user manual.
    - Check the sample file for proper formatting.
    - **Email us at: txdottamu@gmail.com**
    """)
