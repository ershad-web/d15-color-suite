import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Digital D-15 Slot Suite", layout="wide")

st.sidebar.title("🩺 Clinical Control Center")
p_name = st.sidebar.text_input("Patient Full Name", "John Doe")
p_id = st.sidebar.text_input("Medical Record ID (MRN)", "MRN-99234-A")
risk = st.sidebar.selectbox("Known Retinal Risk Factor", ["Type 2 Diabetes", "Hydroxychloroquine Toxicity Check", "Routine Glaucoma Screening"])

st.title("Digital D-15 Color Arrangement Assessment Suite")
st.subheader("Medical Validation & Diagnostic Software Prototype")
st.markdown("---")

st.markdown("### 📋 ACTIVE EXAM SCREEN (Patient Interface)")
st.markdown("**Instructions:** *Drag the solid color coins from the scrambled pile at the bottom and drop them into the empty slots in the top Exam Tray. Line them up to create a smooth color sequence from START to END.*")

# Look up the local directory file safely without complex inline code strings
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=550, scrolling=True)
else:
    st.error("❌ Critical Error: 'index.html' template is missing from your repository.")

st.markdown("---")

# 🩺 FIXED CLINICAL REERENCE SHEETS FOR DOCTORS
st.subheader("📊 Clinical Interpretation Reference Sheet")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**1️⃣ Severity Threshold Brackets**")
    st.markdown("* **TES = 0**: Normal Vision Baseline. Perfect sequential hue alignment across standard pathways.")
    st.markdown("* **TES = 1 to 11**: Mild Variant / Operational Error. Minor local swaps related to monitor glare or eye fatigue.")
    st.markdown("* **TES = 12 to 30**: Moderate Color Vision Deficiency. Confirmed sequencing errors impacting wavelength tracking.")
    st.markdown("* **TES > 30 (e.g., 46 or 50)**: Severe / Profound Color Deficit. Cross-axis confusion shortcuts across the wheel, indicating structural congenital or acquired color blindness.")

with col2:
    st.markdown("**2️⃣ Color Wheel Cross-Axis Meanings**")
    st.markdown("* **Protan Axis (Red-Deficient)**: Confusion jumps skip vertically across the middle of the color circle (linking blues directly to oranges).")
    st.markdown("* **Deutan Axis (Green-Deficient)**: Confusion paths slice diagonally (misaligning soft greens with purples or hot pinks).")
    st.markdown("* **Tritan Axis (Blue-Deficient)**: Confusion shifts horizontally (confusing yellow-greens with deep violets). Highly vital for tracking Hydroxychloroquine (Plaquenil) Retinal Toxicity.")
