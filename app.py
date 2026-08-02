import streamlit as st
import streamlit.components.v1 as components

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

# Safely load the independent HTML test module
try:
    with open("index.html", "r", encoding="utf-8") as html_file:
        html_layout_content = html_file.read()
    
    # Render inside Streamlit's component container
    components.html(html_layout_content, height=650, scrolling=True)

except FileNotFoundError:
    st.error("❌ Error: 'index.html' file not found. Ensure it sits in your root GitHub repository directory alongside this app.py file.")
