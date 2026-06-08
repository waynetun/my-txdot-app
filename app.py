import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background-color: white;
}

/* CENTER CONTAINER */
.wrapper {
    max-width: 1000px;
    margin: auto;
}

/* HEADER */
.header {
    display: flex;
    align-items: center;
    gap: 30px;
}

/* LOGO */
.logo {
    width: 180px;
}

/* TITLE */
.title {
    font-size: 36px;
    font-weight: 600;
}

/* ICON ROW */
.icon-row {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
}

/* GLASS CARD */
.card {
    width: 150px;
    height: 130px;
    border-radius: 12px;
    background: rgba(255,255,255,0.7);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border: 1px solid #ddd;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* HOME BUTTON */
.card-home {
    background: #2a6fa5;
    color: white;
}

/* ICON */
.icon-img {
    width: 36px;
    height: 36px;
    margin-bottom: 8px;
}

/* TEXT */
.card-text {
    font-size: 14px;
    text-align: center;
}

/* SECTION HEADERS */
h2 {
    margin-top: 50px;
}

/* LINE UNDER HEADER */
.line {
    height: 3px;
    background-color: #2a6fa5;
    margin-top: 5px;
    margin-bottom: 20px;
}

/* PARAGRAPH */
p {
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONTENT ----------------
st.markdown("""
<div class="wrapper">

<!-- HEADER -->
<div class="header">
    
    <img src="txdot_logo.png" class="logo">

    <div class="title">
        TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </div>
</div>

<!-- ICONS -->
<div class="icon-row">

<div class="card card-home">
    <img src="https://cdn-icons-png.flaticon.com/512/1946/1946436.png" class="icon-img">
    <div class="card-text">Home</div>
</div>

<div class="card">
    <img src="https://cdn-icons-png.flaticon.com/512/1828/1828817.png" class="icon-img">
    <div class="card-text">Help</div>
</div>

<div class="card">
    <img src="https://cdn-icons-png.flaticon.com/512/2906/2906274.png" class="icon-img">
    <div class="card-text">Sample</div>
</div>

<div class="card">
    <img src="https://cdn-icons-png.flaticon.com/512/681/681494.png" class="icon-img">
    <div class="card-text">Identify Missing Items</div>
</div>

<div class="card">
    <img src="https://cdn-icons-png.flaticon.com/512/190/190411.png" class="icon-img">
    <div class="card-text">Verify Major Quantities</div>
</div>

</div>

<!-- WELCOME -->
<h2>Welcome</h2>
<div class="line"></div>

<p>
The TxDOT - Proactive Construction Work Item Identifier (Pro-CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities in construction and maintenance projects.
</p>

<p>
By analyzing historical project data and using advanced machine learning algorithms, Pro-CWII helps you:
</p>

<ol>
<li>Identify similar past projects for better decision-making.</li>
<li>Predict potential missing work items before they become costly change orders.</li>
<li>Verify major quantities to ensure accurate project planning and resource allocation.</li>
</ol>

<p>
This tool is specifically designed for Texas Department of Transportation (TxDOT) projects and uses TxDOT's standard specifications and work item codes.
</p>

<!-- HOW TO USE -->
<h2>How to Use This Tool</h2>
<div class="line"></div>

<p><b>Prepare Your Data</b></p>
<ul>
<li>Download our sample template to see the required format</li>
<li>Ensure your project data includes item codes, quantities, and unit prices</li>
<li>Save your file in Excel (.xlsx) format</li>
</ul>

<p><b>Choose Your Analysis</b></p>
<ul>
<li>Find Similar Projects</li>
<li>Identify Missing Work Items</li>
<li>Verify Quantities for Major Pay Items</li>
</ul>

<p><b>Get Results</b></p>
<ul>
<li>Upload your prepared Excel file</li>
<li>Review the analysis results</li>
<li>Download the detailed report</li>
<li>Optionally, receive results via email</li>
</ul>

<p><b>Need Help?</b></p>
<ul>
<li>Visit our Help page for detailed instructions</li>
<li>Download the comprehensive user manual</li>
<li>Review common troubleshooting tips</li>
</ul>

<p>
For the best results, ensure your input data follows the sample format exactly.
</p>

</div>
""", unsafe_allow_html=True)
