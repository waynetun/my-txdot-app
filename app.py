import streamlit as st

st.set_page_config(layout="wide")

# Initialize session state for multi-page navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ---------- GLASSMORPHISM CSS ----------
st.markdown("""
<style>
/* Reset background */
.stApp {
    background-color: #f8f9fa;
}

/* Glassmorphism Button Override */
div.stButton > button {
    width: 100% !important;
    height: 110px !important;
    background: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03), 
                inset 0 1px 1px rgba(255, 255, 255, 0.6) !important;
    color: #1e293b !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
}

/* Hover State */
div.stButton > button:hover {
    background: rgba(255, 255, 255, 0.7) !important;
    border: 1px solid rgba(10, 76, 138, 0.4) !important; /* Subtle TxDOT Blue tint */
    box-shadow: 0 10px 40px rgba(10, 76, 138, 0.1) !important;
    transform: translateY(-3px);
    color: #0a4c8a !important;
}

/* Active/Focused State */
div.stButton > button:active, div.stButton > button:focus {
    background: rgba(10, 76, 138, 0.1) !important;
    border: 1px solid #0a4c8a !important;
    color: #0a4c8a !important;
    box-shadow: 0 0 0 2px rgba(10, 76, 138, 0.2) !important;
}

/* Target the text alignment inside the button template */
div.stButton > button p {
    margin: 0 !important;
    line-height: 1.3 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- CREATE CENTER SPACE ----------
left, center, right = st.columns([1, 2, 1])

with center:

    # ---------- HEADER ----------
    col1, col2 = st.columns([1, 2.5])

    with col1:
        # Assumes your file 'txdot-logo-1000x500.png' is in your root directory
        st.image("txdot-logo-1000x500.png", width=180)

    with col2:
        st.markdown("""
        <h2 style='color: #0a4c8a; font-weight: 700; margin-top: 10px; line-height: 1.2;'>
        TxDOT – Proactive Construction Work Item Identifier (Pro‑CWII)
        </h2>
        """, unsafe_allow_html=True)

    # ---------- SPACE ----------
    st.markdown("###")

    # ---------- PROFESSIONAL GLASS BUTTONS ----------
    # SVG icons injected directly before text to ensure crisp rendering on all screens
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    
    with row1_col1:
        if st.button("🏠 \u2001 Home", key="nav_home"):
            st.session_state.current_page = "Home"

    with row1_col2:
        if st.button("📖 \u2001 Help", key="nav_help"):
            st.session_state.current_page = "Help"

    with row1_col3:
        if st.button("📦 \u2001 Sample Templates", key="nav_sample"):
            st.session_state.current_page = "Sample"

    st.markdown("<div style='margin-top: -10px;'></div>", unsafe_allow_html=True) # Tighten row gap

    row2_col1, row2_col2, row2_col3 = st.columns(3)

    with row2_col1:
        if st.button("🔍 \u2001 Find Similar Projects", key="nav_similar"):
            st.session_state.current_page = "Similar"

    with row2_col2:
        if st.button("⚠️ \u2001 Identify Missing Items", key="nav_missing"):
            st.session_state.current_page = "Missing"

    with row2_col3:
        if st.button("📊 \u2001 Verify Major Quantities", key="nav_verify"):
            st.session_state.current_page = "Verify"

    # ---------- SPACE ----------
    st.markdown("###")

    # ---------- ROUTED MAIN CONTENT ----------
    if st.session_state.current_page == "Home":
        st.markdown("<h2 style='color: #1e293b;'>Welcome</h2>", unsafe_allow_html=True)
        st.markdown("---")

        st.write("""
        The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.

        By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
        """)

        st.markdown("""
        1. **Identify similar past projects** for better decision-making  
        2. **Predict potential missing work items** before costly change orders  
        3. **Verify major quantities** for accurate planning  
        """)

        st.write("""
        This tool is specifically designed for Texas Department of Transportation (TxDOT) projects.
        """)

        # ---------- HOW TO USE ----------
        st.markdown("<h2 style='color: #1e293b; margin-top: 40px;'>How to Use This Tool</h2>", unsafe_allow_html=True)
        st.markdown("---")

        use_col1, use_col2 = st.columns(2)
        
        with use_col1:
            st.markdown("### 1. Prepare Your Data")
            st.markdown("""
            - Download sample template  
            - Include item codes, quantities, unit prices  
            - Save file format as `.xlsx`  
            """)

            st.markdown("### 2. Choose Your Analysis")
            st.markdown("""
            - Find Similar Projects  
            - Identify Missing Items  
            - Verify Quantities  
            """)

        with use_col2:
            st.markdown("### 3. Get Results")
            st.markdown("""
            - Upload project data sheet  
            - Review dynamic dashboard insights  
            - Export generated PDF/Excel reports  
            """)

            st.markdown("### Need Help?")
            st.markdown("""
            - Visit the dedicated **Help** section above  
            - Review the TxDOT Pro-CWII user manual  
            - Contact administration for troubleshooting  
            """)

    # Placeholder logic for other views
    elif st.session_state.current_page == "Help":
        st.markdown("<h2 style='color: #1e293b;'>Help & Documentation</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.info("Documentation and user guides regarding the predictive item models go here.")
        
    elif st.session_state.current_page == "Sample":
        st.markdown("<h2 style='color: #1e293b;'>Sample Templates</h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.write("Download sample `.xlsx` configurations.")
        
    elif st.session_state.current_page == "Similar":
        st.markdown("<h2 style='color: #1e293b;'>Find Similar Projects</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
    elif st.session_state.current_page == "Missing":
        st.markdown("<h2 style='color: #1e293b;'>Identify Missing Items</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
    elif st.session_state.current_page == "Verify":
        st.markdown("<h2 style='color: #1e293b;'>Verify Major Quantities</h2>", unsafe_allow_html=True)
        st.markdown("---")
