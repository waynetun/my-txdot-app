import streamlit as st

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

/* CENTER PAGE */
.main-container {
    max-width: 1000px;
    margin: auto;
    text-align: center;
}

/* HEADER */
.header {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
}

/* TITLE */
.title {
    font-size: 34px;
    font-weight: 600;
    text-align: left;
}

/* BUTTON ROW */
.button-row {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}

/* BUTTON */
.btn {
    width: 220px;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #ddd;
    background: #f7f7f7;
}

/* PRIMARY BUTTON */
.btn-primary {
    background: #2a6fa5;
    color: white;
}

/* CONTENT TEXT */
.content {
    text-align: left;
    margin-top: 40px;
}

/* SECTIONS */
.section-title {
    margin-top: 40px;
    text-align: left;
}

.line {
    height: 3px;
    background: #2a6fa5;
    width: 100%;
    margin: 10px 0 20px 0;
}

</style>
""", unsafe_allow_html=True)

# ---------- WRAPPER ----------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ---------- HEADER ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("txdot-logo-1000x500.png", width=180)

with col2:
    st.markdown("""
    <div class="title">
    TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </div>
    """, unsafe_allow_html=True)

# ---------- BUTTONS ----------
st.markdown("""
<div class="button-row">
    <div class="btn btn-primary">🏠 Home</div>
    <div class="btn">❓ Help</div>
    <div class="btn">📄 Sample</div>
</div>

<div class="button-row">
    <div class="btn">🔍 Find Similar Projects</div>
    <div class="btn">📊 Identify Missing Items</div>
    <div class="btn">📦 Verify Major Quantities</div>
</div>
""", unsafe_allow_html=True)

# ---------- CONTENT ----------
st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown('<div class="section-title"><h2>Welcome</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

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

st.markdown('<div class="section-title"><h2>How to Use This Tool</h2></div>', unsafe_allow_html=True)
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

st.markdown("### Prepare Your Data")
st.markdown("""
- Download our sample template  
- Ensure your project data includes item codes, quantities, and unit prices  
- Save your file in Excel (.xlsx) format  
""")

st.markdown("### Choose Your Analysis")
st.markdown("""
- Find Similar Projects  
- Identify Missing Work Items  
- Verify Major Quantities  
""")

st.markdown("### Get Results")
st.markdown("""
- Upload your Excel file  
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

st.write("For best results, follow the sample format exactly.")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CLOSE ----------
st.markdown('</div>', unsafe_allow_html=True)
