import streamlit as st

st.set_page_config(layout="wide")

# ---------- OUTER CENTER (creates margins) ----------
left, container, right = st.columns([1, 3, 1])

with container:

    # ---------- INNER FIXED WIDTH (THIS IS KEY) ----------
    inner_left, inner_center, inner_right = st.columns([1, 8, 1])

    with inner_center:

        # ---------- HEADER ----------
        col1, col2 = st.columns([1, 4])

        with col1:
            st.image("txdot-logo-1000x500.png", width=200)

        with col2:
            st.markdown("""
            <div style="display:flex; align-items:center; height:100%;">
                <h2 style="margin:0;">
                TxDOT - Proactive Construction Work Item Identifier (Pro‑CWII)
                </h2>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- ICON ROW ----------
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("SampleCopilot.png", width=180)

        with col2:
            st.image("HelpCoPilot.png", width=180)

        with col3:
            st.image("FindSimilarProjectCoPilot.png", width=180)

        with col4:
            st.image("IdentifyMissingItemsCopilot.png", width=180)

        with col5:
            st.image("VerifyMajorQuantitiesCoPilot.png", width=180)

        st.markdown("###")

        # ---------- WELCOME ----------
        st.markdown("## Welcome")
        st.markdown("---")

        st.write("""
The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects. By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
        """)

        st.markdown("""
1. Identify similar past projects for better decision-making  
2. Predict potential missing work items before they become costly change orders  
3. Verify major quantities to ensure accurate project planning and resource allocation  
        """)

        st.write("""
This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications and work item codes.
        """)

        # ---------- HOW TO USE ----------
        st.markdown("## How to Use This Tool")
        st.markdown("---")

        st.write("Follow these simple steps to get started:")

        st.markdown("### Prepare Your Data")
        st.markdown("""
- Download our sample template to see the required format  
- Ensure your project data includes item codes, quantities, and unit prices  
- Save your file in Excel (.xlsx) format  
        """)

        st.markdown("### Choose Your Analysis")
        st.markdown("""
- Find Similar Projects  
- Identify Missing Work Items  
- Verify Quantities for Major Pay Items  
        """)

        st.markdown("### Get Results")
        st.markdown("""
- Upload your prepared Excel file  
- Review the analysis results  
- Download the detailed report  
- Optionally, receive results via email  
        """)

        st.markdown("### Need Help?")
        st.markdown("""
- Visit our Help page for detailed instructions  
- Download the comprehensive user manual  
- Review common troubleshooting tips  
        """)

        st.write("""
For the best results, ensure your input data follows the sample format exactly.
        """)
