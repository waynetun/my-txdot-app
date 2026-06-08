import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS to handle spacing and layout structure
st.markdown("""
    <style>
    /* Reduce vertical padding between blocks for tighter, consistent spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Eliminate extra default bottom margins from image blocks in the icon grid */
    div[data-testid="stImage"] {
        margin-bottom: 0rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- OUTER CENTER (creates margins) ----------
left, container, right = st.columns([1, 4, 1])

with container:

    # ---------- INNER FIXED WIDTH ----------
    inner_left, inner_center, inner_right = st.columns([1, 10, 1])

    with inner_center:

        # ---------- HEADER ----------
        col1, col2 = st.columns([1, 3.5])

        with col1:
            st.image("txdot-logo-1000x500.png", width=180)

        with col2:
            st.markdown("""
            <div style="display: flex; align-items: center; height: 100px;">
                <h1 style="margin: 0; font-size: 2rem; font-weight: bold; color: #000000; line-height: 1.2;">
                    TxDOT - Proactive<br>Construction Work Item<br>Identifier (Pro‑CWII)
                </h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- NAVIGATION ICON ROWS ----------
        # Row 1: Home, Help, Sample
        row1_col1, row1_col2, row1_col3 = st.columns(3)
        with row1_col1:
            st.image("SampleCopilot.png", use_container_width=True) # Assuming this is the Home/Blue icon based on your first screenshot
        with row1_col2:
            st.image("HelpCoPilot.png", use_container_width=True)
        with row1_col3:
            st.image("SampleCopilot.png", use_container_width=True)

        # Row 2: Find Similar Projects, Identify Missing Items, Verify Major Quantities
        row2_col1, row2_col2, row2_col3 = st.columns(3)
        with row2_col1:
            st.image("FindSimilarProjectCoPilot.png", use_container_width=True)
        with row2_col2:
            st.image("IdentifyMissingItemsCopilot.png", use_container_width=True)
        with row2_col3:
            st.image("VerifyMajorQuantitiesCoPilot.png", use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- WELCOME SECTION ----------
        st.markdown("""
        <h2 style="color: #000000; margin-bottom: 4px; padding-bottom: 8px; border-bottom: 3px solid #3498db;">
            Welcome
        </h2>
        """, unsafe_allow_html=True)
        
        # Combined text block to ensure pixel-perfect line spacing
        st.markdown("""
The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects. By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:

1. Identify similar past projects for better decision-making.
2. Predict potential missing work items before they become costly change orders.
3. Verify major quantities to ensure accurate project planning and resource allocation.

This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications and work item codes.
        """)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- HOW TO USE SECTION ----------
        st.markdown("""
        <h2 style="color: #000000; margin-bottom: 4px; padding-bottom: 8px; border-bottom: 3px solid #2ecc71;">
            How to Use This Tool
        </h2>
        """, unsafe_allow_html=True)
        
        st.markdown("""
Follow these simple steps to get started:

### Prepare Your Data
* Download our sample template to see the required format  
* Ensure your project data includes item codes, quantities, and unit prices  
* Save your file in Excel (.xlsx) format  

### Choose Your Analysis
* Find Similar Projects  
* Identify Missing Work Items  
* Verify Quantities for Major Pay Items  

### Get Results
* Upload your prepared Excel file  
* Review the analysis results  
* Download the detailed report  
* Optionally, receive results via email  

### Need Help?
* Visit our Help page for detailed instructions  
* Download the comprehensive user manual  
* Review common troubleshooting tips  

For the best results, ensure your input data follows the sample format exactly.
        """)
