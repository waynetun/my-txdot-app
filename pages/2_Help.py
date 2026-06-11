import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

# Function to get icon images (ensure these files exist in your root directory)
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return f"data:image/png;base64,{base64.b64encode(image_file.read()).decode()}"
    return ""

# Load icons
home_b64 = get_image_base64("HomeCopilot.png")
help_b64 = get_image_base64("HelpCoPilot.png")
# ... add other icons as needed

# --- NAVIGATION ICON CONTAINER ---
st.markdown(f"""
<style>
.glass-icon-container {{
    display: flex;
    justify-content: flex-start;
    gap: 16px;
    margin-bottom: 30px;
}}
.glass-icon-item {{
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 10px;
    border: 1px solid rgba(255, 255, 255, 0.7);
    box-shadow: 4px 4px 10px rgba(0,0,0,0.1);
    width: 60px;
}}
.glass-icon-item img {{ width: 100%; }}
</style>

<div class="glass-icon-container">
    <a href="/" class="glass-icon-item"><img src="{home_b64}"></a>
    <div class="glass-icon-item"><img src="{help_b64}"></div>
</div>
""", unsafe_allow_html=True)

# --- HELP CONTENT ---
st.title("📘 Pro-CWII Help Center")
st.markdown("Welcome to the Pro-CWII Help Center!...")
st.divider()
# ... (rest of your help text)
