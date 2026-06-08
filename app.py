import streamlit as st

st.set_page_config(layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

/* center page */
.center-container {
    max-width: 1000px;
    margin: auto;
    text-align: center;
}

/* header */
.title {
    font-size: 32px;
    font-weight: 600;
    text-align: left;
}

/* icon grid */
.icon-grid {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}

/* glass card */
.icon-card {
    width: 150px;
    height: 150px;
    border-radius: 15px;
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    border: 1px solid rgba(200,200,200,0.5);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* highlight home */
.icon-card-home {
    background: linear-gradient(135deg, #2a6fa5, #1e5d8a);
    color: white;
}

/* icon */
.icon-img {
    width: 48px;
    height: 48px;
    margin-bottom: 10px;
}

/* label */
.icon-label {
    font-size: 14px;
}

/* text content */
.content {
    text-align: left;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ---------- CENTER WRAPPER ----------
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# ---------- HEADER ----------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("txdot-logo-1000x500.png", width=160)

with col2:
    st.markdown("""
    <div class="title">
    TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </div>
    """, unsafe_allow_html=True)

# ---------- ICON GRID ----------
st.markdown("""
<div class="icon-grid">

<div class="icon-card icon-card-home">
    <img src="https://cdn-icons-png.flaticon.com/512/1946/1946436.png" class="icon-img">
    <div class="icon-label">Home</div>
</div>

<div class="icon-card">
    <img src="https://cdn-icons-png.flaticon.com/512/1828/1828817.png" class="icon-img">
    <div class="icon-label">Help</div>
</div>

<div class="icon-card">
    <img src="https://cdn-icons-png.flaticon.com/512/2906/2906274.png" class="icon-img">
    <div class="icon-label">Sample</div>
</div>

<div class="icon-card">
    <img src="https://cdn-icons-png.flaticon.com/512/681/681494.png" class="icon-img">
    <div class="icon-label">Identify Missing Items</div>
</div>

<div class="icon-card">
    <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" class="icon-img">
    <div class="icon-label">Verify Major Quantities</div>
</div>

</div>
""", unsafe_allow_html=True)

# ---------- CONTENT ----------
st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown("## Welcome")
st.markdown("---")

st.write("""
The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.

By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
""")

st.markdown("""
1. Identify similar past projects for better decision-making  
2. Predict potential missing work items before costly change orders  
3. Verify major quantities for accurate planning  
""")

st.write("""
This tool is specifically designed for Texas Department of Transportation (TxDOT) projects.
""")

st.markdown("## How to Use This Tool")
st.markdown("---")

st.markdown("### Prepare Your Data")
st.markdown("""
- Download sample template  
- Include item codes, quantities, unit prices  
- Save as Excel (.xlsx)  
""")

st.markdown("### Choose Your Analysis")
st.markdown("""
- Find Similar Projects  
- Identify Missing Items  
- Verify Quantities  
""")

st.markdown("### Get Results")
st.markdown("""
- Upload file  
- Review results  
- Download report  
""")

st.markdown("### Need Help?")
st.markdown("""
- Visit Help page  
- Read user manual  
- Check troubleshooting tips  
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CLOSE ----------
st.markdown('</div>', unsafe_allow_html=True)
