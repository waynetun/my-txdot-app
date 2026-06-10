import streamlit as st
import base64
import os

# 1. Page Configuration
st.set_page_config(layout="wide")

# 2. State Initialization Pipeline
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I am Wayne-AI. How can I help you analyze your TxDOT construction project metrics or files today?"}
    ]

# ---------- PARSE INCOMING CHAT MESSAGES ----------
incoming_msg = st.query_params.get("msg", "")
if incoming_msg:
    st.session_state.chat_history.append({"role": "user", "content": incoming_msg})
    reply = f"Wayne-AI here! I've received your query about: '{incoming_msg}'. Let me pull from the TxDOT historical dataset parameters to build an analysis for you."
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.query_params["msg"] = ""  
    st.rerun()


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


# ---------- STYLING INJECTIONS & IFRAME WRAPPER CONFIGURATION ----------
st.markdown("""
    <style>
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

    /* Force the Streamlit HTML engine box completely down out of document content metrics */
    iframe[title="st.components.v1.html"] {
        position: fixed !important;
        bottom: 0px !important;
        right: 0px !important;
        overflow: visible !important;
        z-index: 999999 !important;
        border: none !important;
        background: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)


# Parse chat bubble records cleanly
chat_bubbles_html = ""
for msg in st.session_state.chat_history:
    bg_color = "#e1f5fe" if msg["role"] == "user" else "#f3f4f6"
    text_color = "#0369a1" if msg["role"] == "user" else "#1f2937"
    align_side = "margin-left: auto;" if msg["role"] == "user" else "margin-right: auto;"
    
    chat_bubbles_html += f"""
    <div style="max-width: 85%; padding: 10px 14px; border-radius: 16px; margin-bottom: 10px; font-size: 0.85rem; line-height: 1.4; background-color: {bg_color}; color: {text_color}; {align_side}">
        <b>{msg['role'].capitalize()}:</b> {msg['content']}
    </div>
    """


# ---------- IFRAME FLOATING WINDOW COMPONENT CONTAINER ----------
st.components.v1.html(f"""
    <div id="wayne-global-root" style="position: fixed; bottom: 25px; right: 25px; display: flex; flex-direction: column; align-items: flex-end; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;">
        
        <div id="wayne-chat-card" style="display: none; width: 360px; height: 440px; background: white; border: 1px solid rgba(0,0,0,0.1); border-radius: 24px; box-shadow: 0px 12px 40px rgba(0,0,0,0.15); margin-bottom: 12px; flex-direction: column; overflow: hidden;">
            <div style="background: linear-gradient(135deg, #a855f7 0%, #3b82f6 100%); padding: 14px 18px; color: white; display: flex; justify-content: space-between; align-items: center;">
                <span style="font-weight: 600; font-size: 0.95rem; letter-spacing: 0.3px;">🔮 Wayne-AI Workspace</span>
            </div>
            <div id="chat-feed-scroller" style="flex: 1; padding: 16px; overflow-y: auto; background: #fafafa; display: flex; flex-direction: column;">
                {chat_bubbles_html}
            </div>
            <div style="padding: 10px 14px; border-top: 1px solid #eee; display: flex; gap: 8px; background: white;">
                <input id="chat-input-field" type="text" placeholder="Type your project question here..." style="flex: 1; padding: 10px 14px; border-radius: 50px; border: 1px solid #e5e7eb; outline: none; font-size: 0.85rem;" />
                <button id="chat-send-btn" style="background: #3b82f6; color: white; border: none; padding: 0 16px; border-radius: 50px; font-weight: 600; cursor: pointer; font-size: 0.85rem;">Send</button>
            </div>
        </div>

        <button id="wayne-trigger-pill" style="background: linear-gradient(135deg, #a855f7 0%, #3b82f6 100%); color: white; border: none; border-radius: 50px; padding: 14px 24px; font-weight: 600; font-size: 0.95rem; cursor: pointer; box-shadow: 0px 8px 25px rgba(59, 130, 246, 0.35); display: flex; align-items: center; gap: 8px; outline: none; white-space: nowrap;">
            <span>💬</span> Ask Wayne-AI
        </button>
    </div>

    <script>
        setTimeout(() => {{
            const pill = document.getElementById('wayne-trigger-pill');
            const card = document.getElementById('wayne-chat-card');
            const scroller = document.getElementById('chat-feed-scroller');
            const btn = document.getElementById('chat-send-btn');
            const input = document.getElementById('chat-input-field');

            if (scroller) {{
                scroller.scrollTop = scroller.scrollHeight;
            }}

            function sendPayload() {{
                const text = input.value.trim();
                if(!text) return;
                
                const currentUrl = new URL(window.parent.location.href);
                currentUrl.searchParams.set("msg", text);
                window.parent.location.href = currentUrl.toString();
            }}

            btn.addEventListener('click', sendPayload);
            input.addEventListener('keydown', (e) => {{
                if(e.key === 'Enter') sendPayload();
            }});

            pill.addEventListener('click', () => {{
                if(card.style.display === 'none') {{
                    card.style.display = 'flex';
                    scroller.scrollTop = scroller.scrollHeight;
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}, 50);
    </script>
""", height=0)
