import streamlit as st

st.set_page_config(page_title="Pro-CWII Help Center", layout="wide")

st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")
st.header("Welcome to the Help Page")
st.write("Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance on using the tool effectively. Whether you're a first-time user or need a quick refresher, you'll find all the information you need here.")

# User Manual
st.subheader("📘 User Manual")
st.write("Our comprehensive user manual contains detailed information about:")
st.markdown("""
* Tool features and capabilities
* Step-by-step usage instructions
* Best practices for data preparation
* Understanding and interpreting results
* Troubleshooting common issues
""")

# Quick Start
st.subheader("🚀 Quick Start Guide")
st.write("**Step 1: Prepare Your Data**")
st.markdown("""
* Download the sample template to understand the required format
* Ensure your Excel file contains these columns: **ItemCode** (8-digit), **Quantity** (numeric), **UnitPrice** (numeric)
* Save your file in standard Excel format (.xlsx)
""")
st.write("**Step 2: Choose Your Analysis**")
st.write("Find Similar Projects, Identify Missing Work Items, or Verify Quantities for Major Pay Items.")
st.write("**Step 3: Get Results**")
st.write("Upload your prepared Excel file, review the results, and download your detailed report.")

# Common Issues
st.subheader("🔧 Common Issues and Solutions")
st.markdown("""
| Category | Problem | Solution |
| :--- | :--- | :--- |
| File Upload | "Invalid file format" | Ensure file is .xlsx (not .xls or Strict Open XML) |
| File Upload | "Incorrect column format" | Verify columns: ItemCode, Quantity, UnitPrice |
| File Upload | "Empty file" | Check that your file contains data |
| Analysis | No similar projects found | Try adjusting the district or project type filters |
| Analysis | Unexpected results | Verify item codes match TxDOT's 2014 specs |
| Email | Results not received | Check spam folder and verify email address |
""")

# Best Practices
st.subheader("💡 Best Practices")
st.write("**Data Preparation:** Use latest Excel, remove formatting/formulas, ensure numeric values.")
st.write("**Analysis Tips:** Start with broad searches, prioritize high-probability missing items, and review similar project patterns.")
st.write("**Getting Best Results:** Include complete project info, use accurate item codes, and review the sample file.")

# Contact
st.divider()
st.subheader("📞 Need More Help?")
st.write("If you're still experiencing issues or have questions not covered here:")
st.write("1. Review the comprehensive user manual")
st.write("2. Check the sample file for proper formatting")
st.write("3. Email us at [txdottamu@gmail.com](mailto:txdottamu@gmail.com)")

st.success("Thank you for using Pro-CWII! We're here to help you succeed with your TxDOT projects.")
