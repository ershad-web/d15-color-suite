import streamlit as st
import streamlit.components.v1 as components
import base64

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

# Encoded web infrastructure to guarantee that Python syntax tracking NEVER crashes
b64_html = (
    "PGRpdiBpZD0iZDE1LWFwcC1jb250YWluZXIiIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9yOiAj"
    "MEQxMTE3OyBwYWRkaW5nOiAyNXB4OyBib3JkZXItcmFkaXVzOiAxMnB4OyBmb250LWZhbWls"
    "eTogc3lzdGVtLXVpLCBzYW5zLXNlcmlmOyBjb2xvcjogd2hpdGU7IHVzZXItc2VsZWN0OiBu"
    "b25lOyI+CiAgICA8ZGl2IHN0eWxlPSJmb250LXdlaWdodDogYm9sZDsgY29sb3I6ICM1OEE2"
    "RkY7IGZvbnQtc2l6ZTogMTNweDsgbWFyZ2luLWJvdHRvbTogMTBweDsgbGV0dGVyLXNwYWNp"
    "bmc6IDAuNXB4OyI+📥IFNURVAgMTogRFJBRyBDT0lOUyBIRVJFTyBPUiBDTElDSyBUTyBQTEFD"
    "RSBUSEVNPC9kaXY+CiAgICA8ZGl2IGlkPSJleGFtLXNsb3RzLXJvdyIgc3R5bGU9ImRpc3Bs"
    "YXk6IGZsZXg7IGdhcDogMTRweDsganVzdGlmeS1jb250ZW50OiBjZW50ZXI7IGFsaWduLWl0"
    "ZW1zOiBjZW50ZXI7IHBhZGRpbmc6IDIwcHg7IGJhY2tncm91bmQ6ICMwNzAAMEU7IGJvcmRl"
    "cjogMnB4IHNvbGlkOiAjMUYyNDJDOyBib3JkZXItcmFkaXVzOiAxMHB4OyBtaW4taGVpZ2h0"
    "OiA5MHB4OyBtYXJnaW4tYm90dG9tOiAzMHB4OyBmbGV4LXdyYXA6IHdyYXA7Ij48L2Rpdj4K"
    "ICAgIAogICAgPGRpdiBzdHlsZT0iZm9udC13ZWlnaHQ6IGJvbGQ7IGNvbG9yOiAjOEI5NDlF"
    "OyBmb250LXNpemU6IDEzcHg7IG1hcmdpbi1ib3R0b206IDEwcHg7IGxldHRlci1zcGFjaW5n"
    "OiAwLjVweDsiPtC6IFNURVAgMjogU09VUkNFIFBJTEUgKEdyYWIgb3Igc2VsZWN0IHBpZWNl"
    "cyBmcm9tIGhlcmUpPC9kaXY+CiAgICA8ZGl2IGlkPSJzY3JhbWJsZWQtc291cmNlLXBpbGUi"
    "IHN0eWxlPSJkaXNwbGF5OiBmbGV4OyBnYXA6IDE0cHg7IGp1c3RpZnktY29udGVudDogY2Vu"
    "dGVyOyBhbGlnbi1pdGVtczogY2VudGVyOyBwYWRkaW5nOiAyNXB4OyBiYWNrZ3JvdW5kOiAj"
    "MTYxQjIyOyBib3JkZXI6IDJweCBkYXNoZWQ6ICMzMDM2M0Q7IGJvcmRlci1yYWRpdXM6IDEw"
    "cHg7IG1pbi1oZWlnaHQ6IDkwcHg7IG1hcmdpbi1ib3R0b206IDI1cHg7IGZsZXgtd3JhcDog"
    "d3JhcDsiPjwvZGl2PgogICAgCiAgICA8ZGl2IHN0eWxlPSJ0ZXh0LWFsaWduOiBjZW50ZXI7"
    "IGRpc3BsYXk6IGZsZXg7IGdhcDogMTVweDsganVzdGlmeS1jb250ZW50OiBjZW50ZXI7Ij4K"
    "ICAgICAgICA8YnV0dG9uIGlkPSJzY29yZS1idG4iIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9y"
    "OiAjMjM4NjM2OyBjb2xvcjogd2hpdGU7IGJvcmRlcjogbm9uZTsgcGFkZGluZzogMTJweCAy"
    "OHB4OyBmb250LXNpemU6IDE1cHg7IGZvbnQtd2VpZ2h0OiBib2xkOyBib3JkZXItcmFkaXVz"
    "OiA2cHg7IGN1cnNvcjogcG9pbnRlcjsgYm94LXNoYWRvdzogMCA0cHggNnB4IHJnYmEoMCww"
    "LDAsMC4yKTsiPlBST0JFIERJQUdOT1NUSUMgUkVTVUxUUzwvYnV0dG9uPgogICAgICAgIDxi"
    "dXR0b24gaWQ9InJlc2V0LWJ0biIgc3R5bGU9ImJhY2tncm91bmQtY29sb3I6ICNBMzcxMTQ7"
    "IGNvbG9yOiB3aGl0ZTsgYm9yZGVyOiBub25lOyBwYWRkaW5nOiAxMnB4IDI4cHg7IGZvbnQt"
    "c2l6ZTogMTVweDsgZm9udC13ZWlnaHQ6IGJvbGQ7IGJvcmRlci1yYWRpZXM6IDZweDsgY3Vy"
    "c29yOiBwb2ludGVyOyBib3gtc2hhZG93OiAwIDRweCA2cHggcmdiYSgwLDAsMCwwLjIpOyBk"
    "aXNwbGF5OiBub25lOyI+🔄IFJFUEVBVCBURVNUIChSRVNFVCk8L2J1dHRvbj4KICAgIDwv"
    "ZGl2PgogICAgCiAgICA8ZGl2IGlkPSJkaWFnbm9zdGljLXJlcG9ydCIgc3R5bGU9Im1hcmdp"
    "bi10b3A6IDMwcHg7IGRpc3BsYXk6IG5vbmU7IGJvcmRlci10b3A6IDFweCBzb2xpZDogIzFG"
    "MjQyQzsgcGFkZGluZy10b3A6IDIwcHg7Ij4KICAgICAgICA8ZGl2IHN0eWxlPSJmb250LXNp"
    "emU6IDI0cHg7IGZvbnQtd2VpZ2h0OiBib2xkOyBjb2xvcjogIzU4QTZGRjsgbWFyZ2luLWJv"
    "dHRvbTogMTVweDsiPtC6IEFVVE9NQVRFRCBDTElOSUNBTCBFVkFMVUFUSU9OIFJFUE9SVDwv"
    "ZGl2PgogICAgICAgIDxkaXYgc3R5bGU9ImZvbnQtc2l6ZTogMThweDsgZm9udC13ZWlnaHQ6"
    "IGJvbGQ7IG1hcmdpbi1ib3R0b206IDE1cHg7Ij5Ub3RhbCBFcnJvciBTY29yZSAoVEVTKTog"
    "PHNwYW4gaWQ9InRlcy12YWwiIHN0eWxlPSJjb2xvcjogI0ZGNkJCheckIj48L3NwYW4+PC9k"
    "aXY+CiAgICAgICAgPGRpdiBpZD0iYWxlcnQtY2FyZCIgc3R5bGU9InBhZGRpbmc6IDE1cHg7"
    "IGJvcmRlci1yYWRpZXM6IDZweDsgZm9udC13ZWlnaHQ6IGJvbGQ7IGZvbnQtc2l6ZTogMTRw"
    "eDsgYmFja2dyb3VuZC1jb2xvcjogIzNCMUIxRTsgY29sb3I6ICNGRjZCNkI7IGJvcmRlcjog"
    "MXB4IHNvbGlkOiAjRkY2QjZCOyI+PC9kaXY+CiAgICA8L2Rpdj4KPC9kaXY+Cgo8c2NyaXB0"
    "Pgpjb25zdCBjb2xvcnMgPSBbIiMwRDFCM0UiLCAiIzA2MzI4QSIsICIjMDA2NkE2Iiw回收"#0D8C80", "#1A9955", "#4CB333", "#99BF26", "#CFAD1A", "#E6801E", "#EB5226", "#E02E59", "#BF1A8C", "#2E0D8C", "#F2F4F7"];
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
        
        slotBox.style.width = "64px"; slotBox.style.height = "64px"; slotBox.style.minWidth = "64px"; slotBox.style.minHeight = "64px";
        slotBox.style.maxWidth = "64px"; slotBox.style.maxHeight = "64px"; slotBox.style.borderRadius = "50%"; slotBox.style.display = "flex";
        slotBox.style.justifyContent = "center"; slotBox.style.alignItems = "center"; slotBox.style.fontSize = "10px"; slotBox.style.fontWeight = "bold"; slotBox.style.boxSizing = "border-box";
        slotsContainer.appendChild(slotBox);
        
        if (capId === null) {
            slotBox.style.border = "2px dashed #30363D"; slotBox.style.backgroundColor = "transparent"; slotBox.innerHTML = "Slot " + slotIdx; slotBox.style.color = "#444C56"; slotBox.style.cursor = "pointer";
            slotBox.addEventListener("click", () => { if (activeDraggedCapId !== null) executeMove(slotIdx); });
        } else {
            slotBox.style.backgroundColor = colors[capId]; slotBox.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)"; slotBox.style.border = "2px solid #21262D";
            if (capId === 0) { slotBox.innerHTML = "START"; slotBox.style.color = "#fff"; slotBox.style.border = "3px solid #58A6FF"; }
            else if (capId === 13) { slotBox.innerHTML = "END"; slotBox.style.color = "#000"; slotBox.style.border = "3px solid #7EE787"; }
            else {
                slotBox.innerHTML = ""; slotBox.setAttribute("draggable", "true"); slotBox.style.cursor = "grab";
                slotBox.addEventListener("dragstart", () => { activeDraggedCapId = capId; activeSourceOrigin = "slot"; activeSourceIndex = slotIdx; });
                slotBox.addEventListener("click", (e) => {
                    e.stopPropagation(); resetHighlights(); activeDraggedCapId = capId; activeSourceOrigin = "slot"; activeSourceIndex = slotIdx;
                    slotBox.style.boxShadow = "0 0 18px #58A6FF, inset 0 0 12px rgba(0,0,0,0.5)"; slotBox.classList.add("selected-coin");
                });
            }
        }
        slotBox.addEventListener("dragover", (e) => e.preventDefault());
        slotBox.addEventListener("drop", (e) => { e.preventDefault(); if (slotStorage[slotIdx] === null) executeMove(slotIdx); });
    });
}

