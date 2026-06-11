def show_help_page():
    st.title("📘 Pro-CWII Help Center")
    st.write("Welcome! This page provides comprehensive guidance on using the tool effectively.")

    # 1. User Manual Section
    with st.expander("📘 User Manual"):
        st.write("""
        Our comprehensive user manual contains detailed information about:
        - Tool features and capabilities
        - Step-by-step usage instructions
        - Best practices for data preparation
        - Understanding and interpreting results
        - Troubleshooting common issues
        """)

    # 2. Quick Start Guide
    with st.expander("🚀 Quick Start Guide"):
        st.subheader("Step 1: Prepare Your Data")
        st.write("- Download the sample template to understand the required format.")
        st.write("- Ensure your Excel file contains: `ItemCode`, `Quantity`, `UnitPrice`.")
        st.write("- Save as standard `.xlsx` format.")
        
        st.subheader("Step 2: Choose Your Analysis")
        st.write("- Find Similar Projects")
        st.write("- Identify Missing Work Items")
        st.write("- Verify Quantities for Major Pay Items")
        
        st.subheader("Step 3: Get Results")
        st.write("- Upload file -> Review results -> Download report.")

    # 3. Troubleshooting
    with st.expander("🔧 Common Issues and Solutions"):
        st.error("File Upload Issues: Ensure you are using .xlsx format and exact column names.")
        st.warning("Analysis Issues: If no projects are found, try adjusting your district filters.")
        st.info("Email Issues: Check your spam folder if the report doesn't arrive.")

    # 4. Best Practices
    with st.expander("💡 Best Practices"):
        st.write("- Use the latest version of Excel.")
        st.write("- Remove formulas from data before uploading.")
        st.write("- Start with broad searches, then use filters to narrow down.")

    # 5. Contact
    st.divider()
    st.subheader("📞 Need More Help?")
    st.write("If you have questions not covered here, email us at: **txdottamu@gmail.com**")

# Call this function whenever you want to display the help page
# show_help_page()
