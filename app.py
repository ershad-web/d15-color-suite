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

# 2. TWO-ZONE EXAM INTERFACE (With added Reset Button functionality)
html_two_zone_suite = """
<div id="d15-app-container" style="background-color: #0D1117; padding: 25px; border-radius: 12px; font-family: system-ui, sans-serif; color: white; user-select: none;">
    
    <div style="font-weight: bold; color: #58A6FF; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">📥 STEP 1: DROP THE COINS INTO THE EMPTY SLOTS IN THIS ROW</div>
    <div id="exam-slots-row" style="display: flex; gap: 12px; justify-content: center; align-items: center; padding: 20px; background: #070A0E; border: 2px solid #1F242C; border-radius: 10px; min-height: 80px; margin-bottom: 30px;"></div>
    
    <div style="font-weight: bold; color: #8B949E; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">🎨 STEP 2: SOURCE PILE (Grab pieces from here)</div>
    <div id="scrambled-source-pile" style="display: flex; gap: 14px; justify-content: center; align-items: center; padding: 25px; background: #161B22; border: 2px dashed #30363D; border-radius: 10px; min-height: 80px; margin-bottom: 25px;"></div>
    
    <div style="text-align: center; display: flex; gap: 15px; justify-content: center;">
        <button id="score-btn" style="background-color: #238636; color: white; border: none; padding: 12px 28px; font-size: 15px; font-weight: bold; border-radius: 6px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">PROBE DIAGNOSTIC RESULTS</button>
        <button id="reset-btn" style="background-color: #A37114; color: white; border: none; padding: 12px 28px; font-size: 15px; font-weight: bold; border-radius: 6px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.2); display: none;">🔄 REPEAT TEST (RESET)</button>
    </div>

    <div id="diagnostic-report" style="margin-top: 30px; display: none; border-top: 1px solid #1F242C; padding-top: 20px;">
        <div style="font-size: 24px; font-weight: bold; color: #58A6FF; margin-bottom: 15px;">🩺 AUTOMATED CLINICAL EVALUATION REPORT</div>
        <div style="font-size: 18px; font-weight: bold; margin-bottom: 15px;">Total Error Score (TES): <span id="tes-val" style="color: #FF6B6B;"></span></div>
        <div id="alert-card" style="padding: 15px; border-radius: 6px; font-weight: bold; font-size: 14px; background-color: #3B1B1E; color: #FF6B6B; border: 1px solid #FF6B6B;"></div>
    </div>
</div>

<script>
const colors = [
    "#0D1B3E", "#06328A", "#0066A6", "#0D8C80", "#1A9955", "#4CB333", 
    "#99BF26", "#CFAD1A", "#E6801E", "#EB5226", "#E02E59", "#BF1A8C", 
    "#2E0D8C", "#F2F4F7"
];

// Re-populated with the exact starting data sequence array values
const originalScrambledPile =;

let slotStorage = [0, null, null, null, null, null, null, null, null, null, null, null, null, 13];
let sourcePile = [...originalScrambledPile]; 

let activeDraggedCapId = null;
let activeSourceOrigin = null;
let activeSourceIndex = null;

function buildInterface() {
    renderSlots();
    renderPile();
}

function renderSlots() {
    const slotsContainer = document.getElementById('exam-slots-row');
    slotsContainer.innerHTML = '';
    
    slotStorage.forEach((capId, slotIdx) => {
        const slotBox = document.createElement('div');
        slotBox.style.width = '64px';
        slotBox.style.height = '64px';
        slotBox.style.borderRadius = '50%';
        slotBox.style.display = 'flex';
        slotsContainer.appendChild(slotBox);
        
        slotBox.style.justifyContent = 'center';
        slotBox.style.alignItems = 'center';
        slotBox.style.fontSize = '11px';
        slotBox.style.fontWeight = 'bold';
        
        if (capId === null) {
            // Empty Target Slots
            slotBox.style.border = '2px dashed #30363D';
            slotBox.style.backgroundColor = 'transparent';
            slotBox.innerHTML = 'Slot ' + slotIdx;
            slotBox.style.color = '#444C56';
        } else {
            // Filled Color Coins
            slotBox.style.backgroundColor = colors[capId];
            slotBox.style.color = (capId === 13) ? '#000' : '#fff';
            slotBox.style.border = '2px solid #21262D';
            
            if (capId === 0) {
                slotBox.innerHTML = 'START';
                slotBox.style.border = '3px solid #58A6FF';
            } else if (capId === 13) {
                slotBox.innerHTML = 'END';
                slotBox.style.border = '3px solid #7EE787';
            } else {
                // Surface remains blank color so patient cannot cheat with numbers
                slotBox.innerHTML = ''; 
                slotBox.setAttribute('draggable', 'true');
                slotBox.style.cursor = 'grab';
                
                slotBox.addEventListener('dragstart', (e) => {
                    activeDraggedCapId = capId;
                    activeSourceOrigin = 'slot';
                    activeSourceIndex = slotIdx;
                });
            }
        }
        
        slotBox.addEventListener('dragover', (e) => e.preventDefault());
        slotBox.addEventListener('drop', (e) => {
            e.preventDefault();
            if (slotStorage[slotIdx] !== null) return;
            
            if (activeSourceOrigin === 'pile') {
                sourcePile.splice(activeSourceIndex, 1);
                slotStorage[slotIdx] = activeDraggedCapId;
            } else if (activeSourceOrigin === 'slot') {
                slotStorage[activeSourceIndex] = null;
                slotStorage[slotIdx] = activeDraggedCapId;
            }
            buildInterface();
        });
    });
}

function renderPile() {
    const pileContainer = document.getElementById('scrambled-source-pile');
    pileContainer.innerHTML = '';
    
    if (sourcePile.length === 0) {
        pileContainer.innerHTML = "<div style='color:#7EE787; font-weight:bold;'>🎉 ALL COINS PLACED! CLICK THE BUTTON BELOW TO SCORE.</div>";
    }
    
    sourcePile.forEach((capId, pileIdx) => {
        const coin = document.createElement('div');
        coin.style.width = '60px';
        coin.style.height = '60px';
        coin.style.borderRadius = '50%';
        coin.style.backgroundColor = colors[capId];
        coin.style.border = '2px solid #21262D';
        coin.style.display = 'flex';
        coin.style.justifyContent = 'center';
        coin.style.alignItems = 'center';
        coin.style.fontWeight = 'bold';
        coin.style.cursor = 'grab';
        coin.setAttribute('draggable', 'true');
        coin.innerHTML = ''; 
        
        coin.addEventListener('dragstart', () => {
            activeDraggedCapId = capId;
            activeSourceOrigin = 'pile';
            activeSourceIndex = pileIdx;
        });
        pileContainer.appendChild(coin);
    });
    
    pileContainer.addEventListener('dragover', (e) => e.preventDefault());
    pileContainer.addEventListener('drop', (e) => {
        e.preventDefault();
        if (activeSourceOrigin === 'slot') {
            slotStorage[activeSourceIndex] = null;
            sourcePile.push(activeDraggedCapId);
            buildInterface();
        }
    });
}

document.getElementById('score-btn').addEventListener('click', () => {
    let incomplete = slotStorage.includes(null);
    const reportDiv = document.getElementById('diagnostic-report');
    const tesSpan = document.getElementById('tes-val');
    const alertCard = document.getElementById('alert-card');
    const resetBtn = document.getElementById('reset-btn');
    
    if (incomplete) {
        reportDiv.style.display = 'block';
        tesSpan.innerText = "N/A";
        alertCard.innerText = "⚠️ CANNOT CALIBRATE: Please place all 12 color coins into the tray before running diagnosis.";
        alertCard.style.backgroundColor = "#3B1B1E";
        alertCard.style.color = "#FF6B6B";
        alertCard.style.border = "1px solid #FF6B6B";
        return;
    }
    
    let totalError = 0;
    for (let i = 0; i < slotStorage.length - 1; i++) {
        let diff = Math.abs(slotStorage[i] - slotStorage[i+1]);
        if (diff > 1) {
            totalError += (diff - 1);
        }
    }
    
    reportDiv.style.display = 'block';
    tesSpan.innerText = totalError;
    resetBtn.style.display = 'inline-block'; 
    
    if (totalError === 0) {
        alertCard.innerText = "✅ PASS: Perfect color sequence arrangement detected. No major vision deficiency patterns flagged.";
        alertCard.style.backgroundColor = "#13231B";
        alertCard.style.color = "#56D364";
        alertCard.style.border = "1px solid #56D364";
    } else {
        alertCard.innerText = "⚠️ ATTENTION: Cross-axis sequence jumps detected. Clinical review recommended for color confusion markers.";
        alertCard.style.backgroundColor = "#3B2E1E";
        alertCard.style.color = "#E3B341";
        alertCard.style.border = "1px solid #E3B341";
    }
});

document.getElementById('reset-btn').addEventListener('click', () => {
    slotStorage = [0, null, null, null, null, null, null, null, null, null, null, null, null, 13];
    sourcePile = [...originalScrambledPile];
