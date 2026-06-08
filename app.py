import streamlit as st

st.set_page_config(layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background-color: white;
}

/* Header */
.header {
    display: flex;
    align-items: center;
    gap: 30px;
}

/* Logo */
.logo {
    width: 200px;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 600;
}

/* Icon row */
.icon-row {
    display: flex;
    gap: 20px;
    margin-top: 40px;
}

/* Glass cards */
.card {
    width: 140px;
    height: 140px;
    border-radius: 18px;
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(200,200,200,0.6);
    box-shadow: 0 8px 18px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Home highlight */
.card-home {
    background: linear-gradient(135deg, #005ea2, #0a4c8a);
    color: white;
}

/* Icon image */
.icon-img {
    width: 48px;
    height: 48px;
    margin-bottom: 10px;
}

/* Text */
.card-text {
    font-size: 15px;
    text-align: center;
}

/* Welcome */
.welcome {
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/TxDOT_logo.svg" class="logo">
    <div class="title">
        TxDOT – Proactive Construction Work Item Identifier (Pro‑CWII)
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- ICONS ----------------
st.markdown("""
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
""", unsafe_allow_html=True)


# ---------------- WELCOME ----------------
st.markdown("""
<div class="welcome">

<h2>Welcome</h2>
<hr>

<p>
The TxDOT – Proactive Construction Work Item Identifier (Pro‑CWII) is a powerful tool designed to help engineers and project managers predict and identify missing work items and verify major quantities.
</p>

<ol>
<li>Identify similar past projects for better decision-making.</li>
<li>Predict missing work items before costly change orders.</li>
<li>Verify major quantities for accurate planning.</li>
</ol>

<p>
Designed specifically for Texas Department of Transportation (TxDOT) projects.
</p>

</div>
""", unsafe_allow_html=True)
