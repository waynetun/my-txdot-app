import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS targeting layout blocks, text classes, and the floating chat panel structure
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

    /* Target Streamlit's native columns inside the icon row container */
    .shaky-row-container div[data-testid="column"]:hover {
        animation: single-shake-animation 0.4s ease-in-out;
        animation-iteration-count: 1;
        cursor: pointer;
    }

    /* ---------- FLOATING COPILOT INTERFACE ---------- */
    /* Sticky bottom-right alignment container for the sidebar popover */
    div[data-testid="stSidebarCollapse"] {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #1f77b4 !important;
        color: white !important;
        border-radius: 50%;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Simple styling rule to customize our chat header block */
    .copilot-header {
        background-color: #1f77b4;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State tracking for the Wayne-AI conversational history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I am Wayne-AI. How can I help you analyze your TxDOT construction project metrics or files today?"}
    ]

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


# ---------- INTERACTIVE SIDEBAR AS CORNER WAYNE-AI PANEL ----------
with st.sidebar:
    st.markdown('<div class="copilot-header">🤖 Wayne-AI Workspace</div>', unsafe_allow_html=True)
    
    # Render historical log exchanges
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
    # Active text processing engine capture terminal 
    if user_input := st.chat_input("Ask Wayne-AI a question..."):
        # Append User input details
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
            
        # Updated Wayne-AI return logic
        copilot_reply = f"Wayne-AI here! I've received your query about: '{user_input}'. Let me pull from the TxDOT historical dataset parameters to build an analysis for you."
        
        st.session_state.chat_history.append({"role": "assistant", "content": copilot_reply})
        with st.chat_message("assistant"):
            st.write(copilot_reply)
