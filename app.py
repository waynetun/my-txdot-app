import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS targeting layout blocks, text classes, and precise floating coordinates
st.markdown("""
    <style>
    /* Reduce vertical padding between blocks for tighter, consistent spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Define the Single Shake Animation Keyframes */
    @keyframes single-shake-animation {
        0% { transform: translate(0px, 0px) rotate(0deg); }
        15% { transform: translate(-2px, 1px) rotate(-1deg); }
        30% { transform: translate(2px, -1px) rotate(1deg); }
        45% { transform: translate(-2px, -1px) rotate(-1deg); }
        60% { transform: translate(2px, 1px) rotate(1deg); }
        75% { transform: translate(-1px, 0px) rotate(0deg); }
        100% { transform: translate(0px, 0px) rotate(0deg); }
    }

    /* Apply single shake on hover to text blocks */
    .shaky-item:hover {
        display: block;
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
        cursor: pointer;
    }

    /* ---------- PREMIUM NATIVE GLASSMORPHIC NAV ROW ---------- */
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
        padding: 4px; /* Tight padding so the glass border perfectly hugs your card shape */
        display: flex;
        align-items: center;
        justify-content: center;
        
        /* Premium 3D Bevel: top/left highlights, deep right/bottom structure */
        border-top: 1px solid rgba(255, 255, 255, 0.7);
        border-left: 1px solid rgba(255, 255, 255, 0.7);
        border-right: 3px solid rgba(0, 0, 0, 0.12);
        border-bottom: 4px solid rgba(0, 0, 0, 0.18);
        
        /* 3D drop shadow cast towards the bottom-right corner */
        box-shadow: 6px 8px 16px rgba(0, 0, 0, 0.08);
        transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: pointer;
    }

    /* Hover effect: simulates pressing down the 3D glass card */
    .glass-icon-item:hover {
        background: rgba(255, 255, 255, 0.55);
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05);
        transform: translate(3px, 3px);
        border-right: 1px solid rgba(0, 0, 0, 0.05);
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        animation: single-shake-animation 0.4s ease-in-out;
    }

    /* Lock your custom image sizes perfectly inside the glass item boundaries */
    .glass-icon-item img {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 20px;
    }

    /* ---------- TRUE FLOATING CHAT WIDGET EFFECT ---------- */
    div.raised-floating-bot {
        position: fixed;
        bottom: 45px; 
        right: 45px;
        z-index: 999999;
        transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    div.raised-floating-bot:hover {
        transform: translateY(-4px);
    }
    
    div.raised-floating-bot button {
        background-color: #1f77b4 !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 0.75rem 1.75rem !important;
        box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px !important;
    }
    
    div[data-testid="stPopoverBody"] {
        width: 390px !important;
        max-height: 520px !important;
        box-shadow: 0px 12px 36px rgba(0, 0, 0, 0.25) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
        backdrop-filter: blur(8px);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State tracking for the Wayne-AI conversational history securely
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I am Wayne-AI. How can I help you analyze your TxDOT construction project metrics or files today?"}
    ]

# ---------- MAIN CONTENT MARGINS & GRID ----------
left, container, right = st.columns([0.5, 5, 0.5])

with container:
    inner_left, inner_center, inner_right = st.columns([0.5, 11, 0.5])

    with inner_center:
        # ---------- HEADER ----------
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                st.image("txdot-logo-1000x500.png", width=180)
            except:
                st.subheader("TxDOT")
        with col2:
            st.markdown("""
            <div style="display: flex; align-items: center; padding-top: 10px;">
                <h1 style="margin: 0; font-size: 2.2rem; font-weight: bold; color: #000000; line-height: 1.2;">
                    TxDOT - Proactive Construction Work Item Identifier (Pro‑CWII)
                </h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- 3D GLASSMORPHIC ROW FOR YOUR ORIGINAL ICON IMAGES ----------
        # Case-corrected filenames used here ensure they load perfectly on cloud environments
        st.markdown("""
            <div class="glass-icon-container">
                <div class="glass-icon-item"><img src="HomeCopilot.png"></div>
                <div class="glass-icon-item"><img src="HelpCoPilot.png"></div>
                <div class="glass-icon-item"><img src="SampleCopilot.png"></div>
                <div class="glass-icon-item"><img src="FindSimilarProjectCoPilot.png"></div>
                <div class="glass-icon-item"><img src="IdentifyMissingItemsCopilot.png"></div>
                <div class="glass-icon-item"><img src="VerifyMajorQuantitiesCoPilot.png"></div>
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


# ---------- INTERACTIVE FLOATING RAISED POPOVER ----------
st.markdown('<div class="raised-floating-bot">', unsafe_allow_html=True)
with st.popover("🤖 Ask Wayne-AI"):
    st.markdown("### 🤖 Wayne-AI Workspace")
    
    chat_container = st.container()
    user_input = st.chat_input("Type your project question here...")
    
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        copilot_reply = f"Wayne-AI here! I've received your query about: '{user_input}'. Let me pull from the TxDOT historical dataset parameters to build an analysis for you."
        st.session_state.chat_history.append({"role": "assistant", "content": copilot_reply})

    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                
st.markdown('</div>', unsafe_allow_html=True)
