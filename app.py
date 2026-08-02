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
st.markdown("**Instructions:** *Drag the solid color coins from the scrambled pile at the bottom and drop them into the empty slots in the top Exam Tray. Line them up to create a smooth color sequence from START to END.*")

# We build the application using safe string additions so the Python parser can NEVER crash
html_data = (
    '<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
    'body { background-color: #0D1117; margin: 0; padding: 10px; font-family: system-ui, sans-serif; color: white; user-select: none; }'
    '.row-container { display: flex; gap: 14px; justify-content: center; align-items: center; padding: 20px; background: #070A0E; border: 2px solid #1F242C; border-radius: 10px; min-height: 80px; margin-bottom: 25px; flex-wrap: wrap; }'
    '.source-container { background: #161B22; border: 2px dashed #30363D; }'
    '.cap-circle { width: 64px; height: 64px; min-width: 64px; min-height: 64px; max-width: 64px; max-height: 64px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 10px; font-weight: bold; box-sizing: border-box; }'
    '.dynamic-coin { border: 2px solid #21262D; box-shadow: inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4); cursor: grab; }'
    '.dynamic-coin:active { cursor: grabbing; }'
    '.empty-slot { border: 2px dashed #30363D; background-color: transparent; color: #444C56; }'
    '.btn-action { background-color: #238636; color: white; border: none; padding: 12px 28px; font-size: 15px; font-weight: bold; border-radius: 6px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.2); }'
    '.btn-reset { background-color: #A37114; }'
    '</style></head><body>'
    '<div id="d15-app-container">'
    '    <div style="font-weight: bold; color: #58A6FF; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">📥 STEP 1: DROP THE COINS INTO THE EMPTY SLOTS IN THIS ROW</div>'
    '    <div id="exam-slots-row" class="row-container"></div>'
    '    <div style="font-weight: bold; color: #8B949E; font-size: 13px; margin-bottom: 10px; letter-spacing: 0.5px;">🎨 STEP 2: SOURCE PILE (Drag pieces from here)</div>'
    '    <div id="scrambled-source-pile" class="row-container source-container"></div>'
    '    <div style="text-align: center; display: flex; gap: 15px; justify-content: center;">'
    '        <button id="score-btn" class="btn-action">PROBE DIAGNOSTIC RESULTS</button>'
    '        <button id="reset-btn" class="btn-action btn-reset" style="display: none;">🔄 REPEAT TEST (RESET)</button>'
    '    </div>'
    '    <div id="diagnostic-report" style="margin-top: 30px; display: none; border-top: 1px solid #1F242C; padding-top: 20px;">'
    '        <div style="font-size: 24px; font-weight: bold; color: #58A6FF; margin-bottom: 15px;">🩺 AUTOMATED CLINICAL EVALUATION REPORT</div>'
    '        <div style="font-size: 18px; font-weight: bold; margin-bottom: 15px;">Total Error Score (TES): <span id="tes-val" style="color: #FF6B6B;"></span></div>'
    '        <div id="alert-card" style="padding: 15px; border-radius: 6px; font-weight: bold; font-size: 14px;"></div>'
    '    </div>'
    '</div>'
    '<script>'
    'const colors = ["#0D1B3E", "#06328A", "#0066A6", "#0D8C80", "#1A9955", "#4CB333", "#99BF26", "#CFAD1A", "#E6801E", "#EB5226", "#E02E59", "#BF1A8C", "#2E0D8C", "#F2F4F7"];'
    'const originalScrambledPile = [7, 4, 11, 2, 8, 1, 9, 5, 10, 3, 6, 12];'
    'let slotStorage = [0, null, null, null, null, null, null, null, null, null, null, null, null, 13];'
    'let sourcePile = [...originalScrambledPile];'
    'let activeDraggedCapId = null; let activeSourceOrigin = null; let activeSourceIndex = null;'
    'function buildInterface() {'
    '    const slotsContainer = document.getElementById("exam-slots-row"); slotsContainer.innerHTML = "";'
    '    slotStorage.forEach((capId, slotIdx) => {'
    '        const slotBox = document.createElement("div"); slotBox.className = "cap-circle"; slotsContainer.appendChild(slotBox);'
    '        if (capId === null) {'
    '            slotBox.className += " empty-slot"; slotBox.innerHTML = "Slot " + slotIdx;'
    '        } else {'
    '            slotBox.className += " dynamic-coin"; slotBox.style.backgroundColor = colors[capId]; slotBox.style.color = (capId === 13) ? "#000" : "#fff";'
    '            if (capId === 0) { slotBox.innerHTML = "START"; slotBox.style.border = "3px solid #58A6FF"; }'
    '            else if (capId === 13) { slotBox.innerHTML = "END"; slotBox.style.border = "3px solid #7EE787"; }'
    '            else {'
    '                slotBox.innerHTML = ""; slotBox.setAttribute("draggable", "true");'
    '                slotBox.addEventListener("dragstart", () => { activeDraggedCapId = capId; activeSourceOrigin = "slot"; activeSourceIndex = slotIdx; });'
    '            }'
    '        }'
    '        slotBox.addEventListener("dragover", (e) => e.preventDefault());'
    '        slotBox.addEventListener("drop", (e) => {'
    '            e.preventDefault(); if (slotStorage[slotIdx] !== null) return;'
    '            if (activeSourceOrigin === "pile") { sourcePile.splice(activeSourceIndex, 1); }'
    '            else if (activeSourceOrigin === "slot") { slotStorage[activeSourceIndex] = null; }'
    '            slotStorage[slotIdx] = activeDraggedCapId; buildInterface();'
    '        });'
    '    });'
    '    const pileContainer = document.getElementById("scrambled-source-pile"); pileContainer.innerHTML = "";'
    '    if (sourcePile.length === 0) { pileContainer.innerHTML = "<div style=\'color:#7EE787; font-weight:bold;\'>🎉 ALL COINS PLACED! CLICK THE BUTTON BELOW TO RUN MEDICAL DIAGNOSIS.</div>"; }'
    '    else {'
    '        sourcePile.forEach((capId, pileIdx) => {'
    '            const coin = document.createElement("div"); coin.className = "cap-circle dynamic-coin"; coin.style.backgroundColor = colors[capId]; coin.setAttribute("draggable", "true");'
    '            coin.addEventListener("dragstart", () => { activeDraggedCapId = capId; activeSourceOrigin = "pile"; activeSourceIndex = pileIdx; });'
    '            pileContainer.appendChild(coin);'
    '        });'
    '    }'
    '}'
    'pileContainerBox = document.getElementById("scrambled-source-pile");'
    'pileContainerBox.addEventListener("dragover", (e) => e.preventDefault());'
    'pileContainerBox.addEventListener("drop", (e) => {'
    '    e.preventDefault(); if (activeSourceOrigin === "slot") { slotStorage[activeSourceIndex] = null; sourcePile.push(activeDraggedCapId); buildInterface(); }'
    '});'
    'document.getElementById("score-btn").addEventListener("click", () => {'
    '    let incomplete = slotStorage.includes(null); const reportDiv = document.getElementById("diagnostic-report"); const tesSpan = document.getElementById("tes-val"); const alertCard = document.getElementById("alert-card"); const resetBtn = document.getElementById("reset-btn");'
    '    if (incomplete) {'
    '        reportDiv.style.display = "block"; tesSpan.innerText = "N/A"; alertCard.innerText = "⚠️ CANNOT CALIBRATE: Please place all 12 color coins into the tray before running diagnosis.";'
    '        alertCard.style.backgroundColor = "#3B1B1E"; alertCard.style.color = "#FF6B6B"; alertCard.style.border = "1px solid #FF6B6B"; return;'
    '    }'
    '    let totalError = 0;'
    '    for (let i = 0; i < slotStorage.length - 1; i++) { let diff = Math.abs(slotStorage[i] - slotStorage[i+1]); if (diff > 1) totalError += (diff - 1); }'
    '    reportDiv.style.display = "block"; tesSpan.innerText = totalError; resetBtn.style.display = "inline-block";'
    '    if (totalError === 0) { alertCard.innerText = "✅ PASS: Perfect color sequence arrangement detected."; alertCard.style.backgroundColor = "#13231B"; alertCard.style.color = "#56D364"; alertCard.style.border = "1px solid #56D364"; }'
    '    else { alertCard.innerText = "⚠️ ATTENTION: Cross-axis sequence jumps detected (" + totalError + " errors)."; alertCard.style.backgroundColor = "#3B2E1E"; alertCard.style.color = "#E3B341"; alertCard.style.border = "1px solid #E3B341"; }'
    '});'
    'document.getElementById("reset-btn").addEventListener("click", () => {'
    '    slotStorage = [0, null, null, null, null, null, null, null, null, null, null, null, null, 13]; sourcePile = [...originalScrambledPile];'
    '    document.getElementById("diagnostic-report").style.display = "none"; document.getElementById("reset-btn").style.display = "none"; buildInterface();'
    '});'
    'buildInterface();</script></body></html>'
)

# Render the layout component container safely inside your hosted workspace
components.html(html_data, height=650, scrolling=True)
