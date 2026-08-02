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
st.markdown("**Instructions:** *Drag the solid color coins from the scrambled pile at the bottom and drop them into the empty slots in the top Exam Tray. Line them up to create a smooth color sequence from START to END. (If dragging feels restricted by your browser, you can also click a coin and click a slot).*")

# Read the HTML layout file safely
try:
    with open("index.html", "r", encoding="utf-8") as html_file:
        html_layout_content = html_file.read()
    
    # Use Streamlit's official HTML component to bypass iframe security blocks
    components.html(html_layout_content, height=650, scrolling=True)

except FileNotFoundError:
    st.error("❌ Error: 'index.html' file not found. Please make sure index.html is in the same GitHub repository folder as your python script.")