function renderPile() {
    const pileContainer = document.getElementById("scrambled-source-pile"); pileContainer.innerHTML = "";
    if (sourcePile.length === 0) { pileContainer.innerHTML = "<div style='color:#7EE787; font-weight:bold; width:100%; text-align:center;'>🎉 ALL COINS PLACED! CLICK THE BUTTON BELOW TO SCORE.</div>"; return; }
    sourcePile.forEach((capId, pileIdx) => {
        const coin = document.createElement("div");
        coin.style.width = "64px"; coin.style.height = "64px"; coin.style.minWidth = "64px"; coin.style.minHeight = "64px"; coin.style.maxWidth = "64px"; coin.style.maxHeight = "64px";
        coin.style.borderRadius = "50%"; coin.style.backgroundColor = colors[capId]; coin.style.border = "2px solid #21262D"; coin.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)";
        coin.style.display = "flex"; coin.style.justifyContent = "center"; coin.style.alignItems = "center"; coin.style.cursor = "grab"; coin.style.boxSizing = "border-box"; coin.setAttribute("draggable", "true"); coin.innerHTML = "";
        coin.addEventListener("dragstart", () => { activeDraggedCapId = capId; activeSourceOrigin = "pile"; activeSourceIndex = pileIdx; });
        coin.addEventListener("click", (e) => {
            e.stopPropagation(); resetHighlights(); activeDraggedCapId = capId; activeSourceOrigin = "pile"; activeSourceIndex = pileIdx;
            coin.style.boxShadow = "0 0 18px #FFFFFF, inset 0 0 12px rgba(0,0,0,0.5)"; coin.classList.add("selected-coin");
        });
        pileContainer.appendChild(coin);
    });
    pileContainer.addEventListener("dragover", (e) => e.preventDefault());
    pileContainer.addEventListener("drop", (e) => { e.preventDefault(); if (activeSourceOrigin === "slot") { slotStorage[activeSourceIndex] = null; sourcePile.push(activeDraggedCapId); clearSelection(); buildInterface(); } });
}

function executeMove(targetSlotIdx) {
    if (activeSourceOrigin === "pile") sourcePile.splice(activeSourceIndex, 1);
    else if (activeSourceOrigin === "slot") slotStorage[activeSourceIndex] = null;
    slotStorage[targetSlotIdx] = activeDraggedCapId; clearSelection(); buildInterface();
}

function resetHighlights() { document.querySelectorAll(".selected-coin").forEach(el => { el.style.boxShadow = "inset 0 0 12px rgba(0,0,0,0.5), 0 4px 8px rgba(0,0,0,0.4)"; }); }
function clearSelection() { activeDraggedCapId = null; activeSourceOrigin = null; activeSourceIndex = null; }

