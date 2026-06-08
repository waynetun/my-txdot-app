import streamlit as st

st.set_page_config(layout="wide")

# ---------- CONTAINER ----------
st.markdown("""
<div style="max-width:1000px; margin:auto;">
""", unsafe_allow_html=True)

# ---------- HEADER (FIXED LOGO) ----------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("txdot-logo-1000x500.png", width=170)

with col2:
    st.markdown("""
    <h2 style="margin-top:20px;">
    TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </h2>
    """, unsafe_allow_html=True)

# ---------- BUTTONS ----------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("🏠 Home", use_container_width=True)

with col2:
    st.button("❓ Help", use_container_width=True)

with col3:
    st.button("📄 Sample", use_container_width=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.button("🔍 Find Similar Projects", use_container_width=True)

with col5:
    st.button("📊 Identify Missing Items", use_container_width=True)

with col6:
    st.button("📦 Verify Major Quantities", use_container_width=True)

# ---------- CONTENT ----------
st.markdown("## Welcome")
st.markdown("---")

st.write("""
The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.

By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
""")

st.markdown("""
1. Identify similar past projects for better decision-making  
2. Predict potential missing work items before they become costly change orders  
3. Verify major quantities to ensure accurate project planning and resource allocation  
""")

st.write("""
This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications and work item codes.
""")

# ---------- HOW TO USE ----------
st.markdown("## How to Use This Tool")
st.markdown("---")

st.markdown("### Prepare Your Data")
st.markdown("""
- Download our sample template  
- Ensure your data includes item codes, quantities, unit prices  
- Save as Excel (.xlsx)  
""")

st.markdown("### Choose Your Analysis")
st.markdown("""
- Find Similar Projects  
- Identify Missing Work Items  
- Verify Major Quantities  
""")

st.markdown("### Get Results")
st.markdown("""
- Upload your file  
- Review results  
- Download report  
- Optional email results  
""")

st.markdown("### Need Help?")
st.markdown("""
- Visit Help page  
- Download user manual  
- Review troubleshooting tips  
""")

st.write("For best results, follow the template exactly.")

# ---------- CLOSE WRAPPER ----------
st.markdown("</div>", unsafe_allow_html=True)
