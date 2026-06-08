import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CENTER WRAPPER ----------------
st.markdown("""
<div style="max-width:1000px; margin:auto;">
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("txdot-logo-1000x500.png", width=180)

with col2:
    st.markdown("""
    <h1 style="margin-bottom:0;">
    TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </h1>
    """, unsafe_allow_html=True)

# ---------------- BUTTONS (clean + centered) ----------------
st.markdown("###")

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

# ---------------- CONTENT ----------------
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

# ---------------- HOW TO USE ----------------
st.markdown("## How to Use This Tool")
st.markdown("---")

st.markdown("### Prepare Your Data")
st.markdown("""
- Download our sample template to see the required format  
- Ensure your project data includes item codes, quantities, and unit prices  
- Save your file in Excel (.xlsx) format  
""")

st.markdown("### Choose Your Analysis")
st.markdown("""
- Find Similar Projects  
- Identify Missing Work Items  
- Verify Quantities for Major Pay Items  
""")

st.markdown("### Get Results")
st.markdown("""
- Upload your prepared Excel file  
- Review the analysis results  
- Download the detailed report  
- Optionally, receive results via email  
""")

st.markdown("### Need Help?")
st.markdown("""
- Visit our Help page for detailed instructions  
- Download the comprehensive user manual  
- Review common troubleshooting tips  
""")

st.write("""
For the best results, ensure your input data follows the sample format exactly.
""")

# ---------------- CLOSE WRAPPER ----------------
st.markdown("</div>", unsafe_allow_html=True)
