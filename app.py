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
st.markdown("**Instructions:** *Arrange the color coins into the empty slots. **Drag and drop each coin, or click a coin and then click a slot to place it.***")

# Determine paths securely
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

# Secure execution container path loader
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=650, scrolling=True)
else:
    st.error("❌ Diagnostic component template structure ('index.html') missing from the repository root folder.")
