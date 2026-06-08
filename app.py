import streamlit as st

st.set_page_config(layout="wide")

# ---------- CSS (THIS MAKES IT LOOK PROFESSIONAL) ----------
st.markdown("""
<style>
body {
    background-color: white;
}

/* container */
.main-container {
    width: 90%;
    margin: auto;
}

/* header */
.header {
    display: flex;
    align-items: center;
    gap: 30px;
}

.header img {
    width: 140px;
}

.title {
    font-size: 42px;
    font-weight: 600;
}

/* icon grid */
.icon-row {
    display: flex;
    gap: 20px;
    margin-top: 30px;
}

/* icon cards */
.card {
    width: 140px;
    height: 140px;
    border-radius: 16px;
    background: #f3f4f6;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}

/* HOME special */
.card-home {
    background: linear-gradient(135deg, #0b5394, #134f83);
    color: white;
}

/* icons */
.icon {
    font-size: 40px;
    margin-bottom: 10px;
}

/* text */
.card-text {
    font-size: 16px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown("""
<div class="main-container">

<div class="header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/TxDOT_logo.svg/512px-TxDOT_logo.svg.png">
    <div class="title">
        TxDOT – Proactive Construction Work Item Identifier (Pro‑CWII)
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- ICON ROW ----------
st.markdown("""
<div class="icon-row">

<div class="card card-home">
    <div class="icon">🏠</div>
    <div class="card-text">Home</div>
</div>

<div class="card">
    <div class="icon">❓</div>
    <div class="card-text">Help</div>
</div>

<div class="card">
    <div class="icon">🧪</div>
    <div class="card-text">Sample</div>
</div>

<div class="card">
    <div class="icon">▦</div>
    <div class="card-text">Identify Missing Items</div>
</div>

<div class="card">
    <div class="icon">✅</div>
    <div class="card-text">Verify Major Quantities</div>
</div>

</div>
""", unsafe_allow_html=True)


# ---------- WELCOME SECTION ----------
st.markdown("""
<h2 style="margin-top:40px;">Welcome</h2>
<hr>

<p>
The TxDOT – Proactive Construction Work Item Identifier (Pro‑CWII) is a powerful tool designed to help engineers and project managers predict and identify potential missing work items and verify major quantities.
</p>

<ol>
<li>Identify similar past projects for better decision-making.</li>
<li>Predict potential missing items before costly change orders.</li>
<li>Verify major quantities to ensure accurate project planning.</li>
</ol>

<p>
This tool is specifically designed for Texas Department of Transportation (TxDOT) projects.
</p>

</div>
""", unsafe_allow_html=True)
