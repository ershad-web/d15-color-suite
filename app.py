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
st.markdown("**Instructions:** *Physically drag the solid color coins from the scrambled pile at the bottom and drop them into the empty slots in the top Exam Tray. Line them up to create a smooth color sequence from START to END.*")

# Safely extract directory path locations to prevent cloud deployment tracking loss
current_directory = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_directory, "index.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as file:
        raw_html_content = file.read()
    
    # Render using the native iframe window wrapper at a locked pixel height
    components.html(raw_html_content, height=650, scrolling=True)
else:
    st.error("❌ Fatal Error: 'index.html' target module structure was not found in the root directory branch.")
