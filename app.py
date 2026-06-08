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
        TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
        </h2>
        """, unsafe_allow_html=True)

    st.markdown("###")

    # ---------- ICON GRID ----------
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image("SampleCopilot.png", width=120)
        st.markdown("<div style='text-align:center;'>Sample</div>", unsafe_allow_html=True)

    with col2:
        st.image("HelpCoPilot.png", width=120)
        st.markdown("<div style='text-align:center;'>Help</div>", unsafe_allow_html=True)

    with col3:
        st.image("FindSimilarProjectCoPilot.png", width=120)
        st.markdown("<div style='text-align:center;'>Find Similar Projects</div>", unsafe_allow_html=True)

    with col4:
        st.image("IdentifyMissingItemsCopilot.png", width=120)
        st.markdown("<div style='text-align:center;'>Identify Missing Items</div>", unsafe_allow_html=True)

    with col5:
        st.image("VerifyMajorQuantitiesCoPilot.png", width=120)
        st.markdown("<div style='text-align:center;'>Verify Major Quantities</div>", unsafe_allow_html=True)

    # ---------- SPACE ----------
    st.markdown("###")

    # ---------- CONTENT ----------
    st.markdown("## Welcome")
    st.markdown("---")

    st.write("""
    The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.
    """)

    st.write("""
    By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
    """)

    st.markdown("""
    1. Identify similar past projects for better decision-making  
    2. Predict potential missing work items before they become costly change orders  
    3. Verify major quantities to ensure accurate project planning and resource allocation  
    """)

    st.write("""
    This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications.
    """)
