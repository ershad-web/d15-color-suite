import streamlit as st
import urllib.parse

# 1. Page Configuration Setup
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

# Safely read the frontend layout directly from the separate standalone file
with open("index.html", "r", encoding="utf-8") as html_file:
    html_layout_content = html_file.read()

# Encode the HTML text safely so it can be read as a secure URL by st.iframe
safe_html_url = "data:text/html;charset=utf-8," + urllib.parse.quote(html_layout_content)

# FIXED: Using st.iframe with no deprecated scrolling argument to satisfy the 2026 server rules
st.iframe(src=safe_html_url, height=600)
