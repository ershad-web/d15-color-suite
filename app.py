%%writefile app.py
import streamlit as st
import streamlit.components.v1 as components

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

# 2. FIXED TWO-ZONE EXAM INTERFACE
html_two_zone_suite = """

    📥 STEP 1: DROP THE COINS INTO THE EMPTY SLOTS IN THIS ROW
    
    🎨 STEP 2: SOURCE PILE (Grab pieces from here)
    
    
        
    
    
        🩺 AUTOMATED CLINICAL EVALUATION REPORT
        Total Error Score (TES): 
        
    



"""

components.html(html_two_zone_suite, height=600, scrolling=True)

     
Overwriting app.py
