import streamlit as st

# Page Configuration
st.set_page_config(page_title="Pro-CWII Portal", layout="wide")

# Header Section
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("txdot-logo-1000x500.png", width=120)
with col_title:
    st.title("TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)")

# Custom Navigation Bar
nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(6)

with nav1:
    st.image("HomeCopilot.png", width=60)
    st.button("Home")
with nav2:
    st.image("HelpCopilot.png", width=60)
    st.button("Help")
with nav3:
    st.image("SampleCopilot.png", width=60)
    st.button("Sample")
with nav4:
    st.image("FindSimilarProjectCoPilot.png", width=60)
    st.button("Find Similar")
with nav5:
    st.image("IdentifyMissingItemsCopilot.png", width=60)
    st.button("Identify Missing")
with nav6:
    st.image("VerifyMajorQuantitiesCoPilot.png", width=60)
    st.button("Verify Major")

st.divider()

# HELP PAGE CONTENT
st.header("Welcome to the Help Page")
st.write("Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance on using the tool effectively. Whether you're a first-time user or need a quick refresher, you'll find all the information you need here.")

st.subheader("📘 User Manual")
st.write("Our comprehensive user manual contains detailed information about:")
st.markdown("""
* Tool features and capabilities
* Step-by-step usage instructions
* Best practices for data preparation
* Understanding and interpreting results
* Troubleshooting common issues
""")

st.subheader("🚀 Quick Start Guide")
st.markdown("""
**Step 1: Prepare Your Data**
* Download the sample template to understand the required format.
* Ensure your Excel file contains these columns: **ItemCode** (8-digit TxDOT item code), **Quantity** (numeric value), **UnitPrice** (numeric value).
* Save your file in standard Excel format (.xlsx).

**Step 2: Choose Your Analysis**
* Find Similar Projects
* Identify Missing Work Items
* Verify Quantities for Major Pay Items

**Step 3: Get Results**
* Upload your prepared Excel file.
* Review the analysis results.
* Download the detailed report or receive results via email.
""")

st.subheader("🔧 Common Issues and Solutions")
st.markdown("""
| Category | Problem | Solution |
| :--- | :--- | :--- |
| File Upload | "Invalid file format" | Ensure file is .xlsx (not .xls or Strict Open XML) |
| File Upload | "Incorrect column format" | Verify columns: ItemCode, Quantity, UnitPrice |
| File Upload | "Empty file" | Check that your file contains data |
| Analysis | No similar projects found | Try adjusting district or project type filters |
| Analysis | Unexpected results | Verify item codes match TxDOT's 2014 specs |
| Email | Results not received | Check spam folder and verify email address |
""")

st.subheader("💡 Best Practices")
st.write("**Data Preparation:** Use the latest version of Excel, remove formatting/formulas, and ensure item codes/quantities are numeric.")
st.write("**Analysis Tips:** Start with a broad search, prioritize high-probability missing items, and review similar project patterns.")
st.write("**Getting Results:** Include complete project info, use accurate item codes, and review the sample file.")

st.subheader("📞 Need More Help?")
st.write("If you're still experiencing issues or have questions not covered here, review the user manual, check the sample file for formatting, or email us at [txdottamu@gmail.com](mailto:txdottamu@gmail.com).")

st.info("Thank you for using Pro-CWII! We're here to help you succeed with your TxDOT projects.")
