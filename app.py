import streamlit as st

st.set_page_config(layout="wide")

# Optimized CSS Injector targeting structural layout blocks, text classes, and the floating chatbox
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

    /* Apply single shake on hover to our text blocks */
    .shaky-item:hover {
        display: block;
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
        cursor: pointer;
    }

    /* Target Streamlit's native columns ONLY inside our designated icon row container */
    .shaky-row-container div[data-testid="column"]:hover {
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
        cursor: pointer;
    }

    /* ---------- FLOATING AI CHATBOX BOX STYLING ---------- */
    .floating-chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 320px;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.15);
        border: 1px solid #e0e0e0;
        font-family: sans-serif;
        z-index: 999999;
        overflow: hidden;
    }
    
    /* Apply the single shake effect on hover to the chatbox */
    .floating-chat-container:hover {
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
    }

    .chat-header {
        background-color: #1f77b4;
        color: white;
        padding: 12px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .chat-body {
        padding: 15px;
        height: 200px;
        overflow-y: auto;
        font-size: 0.9rem;
        color: #333333;
        background-color: #f9f9f9;
    }

    .chat-bubble-ai {
        background-color: #e1f5fe;
        padding: 8px 12px;
        border-radius: 12px 12px 12px 0px;
        margin-bottom: 10px;
        line-height: 1.3;
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

        # ---------- NAVIGATION ICON ROW ----------
        st.markdown('<div class="shaky-row-container">', unsafe_allow_html=True)
        
        icon_cols = st.columns(6)
        
        with icon_cols[0]:
            st.image("HomeCopilot.png", use_container_width=True)
        with icon_cols[1]:
            st.image("HelpCoPilot.png", use_container_width=True)
        with icon_cols[2]:
            st.image("SampleCopilot.png", use_container_width=True)
        with icon_cols[3]:
            st.image("FindSimilarProjectCoPilot.png", use_container_width=True)
        with icon_cols[4]:
            st.image("IdentifyMissingItemsCopilot.png", use_container_width=True)
        with icon_cols[5]:
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

# ---------- FLOATING RIGHT CORNER COPILOT CHATBOX ----------
# Placed outside the central column framework so it pins directly to the browser window viewport boundaries
st.markdown("""
    <div class="floating-chat-container">
        <div class="chat-header">
            🤖 Pro-CWII Copilot
        </div>
        <div class="chat-body">
            <div class="chat-bubble-ai">
                Hello! How can I help you analyze your TxDOT construction project data today?
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Embedded target text inputs directly underneath the overlay via Streamlit layout mechanics
with st.sidebar:
    # Optional fallback context or controls could go here. 
    # To keep the chat text input interactive with Python logic, we can place the native input element inside the floating frame area if needed.
    pass
