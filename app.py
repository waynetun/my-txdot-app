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


# ---------- STYLING INJECTIONS & FLOATING VIEWPORT OVERRIDES ----------
st.markdown("""
    <style>
    /* CRITICAL ADJUSTMENT: Increased padding-top from 2rem to 4.5rem.
       This pushes the TxDOT logo and app title down so that the toolbar 
       elements never overlap or mask them.
    */
    .block-container {
        padding-top: 4.5rem !important;
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

    /* Keep the overlay iframe completely clear of the viewport layout grid */
    iframe[title="st.components.v1.html"] {
        position: fixed !important;
        top: 0px !important;
        right: 0px !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999999 !important;
        border: none !important;
        background: transparent !important;
        pointer-events: none !important; 
    }
    </style>
""", unsafe_allow_html=True)


# Parse chat bubble records into rendering structures safely
chat_bubbles_html = ""
for msg in st.session_state.chat_history:
    bg_color = "#e1f5fe" if msg["role"] == "user" else "#f3f4f6"
    text_color = "#0369a1" if msg["role"] == "user" else "#1f2937"
    align_side = "margin-left: auto;" if msg["role"] == "user" else "margin-right: auto;"
    
    chat_bubbles_html += f"""
    <div style="max-width: 85%; padding: 10px 14px; border-radius: 12px; margin-bottom: 10px; font-size: 0.85rem; line-height: 1.4; background-color: {bg_color}; color: {text_color}; {align_side}">
        <b>{msg['role'].capitalize()}:</b> {msg['content']}
    </div>
    """


# ---------- PERSISTENT INJECTED COPTILOT WIDGET ----------
st.components.v1.html(f"""
    <div id="wayne-toolbar-pill" style="pointer-events: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; background: transparent; color: #31333f; padding: 4px 10px; font-weight: 400; font-size: 0.875rem; cursor: pointer; border-radius: 8px; border: 1px solid transparent; height: 36px; box-sizing: border-box; user-select: none; transition: background 0.1s; margin-right: 4px;">
        <span style="font-size: 1.05rem; display: flex; align-items: center;">💬</span>
        <span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">Ask Wayne-AI</span>
        <span id="pill-arrow-indicator" style="font-size: 0.55rem; color: #737373; margin-left: 2px;">▼</span>
    </div>

    <div id="wayne-chat-card" style="pointer-events: auto; display: none; position: fixed; top: 50px; right: 20px; width: 340px; height: 480px; background: white; border: 1px solid #cbd5e1; border-radius: 12px; box-shadow: 0px 8px 32px rgba(0,0,0,0.16); flex-direction: column; overflow: hidden; font-family: -apple-system, BlinkMacSystemFont, sans-serif; z-index: 10000000;">
        
        <div style="background: #2b3e50; padding: 12px 14px; color: white; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 600; font-size: 0.9rem; letter-spacing: 0.2px;">👤 Wayne-AI Workspace</span>
        </div>

        <div id="chat-feed-scroller" style="flex: 1; padding: 14px; overflow-y: auto; background: #ffffff; display: flex; flex-direction: column; border-bottom: 1px solid #e2e8f0;">
            {chat_bubbles_html}
        </div>

        <div style="padding: 12px; background: #f8fafc; display: flex; flex-direction: column; gap: 8px;">
            <input id="chat-input-field" type="text" placeholder="Ask about TxDOT item parameters..." style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-size: 0.85rem; outline: none; background: white;" />
            <button id="chat-send-btn" style="background: #1d6fa5; color: white; border: none; padding: 10px; border-radius: 6px; font-weight: 600; cursor: pointer; font-size: 0.85rem; width: 100%; transition: background 0.15s;">Send Query</button>
        </div>
    </div>

    <script>
        function runDOMInjectionPipeline() {{
            const parentDoc = window.parent.document;
            const nativeToolbar = parentDoc.querySelector('.stAppToolbar');
            const targetPill = document.getElementById('wayne-toolbar-pill');
            const targetCard = document.getElementById('wayne-chat-card');
            
            if (!nativeToolbar || !targetPill) {{
                setTimeout(runDOMInjectionPipeline, 100);
                return;
            }}

            // Insert our custom button container neatly inside the toolbar flex-row
            nativeToolbar.insertBefore(targetPill, nativeToolbar.firstChild);
            parentDoc.body.appendChild(targetCard);

            const scroller = document.getElementById('chat-feed-scroller');
            const btn = document.getElementById('chat-send-btn');
            const input = document.getElementById('chat-input-field');
            const arrow = document.getElementById('pill-arrow-indicator');

            if (scroller) {{
                scroller.scrollTop = scroller.scrollHeight;
            }}

            targetPill.addEventListener('mouseenter', () => {{
                targetPill.style.background = 'rgba(151, 166, 195, 0.15)';
            }});
            targetPill.addEventListener('mouseleave', () => {{
                if (targetCard.style.display !== 'flex') {{
                    targetPill.style.background = 'transparent';
                }}
            }});

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

            targetPill.addEventListener('click', (e) => {{
                e.stopPropagation();
                if(targetCard.style.display === 'none' || !targetCard.style.display) {{
                    const pillRect = targetPill.getBoundingClientRect();
                    targetCard.style.top = (pillRect.bottom + 6) + 'px';
                    targetCard.style.right = (parentDoc.documentElement.clientWidth - pillRect.right) + 'px';
                    
                    targetCard.style.display = 'flex';
                    targetPill.style.background = 'rgba(151, 166, 195, 0.25)';
                    arrow.innerHTML = '▲';
                    if (scroller) scroller.scrollTop = scroller.scrollHeight;
                }} else {{
                    targetCard.style.display = 'none';
                    targetPill.style.background = 'transparent';
                    arrow.innerHTML = '▼';
                }}
            }});
        }}

        if (document.readyState === 'complete' || document.readyState === 'interactive') {{
            runDOMInjectionPipeline();
        }} else {{
            document.addEventListener('DOMContentLoaded', runDOMInjectionPipeline);
        }}
    </script>
""", height=0)
