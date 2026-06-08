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
        st.markdown("<h2>TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)</h2>", unsafe_allow_html=True)

    st.markdown("###")

    # ---------- ICONS ----------
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image("Sample.png", width=120)
        st.markdown("<div style='text-align:center;'>Sample</div>", unsafe_allow_html=True)

    with col2:
        st.image("Help.png", width=120)
        st.markdown("<div style='text-align:center;'>Help</div>", unsafe_allow_html=True)

    with col3:
        st.image("Find_Similar_Projects.png", width=120)
        st.markdown("<div style='text-align:center;'>Find Similar Projects</div>", unsafe_allow_html=True)

    with col4:
        st.image("Identify_Missing_Items.png", width=120)
        st.markdown("<div style='text-align:center;'>Identify Missing Items</div>", unsafe_allow_html=True)

    with col5:
        st.image("Verify_Major_Quantities.png", width=120)
        st.markdown("<div style='text-align:center;'>Verify Major Quantities</div>", unsafe_allow_html=True)

    st.markdown("###")

    # ---------- CONTENT ----------
    st.markdown("## Welcome")
    st.markdown("---")

    st.write("""
    The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) helps engineers
    predict missing work items and verify major quantities.
    """)

    st.markdown("""
    1. Identify similar past projects  
    2. Predict missing items before change orders  
    3. Verify quantities  
    """)
