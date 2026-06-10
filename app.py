import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

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

# ---------- GLOBAL APPRUN DESIGN STYLES ----------
st.markdown("""
    <style>
    /* Clean up top page padding blocks */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
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
    
    .footer-divider {
        margin-top: 40px;
        margin-bottom: 20px;
        border: 0;
        height: 1px;
        background: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.1), rgba(0,0,0,0));
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State tracking for the Wayne-AI conversational history securely
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I am Wayne-AI. How can I help you analyze your TxDOT construction project metrics or files today?"}
    ]

# Keep track of whether the popup window is open or closed across refreshes
if "chat_is_open" not in st.session_state:
    st.session_state.chat_is_open = "false"

# ---------- MAIN CONTENT DASHBOARD GRID ----------
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

        st.markdown('<hr class="footer-divider">', unsafe_allow_html=True)


# -------------------------------------------------------------------------
# ---------- CHAT PROCESSOR & PARAMETER TRACKING ----------
# -------------------------------------------------------------------------
# Capture messages sent from inside the HTML frame
incoming_message = st.query_params.get("msg", "")
updated_panel_state = st.query_params.get("panel_state", "")

# Save window visibility configuration seamlessly across updates
if updated_panel_state:
    st.session_state.chat_is_open = updated_panel_state
    st.query_params["panel_state"] = ""

if incoming_message:
    st.session_state.chat_history.append({"role": "user", "content": incoming_message})
    copilot_reply = f"Wayne-AI here! I've received your query about: '{incoming_message}'. Let me pull from the TxDOT historical dataset parameters to build an analysis for you."
    st.session_state.chat_history.append({"role": "assistant", "content": copilot_reply})
    st.query_params["msg"] = ""  
    st.rerun()

# Build HTML message string elements dynamically
chat_bubbles_html = ""
for msg in st.session_state.chat_history:
    bg_color = "#e1f5fe" if msg["role"] == "user" else "#f3f4f6"
    text_color = "#0369a1" if msg["role"] == "user" else "#1f2937"
    margin = "margin-left: auto;" if msg["role"] == "user" else "margin-right: auto;"
    
    chat_bubbles_html += f"""
    <div style='max-width: 85%; padding: 10px 14px; border-radius: 16px; margin-bottom: 10px; font-size: 0.9rem; line-height: 1.4; background-color: {bg_color}; color: {text_color}; {margin}'>
        <b>{msg['role'].capitalize()}:</b> {msg['content']}
    </div>
    """

# ---------- POPUP MODAL FOOTER ELEMENT HTML ----------
# The frame height is raised to 520px so that when it expands, it has plenty of structural room to pop up beautifully.
st.components.v1.html(f"""
    <div id="wayne-footer-container" style="width: 100%; max-width: 1100px; margin: 0 auto; padding: 10px; box-sizing: border-box; font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif; position: relative; height: 500px; display: flex; flex-direction: column; justify-content: flex-end;">
        
        <div id="wayne-sliding-window" style="background: rgba(255, 255, 255, 0.98); border: 1px solid rgba(0,0,0,0.1); border-radius: 24px; box-shadow: 0px -10px 30px rgba(0,0,0,0.08); overflow: hidden; display: flex; flex-direction: column; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); width: 100%;">
            
            <div id="wayne-header-bar" style="background: linear-gradient(135deg, #a855f7 0%, #3b82f6 100%); padding: 16px 24px; color: white; display: flex; justify-content: space-between; align-items: center; cursor: pointer; user-select: none;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 1.2rem;">🔮</span>
                    <span style="font-weight: 600; font-size: 1.05rem; letter-spacing: 0.3px;">Wayne-AI Project Analysis Workspace</span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span id="window-status-pill" style="font-size: 0.75rem; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-weight: 500;">Click to Open</span>
                    <span id="toggle-arrow-indicator" style="font-size: 1rem; font-weight: bold; transition: transform 0.3s ease;">▲</span>
                </div>
            </div>
            
            <div id="wayne-drawer-body" style="display: none; flex-direction: column; background: #ffffff;">
                <div style="height: 280px; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; background: #fafafa; border-bottom: 1px solid rgba(0,0,0,0.04);" id="chat-scroller-node">
                    {chat_bubbles_html}
                </div>
                
                <div style="padding: 14px 20px; display: flex; gap: 12px; background: white; align-items: center;">
                    <input id="chat-input-box" type="text" placeholder="Ask Wayne-AI about item codes, quantities or spec details..." style="flex: 1; padding: 12px 18px; border-radius: 50px; border: 1px solid #e5e7eb; outline: none; font-size: 0.9rem;" />
                    <button id="send-chat-payload" style="background: #3b82f6; color: white; border: none; padding: 12px 28px; border-radius: 50px; font-weight: 600; cursor: pointer; font-size: 0.9rem; white-space: nowrap;">Send Request</button>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 15px; font-size: 0.75rem; color: #9ca3af; width: 100%;">
            © 2026 TxDOT Pro-CWII Assistant Network Engine • Powered by Wayne-AI
        </div>
    </div>

    <script>
        const headerBar = document.getElementById('wayne-header-bar');
        const slidingWindow = document.getElementById('wayne-sliding-window');
        const drawerBody = document.getElementById('wayne-drawer-body');
        const arrowIndicator = document.getElementById('toggle-arrow-indicator');
        const statusPill = document.getElementById('window-status-pill');
        
        const sendBtn = document.getElementById('send-chat-payload');
        const inputField = document.getElementById('chat-input-box');
        const scroller = document.getElementById('chat-scroller-node');

        // Parse state flags sent directly from Streamlit session context memory
        let isOpen = {st.session_state.chat_is_open};

        function applyWindowState(open, animate = false) {{
            if (!animate) {{
                slidingWindow.style.transition = 'none';
            }} else {{
                slidingWindow.style.transition = 'all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';
            }}

            if (open) {{
                drawerBody.style.display = 'flex';
                arrowIndicator.style.transform = 'rotate(180deg)';
                statusPill.innerText = "Click to Collapse";
                statusPill.style.background = "rgba(0, 200, 80, 0.25)";
                scroller.scrollTop = scroller.scrollHeight;
            }} else {{
                drawerBody.style.display = 'none';
                arrowIndicator.style.transform = 'rotate(0deg)';
                statusPill.innerText = "Click to Expand";
                statusPill.style.background = "rgba(255,255,255,0.2)";
            }}
        }}

        // Run initial configuration state check on initial boot rendering pipelines
        applyWindowState(isOpen, false);

        // Click handler to slide the window up or down smoothly
        headerBar.addEventListener('click', () => {{
            isOpen = !isOpen;
            applyWindowState(isOpen, true);
            
            // Sync window state configuration flags back to the main parent environment
            const url = new URL(window.parent.location.href);
            url.searchParams.set("panel_state", isOpen ? "true" : "false");
            window.parent.history.replaceState({{}}, "", url.toString());
        }});

        function submitMessage() {{
            const txt = inputField.value.trim();
            if(!txt) return;
            
            const url = new URL(window.parent.location.href);
            url.searchParams.set("msg", txt);
            url.searchParams.set("panel_state", "true"); // Force window open on rerun
            window.parent.location.href = url.toString();
        }}

        sendBtn.addEventListener('click', submitMessage);
        inputField.addEventListener('keydown', (e) => {{
            if(e.key === 'Enter') submitMessage();
        }});
    </script>
""", height=520)
