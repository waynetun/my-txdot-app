import streamlit as st

st.set_page_config(layout="wide")

# ---------- CREATE CENTER SPACE ----------
left, center, right = st.columns([1, 2, 1])

with center:

    # ---------- HEADER ----------
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("txdot-logo-1000x500.png", width=180)

    with col2:
        st.markdown("""
        <h2>
        TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
        </h2>
        """, unsafe_allow_html=True)

    # ---------- SPACE ----------
    st.markdown("###")

    # ---------- BUTTONS ----------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Home")

    with col2:
        st.button("Help")

    with col3:
        st.button("Sample")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.button("Find Similar Projects")

    with col5:
        st.button("Identify Missing Items")

    with col6:
        st.button("Verify Major Quantities")

    # ---------- SPACE ----------
    st.markdown("###")

    # ---------- CONTENT ----------
    st.markdown("## Welcome")
    st.markdown("---")

    st.write("""
    The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.

    By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
    """)

    st.markdown("""
    1. Identify similar past projects for better decision-making  
    2. Predict potential missing work items before costly change orders  
    3. Verify major quantities for accurate planning  
    """)

    st.write("""
    This tool is specifically designed for Texas Department of Transportation (TxDOT) projects.
    """)

    # ---------- HOW TO USE ----------
    st.markdown("## How to Use This Tool")
    st.markdown("---")

    st.markdown("### Prepare Your Data")
    st.markdown("""
    - Download sample template  
    - Include item codes, quantities, unit prices  
    - Save as .xlsx  
    """)

    st.markdown("### Choose Your Analysis")
    st.markdown("""
    - Find Similar Projects  
    - Identify Missing Items  
    - Verify Quantities  
    """)

    st.markdown("### Get Results")
    st.markdown("""
    - Upload file  
    - Review results  
    - Download report  
    """)

    st.markdown("### Need Help?")
    st.markdown("""
    - Visit Help page  
    - Read user manual  
    - Check troubleshooting tips  
    """)
