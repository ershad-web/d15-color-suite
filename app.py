import streamlit as st
import random

# Initialize Page Settings
st.set_page_config(page_title="Digital D-15 Slot Suite", layout="wide")

# Official Farnsworth-Munsell D-15 Hex Color Spectrum Values
# Cap 0 is the fixed START anchor, Cap 13 is the fixed END anchor
ALL_COLORS = [
    "#0D1B3E", "#06328A", "#0066A6", "#0D8C80", "#1A9955", "#4CB333", 
    "#99BF26", "#CFAD1A", "#E6801E", "#EB5226", "#E02E59", "#BF1A8C", 
    "#2E0D8C", "#F2F4F7"
]

# Initialize persistent session states for the application logic
if "scrambled_pile" not in st.session_state:
    # Generate the 12 intermediate caps (indices 1 to 12) and scramble them randomly
    caps = list(range(1, 13))
    random.shuffle(caps)
    st.session_state.scrambled_pile = caps

if "exam_tray" not in st.session_state:
    # Pre-fill Exam Tray layout with START (0), 12 empty slots, and END (13)
    st.session_state.exam_tray = [0] + [None] * 12 + [13]

if "selected_coin" not in st.session_state:
    st.session_state.selected_coin = None

# Sidebar Control Pipeline
st.sidebar.title("🩺 Clinical Control Center")
p_name = st.sidebar.text_input("Patient Full Name", "John Doe")
p_id = st.sidebar.text_input("Medical Record ID (MRN)", "MRN-99234-A")
risk = st.sidebar.selectbox("Known Retinal Risk Factor", ["Type 2 Diabetes", "Hydroxychloroquine Toxicity Check", "Routine Glaucoma Screening"])

# Main Application Headers
st.title("Digital D-15 Color Arrangement Assessment Suite")
st.subheader("Medical Validation & Diagnostic Software Prototype (Pure Python Engine)")
st.markdown("---")

st.markdown("### 📋 ACTIVE EXAM SCREEN (Patient Interface)")
st.markdown("**Instructions:** *Click a colored coin from Step 2 to select it, then click any empty gray slot in Step 1 to place it. To return a placed coin to the source pile, click it again.*")
st.write("")

# Helper formatting function to create circular custom metric cap divs safely via markup
def render_cap_circle(cap_index, label=""):
    color_hex = ALL_COLORS[cap_index]
    text_color = "#000000" if cap_index == 13 else "#FFFFFF"
    return f"""
    <div style="
        background-color: {color_hex}; 
        width: 65px; 
        height: 65px; 
        border-radius: 50%; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        color: {text_color}; 
        font-weight: bold; 
        font-size: 11px;
        font-family: sans-serif;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5), 0 4px 6px rgba(0,0,0,0.3);
        border: 2px solid #21262D;
        margin: auto;
    ">{label}</div>
    """

# 📥 STEP 1: EXAM TRAY VIEW
st.markdown("#### 📥 STEP 1: EXAM TRAY (Place Coins Here)")
tray_cols = st.columns(14)

for idx, cap in enumerate(st.session_state.exam_tray):
    with tray_cols[idx]:
        if cap == 0:
            st.markdown(render_cap_circle(0, "START"), unsafe_allow_html=True)
            st.caption("<center>START</center>", unsafe_allow_html=True)
        elif cap == 13:
            st.markdown(render_cap_circle(13, "END"), unsafe_allow_html=True)
            st.caption("<center>END</center>", unsafe_allow_html=True)
        elif cap is not None:
            # Placed adjustable coin layout wrapper logic
            st.markdown(render_cap_circle(cap), unsafe_allow_html=True)
            if st.button("❌ Remove", key=f"rm_{idx}"):
                st.session_state.scrambled_pile.append(cap)
                st.session_state.exam_tray[idx] = None
                st.rerun()
        else:
            # Empty landing destination targets
            st.markdown(
                '<div style="width:65px; height:65px; border-radius:50%; border:2px dashed #444C56; margin:auto; background: transparent;"></div>', 
                unsafe_allow_html=True
            )
            if st.button("Place Here", key=f"slot_{idx}"):
                if st.session_state.selected_coin is not None:
                    coin_to_place = st.session_state.selected_coin
                    st.session_state.exam_tray[idx] = coin_to_place
                    st.session_state.scrambled_pile.remove(coin_to_place)
                    st.session_state.selected_coin = None
                    st.rerun()

st.markdown("---")

# 🎨 STEP 2: SOURCE PILE VIEW
st.markdown("#### 🎨 STEP 2: SOURCE PILE (Select Active Coins From Here)")

if len(st.session_state.scrambled_pile) == 0:
    st.success("🎉 ALL COINS PLACED! CLICK THE 'PROBE DIAGNOSTIC RESULTS' BUTTON BELOW TO SCORE THE ASSESSMENT.")
else:
    # Render available caps dynamically in columns
    pile_cols = st.columns(max(len(st.session_state.scrambled_pile), 1))
    for p_idx, cap in enumerate(st.session_state.scrambled_pile):
        with pile_cols[p_idx]:
            # Highlight selected coin with an exterior layout border matrix outline
            if st.session_state.selected_coin == cap:
                st.markdown(
                    f'<div style="border: 3px solid #58A6FF; border-radius: 50%; padding: 2px; width:73px; margin:auto;">{render_cap_circle(cap)}</div>', 
                    unsafe_allow_html=True
                )
            else:
                st.markdown(render_cap_circle(cap), unsafe_allow_html=True)
                
            if st.button("Select", key=f"sel_{cap}"):
                st.session_state.selected_coin = cap
                st.rerun()

st.markdown("---")

# 🩺 ACTION ENGINE CONTROL PILE ROW
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🩺 PROBE DIAGNOSTIC RESULTS", use_container_width=True):
        if None in st.session_state.exam_tray:
            st.error("⚠️ CANNOT CALIBRATE: Please place all 12 color coins into the tray before running diagnosis.")
        else:
            # Execute medical sequence jump analysis loop metrics
            total_error = 0
            for i in range(len(st.session_state.exam_tray) - 1):
                diff = abs(st.session_state.exam_tray[i] - st.session_state.exam_tray[i+1])
                if diff > 1:
                    total_error += (diff - 1)
            
            st.markdown(f"### Automated Clinical Evaluation Report")
            st.markdown(f"#### Total Error Score (TES): `{total_error}`")
            
            if total_error == 0:
                st.success("✅ PASS: Perfect color sequence arrangement detected.")
            else:
                st.warning(f"⚠️ ATTENTION: Cross-axis sequence jumps detected ({total_error} total configuration errors).")

with btn_col2:
    if st.button("🔄 REPEAT TEST (RESET)", use_container_width=True):
        caps = list(range(1, 13))
        random.shuffle(caps)
        st.session_state.scrambled_pile = caps
        st.session_state.exam_tray = [0] + [None] * 12 + [13]
        st.session_state.selected_coin = None
        st.rerun()
