import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* PAGE BACKGROUND */
body {
    background-color: white;
}

/* MAIN CENTER CONTAINER */
.main-container {
    max-width: 1000px;
    margin: 0 auto;
    padding-top: 20px;
}

/* HEADER */
.header {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 30px;
    margin-bottom: 20px;
}

/* LOGO */
.logo {
    width: 170px;
}

/* TITLE */
.title {
    font-size: 34px;
    font-weight: 600;
    line-height: 1.2;
}

/* BUTTON ROWS */
.button-row {
    display: flex;
    gap: 20px;
    margin-top: 15px;
}

/* BUTTON STYLE */
.button-box {
    flex: 1;
    height: 55px;
    border-radius: 10px;
    border: 1px solid #ddd;
    background-color: #f7f7f7;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
}

/* HOME BUTTON */
.button-primary {
    background-color: #2a6fa5;
    color: white;
    border: none;
}

/* SECTION */
.section {
    margin-top: 50px;
}

/* SECTION LINE */
.line {
    height: 3px;
    background-color: #2a6fa5;
    margin: 10px 0 20px 0;
}

/* TEXT */
p {
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)

# ---------------- CONTENT ----------------
st.markdown("""
<div class="main-container">

<!-- HEADER -->
<div class="header">

    <img src="txdot-logo-1000x500.png" class="logo">

    <div class="title">
        TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)
    </div>

</div>

<!-- BUTTONS ROW 1 -->
<div class="button-row">
    <div class="button-box button-primary">🏠 Home</div>
    <div class="button-box">❓ Help</div>
    <div class="button-box">📄 Sample</div>
</div>

<!-- BUTTONS ROW 2 -->
<div class="button-row">
    <div class="button-box">🔍 Find Similar Projects</div>
    <div class="button-box">📊 Identify Missing Items</div>
    <div class="button-box">📦 Verify Major Quantities</div>
</div>

<!-- WELCOME -->
<div class="section">
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

</div>

<!-- HOW TO USE -->
<div class="section">
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

</div>
""", unsafe_allow_html=True)
