import streamlit as st

st.set_page_config(layout="wide")

# Corrected CSS Injector targeting all specific wrappers with a SINGLE shake
st.markdown("""
    <style>
    /* Reduce vertical padding between blocks for tighter, consistent spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Define the Single Shake Animation Keyframes (Quick & subtle) */
    @keyframes single-shake-animation {
        0% { transform: translate(0px, 0px) rotate(0deg); }
        15% { transform: translate(-2px, 1px) rotate(-1deg); }
        30% { transform: translate(2px, -1px) rotate(1deg); }
        45% { transform: translate(-2px, -1px) rotate(-1deg); }
        60% { transform: translate(2px, 1px) rotate(1deg); }
        75% { transform: translate(-1px, 0px) rotate(0deg); }
        100% { transform: translate(0px, 0px) rotate(0deg); }
    }

    /* Apply the shake effect ONLY ONCE on hover to marked elements */
    .shaky-item:hover, .shaky-icon:hover {
        display: block;
        animation: single-shake-animation 0.4s; /* Set duration */
        animation-iteration-count: 1; /* Key change: Run only once per hover */
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- OUTER CENTER (creates margins) ----------
left, container, right = st.columns([0.5, 5, 0.5])

with container:

    # ---------- INNER FIXED WIDTH ----------
    inner_left, inner_center, inner_right = st.columns([0.5, 11, 0.5])

    with inner_center:

        # ---------- HEADER ----------
        col1, col2 = st.columns([1, 4])

        with col1:
            st.image("txdot-logo-1000x500.png", width=180)

        with col2:
            st.markdown("""
            <div style="display: flex; align-items: center; padding-top: 10px;">
                <h1 style="margin: 0; font-size: 2.2rem; font-weight: bold; color: #000000; line-height: 1.2;">
                    TxDOT - Proactive Construction Work Item Identifier (Pro‑CWII)
                </h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- NAVIGATION ICON ROW WITH SHAKY-ICON WRAPPERS ----------
        icon_cols = st.columns(6)
        
        # Wrapping each column's asset inside our specific sneaky class wrapper
        with icon_cols[0]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("HomeCopilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with icon_cols[1]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("HelpCoPilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with icon_cols[2]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("SampleCopilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with icon_cols[3]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("FindSimilarProjectCoPilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with icon_cols[4]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("IdentifyMissingItemsCopilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with icon_cols[5]:
            st.markdown('<div class="shaky-icon">', unsafe_allow_html=True)
            st.image("VerifyMajorQuantitiesCoPilot.png", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- WELCOME SECTION ----------
        st.markdown("""
        <div class="shaky-item">
            <h2 style="color: #000000; margin-bottom: 4px; padding-bottom: 8px; border-bottom: 3px solid #3498db; margin-top: 0;">
                Welcome
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="shaky-item">
        <p>The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects. By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:</p>
        <ol>
            <li>Identify similar past projects for better decision-making.</li>
            <li>Predict potential missing work items before they become costly change orders.</li>
            <li>Verify major quantities to ensure accurate project planning and resource allocation.</li>
        </ol>
        <p>This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications and work item codes.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- HOW TO USE SECTION ----------
        st.markdown("""
        <div class="shaky-item">
            <h2 style="color: #000000; margin-bottom: 4px; padding-bottom: 8px; border-bottom: 3px solid #2ecc71; margin-top: 0;">
                How to Use This Tool
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="shaky-item">
        <p>Follow these simple steps to get started:</p>
        <h3>Prepare Your Data</h3>
        <ul>
            <li>Download our sample template to see the required format</li>
            <li>Ensure your project data includes item codes, quantities, and unit prices</li>
            <li>Save your file in Excel (.xlsx) format</li>
        </ul>
        <h3>Choose Your Analysis</h3>
        <ul>
            <li>Find Similar Projects</li>
            <li>Identify Missing Work Items</li>
            <li>Verify Quantities for Major Pay Items</li>
        </ul>
        <h3>Get Results</h3>
        <ul>
            <li>Upload your prepared Excel file</li>
            <li>Review the analysis results</li>
            <li>Download the detailed report</li>
            <li>Optionally, receive results via email</li>
        </ul>
        <h3>Need Help?</h3>
        <ul>
            <li>Visit our Help page for detailed instructions</li>
            <li>Download the comprehensive user manual</li>
            <li>Review common troubleshooting tips</li>
        </ul>
        <p>For the best results, ensure your input data follows the sample format exactly.</p>
        </div>
        """, unsafe_allow_html=True)
