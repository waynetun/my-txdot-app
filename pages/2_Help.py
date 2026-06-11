def show_help_page():
    # We keep the same column structure to ensure the design "feels" identical to your home page
    _, container, _ = st.columns([0.5, 5, 0.5])
    
    with container:
        # Re-using your header style for consistency
        st.markdown("<h1 style='color: #000000;'>📘 Pro-CWII Help Center</h1>", unsafe_allow_html=True)
        st.write("Welcome! This page provides comprehensive guidance on using the tool effectively.")
        
        # User Manual
        with st.expander("📘 User Manual"):
            st.write("Our manual covers feature capabilities, usage instructions, and data preparation best practices.")
            
        # Quick Start
        with st.expander("🚀 Quick Start Guide"):
            st.markdown("""
            **Step 1: Prepare Your Data**
            - Download our sample template.
            - Ensure columns: `ItemCode`, `Quantity`, `UnitPrice`.
            - Save as `.xlsx`.
            
            **Step 2: Choose Your Analysis**
            - Select: Similar Projects, Missing Items, or Verify Quantities.
            
            **Step 3: Get Results**
            - Upload, review, and download your report.
            """)
            
        # Troubleshooting
        with st.expander("🔧 Common Issues & Solutions"):
            st.error("Upload Error: Ensure file is .xlsx format and not 'Strict Open XML'.")
            st.warning("Analysis Error: Try adjusting district/project filters.")
            
        # Contact
        st.divider()
        st.subheader("📞 Need More Help?")
        st.write("Email us at: **txdottamu@gmail.com**")
        
        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "Dashboard"
            st.rerun()
