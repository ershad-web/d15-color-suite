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

# HTML/JavaScript layout built directly inside Python to force immediate cloud rendering
html_engine = """
<div id="d15-app-container" style="background-color: #0D1117; padding: 25px; border-radius: 12px; font-family: system-ui, sans-serif; color: white; user-select: none;">
    <div style="font-weight: bold; color: #58A6FF; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">📥 STEP 1: DRAG COINS HERE OR CLICK TO PLACE THEM</div>
    <div id="exam-slots-row" style="display: flex; gap: 14px; justify-content: center; align-items: center; padding: 20px; background: #070A0E; border: 2px solid #1F242C; border-radius: 10px; min-height: 90px; margin-bottom: 30px; flex-wrap: wrap;"></div>
    
    <div style="font-weight: bold; color: #8B949E; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">🎨 STEP 2: SOURCE PILE (Grab or select pieces from here)</div>
    <div id="scrambled-source-pile" style="display: flex; gap: 14px; justify-content: center; align-items: center; padding: 25px; background: #161B22; border: 2px dashed #30363D; border-radius: 10px; min-height: 90px; margin-bottom: 25px; flex-wrap: wrap;"></div>
    
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
const colors = ["#0D1B3E", "#06328A", "#0066A6", "#0D8C80", "#1A9955", "#4CB333", "#99BF26", "#CFAD1A", "#E6801E", "#EB5226", "#E02E59", "#BF1A8C", "#2E0D8C", "#F2F4F7"];
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
    const slotsContainer = document.getElementById("exam-slots-row"); 
    slotsContainer.innerHTML = "";
    
    slotStorage.forEach((capId, slotIdx) => {
        const slotBox = document.createElement("div"); 
        
        slotBox.style.width = "64px"; 
        slotBox.style.height = "64px"; 
        slotBox.style.minWidth = "64px";
        slotBox.style.minHeight = "64px";
        slotBox.style.maxWidth = "64px";
        slotBox.style.maxHeight = "64px";
        slotBox.style.borderRadius = "50%"; 
        slotBox.style.display = "flex"; 
        slotBox.style.justifyContent = "center"; 
        slotBox.style.alignItems = "center"; 
        slotBox.style.fontSize = "10px"; 
        slotBox.style.fontWeight = "bold";
        slotBox.style.boxSizing = "border-box";
        slotsContainer.appendChild(slotBox);
        
        if (capId === null) {
            slotBox.style.border = "2px dashed #30363D"; 
            slotBox.style.backgroundColor = "transparent"; 
            slotBox.innerHTML = "Slot " + slotIdx; 
            slotBox.style.color = "#444C56";
            slotBox.style.cursor = "pointer";
            
            slotBox.addEventListener("click", () => {
                if (activeDraggedCapId !== null) {
                    executeMove(slotIdx);
                }
            });
        } else {
            slotBox.style.backgroundColor = colors[capId]; 
            slotBox.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)";
            slotBox.style.border = "2px solid #21262D";
            
            if (capId === 0) { 
                slotBox.innerHTML = "START"; 
                slotBox.style.color = "#fff";
                slotBox.style.border = "3px solid #58A6FF"; 
            } else if (capId === 13) { 
                slotBox.innerHTML = "END"; 
                slotBox.style.color = "#000";
                slotBox.style.border = "3px solid #7EE787"; 
            } else {
                slotBox.innerHTML = ""; 
                slotBox.setAttribute("draggable", "true"); 
                slotBox.style.cursor = "grab";
                
                slotBox.addEventListener("dragstart", () => { 
                    activeDraggedCapId = capId; 
                    activeSourceOrigin = "slot"; 
                    activeSourceIndex = slotIdx; 
                });
                
                slotBox.addEventListener("click", (e) => {
                    e.stopPropagation();
                    resetHighlights();
                    activeDraggedCapId = capId;
                    activeSourceOrigin = "slot";
                    activeSourceIndex = slotIdx;
                    slotBox.style.boxShadow = "0 0 18px #58A6FF, inset 0 0 12px rgba(0,0,0,0.5)";
                    slotBox.classList.add('selected-coin');
                });
            }
        }
        
        slotBox.addEventListener("dragover", (e) => e.preventDefault());
        slotBox.addEventListener("drop", (e) => {
            e.preventDefault(); 
            if (slotStorage[slotIdx] === null) {
                executeMove(slotIdx);
            }
        });
    });
}

function renderPile() {
    const pileContainer = document.getElementById("scrambled-source-pile"); 
    pileContainer.innerHTML = "";
    
    if (sourcePile.length === 0) { 
        pileContainer.innerHTML = "<div style='color:#7EE787; font-weight:bold; width:100%; text-align:center;'>🎉 ALL COINS PLACED! CLICK THE BUTTON BELOW TO SCORE.</div>"; 
        return;
    }
    
    sourcePile.forEach((capId, pileIdx) => {
        const coin = document.createElement("div"); 
        coin.style.width = "64px"; 
        coin.style.height = "64px"; 
        coin.style.minWidth = "64px";
        coin.style.minHeight = "64px";
        coin.style.maxWidth = "64px";
        coin.style.maxHeight = "64px";
        coin.style.borderRadius = "50%"; 
        coin.style.backgroundColor = colors[capId]; 
        coin.style.border = "2px solid #21262D"; 
        coin.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)";
        coin.style.display = "flex"; 
        coin.style.justifyContent = "center"; 
        coin.style.alignItems = "center"; 
        coin.style.cursor = "grab"; 
        coin.style.boxSizing = "border-box";
        coin.setAttribute("draggable", "true"); 
        coin.innerHTML = "";
        
        coin.addEventListener("dragstart", () => { 
            activeDraggedCapId = capId; 
            activeSourceOrigin = "pile"; 
            activeSourceIndex = pileIdx; 
        });
        
        coin.addEventListener("click", (e) => {
            e.stopPropagation();
            resetHighlights();
            activeDraggedCapId = capId; 
            activeSourceOrigin = "pile"; 
            activeSourceIndex = pileIdx;
            coin.style.boxShadow = "0 0 18px #FFFFFF, inset 0 0 12px rgba(0,0,0,0.5)";
            coin.classList.add('selected-coin');
        });
        
        pileContainer.appendChild(coin);
    });
    
    pileContainer.addEventListener("dragover", (e) => e.preventDefault());
    pileContainer.addEventListener("drop", (e) => {
        e.preventDefault(); 
        if (activeSourceOrigin === "slot") { 
            slotStorage[activeSourceIndex] = null; 
            sourcePile.push(activeDraggedCapId); 
            clearSelection();
            buildInterface(); 
        }
    });
}

function executeMove(targetSlotIdx) {
    if (activeSourceOrigin === "pile") {
        sourcePile.splice(activeSourceIndex, 1);
    } else if (activeSourceOrigin === "slot") {
        slotStorage[activeSourceIndex] = null;
    }
    slotStorage[targetSlotIdx] = activeDraggedCapId;
    clearSelection();
    buildInterface();
}

function resetHighlights() {
    document.querySelectorAll('.selected-coin').forEach(el => {
        el.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)";
    });
}

function clearSelection() {
    activeDraggedCapId = null;
    activeSourceOrigin = null;
    activeSourceIndex = null;
}

