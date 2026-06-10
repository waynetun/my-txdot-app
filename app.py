import streamlit as st
import base64
import os

# 1. Set page configuration first
st.set_page_config(layout="wide")

# 2. CLEAR ALL RUNTIME BUGS: Initialize Session State at the Absolute Top
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I am Wayne-AI. How can I help you analyze your TxDOT construction project metrics or files today?"}
    ]

if "chat_is_open" not in st.session_state:
    st.session_state.chat_is_open = False


# Helper function to safely convert local image files into base64 HTML strings
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode()}"
    return ""

# Pre-encode all navigation icons securely
home_b64 = get_image_base64("HomeCopilot.png")
help_b64 = get_image_base64("HelpCoPilot.png")
sample_b64 = get_image_base64("SampleCopilot.png")
similar_b64 = get_image_base64("FindSimilarProjectCoPilot.png")
missing_b64 = get_image_base64("IdentifyMissingItemsCopilot.png")
verify_b64 = get_image_base64("VerifyMajorQuantitiesCoPilot.png")


# ---------- GLOBAL SYSTEM-WIDE CSS INJECTIONS ----------
st.markdown("""
    <style>
    /* Clean up overall layout margins */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* Single Shake Hover Animation */
    @keyframes single-shake-animation {
        0% { transform: translate(0px, 0px) rotate(0deg); }
        15% { transform: translate(-2px, 1px) rotate(-1deg); }
        30% { transform: translate(2px, -1px) rotate(1deg); }
        45% { transform: translate(-2px, -1px) rotate(-1deg); }
        60% { transform: translate(2px, 1px) rotate(1deg); }
        75% { transform: translate(-1px, 0px) rotate(0deg); }
        100% { transform: translate(0px, 0px) rotate(0deg); }
    }

    .shaky-item:hover {
        display: block;
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
        cursor: pointer;
    }

    /* ---------- FLEXBOX 3D GLASS NAVIGATION ROW ---------- */
    .glass-icon-container {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        width: 100%;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    .glass-icon-item {
        flex: 1;
        background: rgba(255, 255, 255, 0.35);
        backdrop-filter: blur(12px) saturate(140%);
        -webkit-backdrop-filter: blur(12px) saturate(140%);
        border-radius: 24px;
        padding: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-top: 1px solid rgba(255, 255, 255, 0.7);
        border-left: 1px solid rgba(255, 255, 255, 0.7);
        border-right: 3px solid rgba(0, 0, 0, 0.12);
        border-bottom: 4px solid rgba(0, 0, 0, 0.18);
        box-shadow: 6px 8px 16px rgba(0, 0, 0, 0.08);
        transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: pointer;
    }

    .glass-icon-item:hover {
        background: rgba(255, 255, 255, 0.55);
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05);
        transform: translate(3px, 3px);
        border-right: 1px solid rgba(0, 0, 0, 0.05);
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        animation: single-shake-animation 0.4s ease-in-out;
    }

    .glass-icon-item img {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 20px;
    }

    /* ---------- FLOATING POSITION HOOK ENGINE ---------- 
       This completely tears the widget out of Streamlit's layout flow 
       and anchors it beautifully to the bottom right corner.
    */
    div[data-testid="stVerticalBlockBorderWrapper"]:has(div#wayne-floating-anchor) {
        position: fixed !important;
        bottom: 20px !important;
        right: 20px !important;
        width: 380px !important;
        z-index: 999999 !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- MAIN DASHBOARD LAYOUT GRID ----------
left, container, right = st.columns([0.5, 5, 0.5])

with container:
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

        # ---------- NAVIGATION BAR CONTAINER ----------
        st.markdown(f"""
            <div class="glass-icon-container">
                <div class="glass-icon-item"><img src="{home_b64 if home_b64 else 'https://img.icons8.com/fluency/96/home.png'}"></div>
                <div class="glass-icon-item"><img src="{help_b64 if help_b64 else 'https://img.icons8.com/fluency/96/help.png'}"></div>
                <div class="glass-icon-item"><img src="{sample_b64 if sample_b64 else 'https://img.icons8.com/fluency/96/test-partial-passed.png'}"></div>
                <div class="glass-icon-item"><img src="{similar_b64 if similar_b64 else 'https://img.icons8.com/fluency/96/layers.png'}"></div>
                <div class="glass-icon-item"><img src="{missing_b64 if missing_b64 else 'https://img.icons8.com/fluency/96/delete-property.png'}"></div>
                <div class="glass-icon-item"><img src="{verify_b64 if verify_b64 else 'https://img.icons8.com/fluency/96/checked-checkbox.png'}"></div>
            </div>
        """, unsafe_allow_html=True)

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

        # EXACTLY ONE CLEAN LINE SPACE GAP UNDER THE LAST PARAGRAPH
        st.markdown('<div style="margin-top: 24px;"></div>', unsafe_allow_html=True)


# -------------------------------------------------------------------------
# ---------- PRODUCTION-READY FLOATING WAYNE-AI MOTOR ENGINE ----------
# -------------------------------------------------------------------------
floating_box = st.container()
with floating_box:
    # Anchor Hook that links directly to the viewport-pinning CSS rule above
    st.markdown('<div id="wayne-floating-anchor"></div>', unsafe_allow_html=True)
    
    # Process messaging
