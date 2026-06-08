import streamlit as st

st.set_page_config(layout="wide")

# ---------- CENTER LAYOUT ----------
left, center, right = st.columns([1, 2, 1])

with center:

    # ---------- HEADER ----------
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("txdot-logo-1000x500.png", width=180)

    with col2:
        st.markdown("""
        <h2 style="margin-top:20px;">
        TxDOT - Proactive Construction Work Item Identifier (Pro‑CWII)
        </h2>
        """, unsafe_allow_html=True)

    st.markdown("###")

    # ---------- ICON ROW ----------
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image("SampleCopilot.png", width=110)

    with col2:
        st.image("HelpCoPilot.png", width=110)

    with col3:
        st.image("FindSimilarProjectCoPilot.png", width=110)

    with col4:
        st.image("IdentifyMissingItemsCopilot.png", width=110)

    with col5:
        st.image("VerifyMajorQuantitiesCoPilot.png", width=110)

    st.markdown("###")

    # ---------- WELCOME ----------
    st.markdown("## Welcome")
    st.markdown("---")

    st.write("""
    The TxDOT Proactive Construction Work Item Identifier (Pro‑CWII) is a decision-support tool developed to assist engineers and project managers in identifying potential missing work items and verifying major quantities in construction and maintenance projects.
    """)

    st.write("""
    Using historical project data and advanced analytics, Pro‑CWII supports improved planning, cost control, and accuracy by enabling users to:
    """)

    st.markdown("""
    1. Identify similar past projects to support decision-making  
    2. Detect potential missing work items before change orders occur  
    3. Verify major quantities to improve estimate reliability  
    """)

    st.write("""
    This tool is designed specifically for Texas Department of Transportation (TxDOT) projects and aligns with TxDOT standard specifications and item codes.
    """)

    # ---------- HOW TO USE ----------
    st.markdown("## How to Use This Tool")
    st.markdown("---")

    st.markdown("### 1. Prepare Your Data")
    st.markdown("""
    - Download the sample template  
    - Include item codes, quantities, and unit prices  
    - Save your file as Excel (.xlsx)  
    """)

    st.markdown("### 2. Select an Analysis Option")
    st.markdown("""
    - Find Similar Projects  
    - Identify Missing Work Items  
    - Verify Major Quantities  
    """)

    st.markdown("### 3. Review Results")
    st.markdown("""
    - Upload your Excel file  
    - Review analysis results  
    - Download detailed reports  
    """)

    st.markdown("### Need Help?")
    st.markdown("""
    - Visit the Help page  
    - Review user documentation  
    - Check troubleshooting guidance  
    """)

    st.write("""
    For best results, ensure your input data follows the required template format.
    """)
