import streamlit as st
import pandas as pd
from datetime import datetime, date
import os
from io import BytesIO

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Payments Tracker (USD)",
    page_icon="💵",
    layout="wide"
)

# ------------------ MOBILE CSS ------------------
mobile_css = """
<style>

/* Make everything bigger on mobile */
@media (max-width: 768px) {

    .block-container {
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
    }

    h1, h2, h3, h4 {
        font-size: 150% !important;
        text-align: center !important;
    }

    .stButton > button {
        width: 100% !important;
        padding: 1rem !important;
        font-size: 1.2rem !important;
        border-radius: 10px !important;
    }

    textarea, input[type=text], input[type=number] {
        font-size: 1.2rem !important;
    }

    .metric-container div {
        text-align: center !important;
    }

    .stDataFrame {
        font-size: 1.1rem !important;
    }

    /* Makes charts not overflow screen */
    .stPlotlyChart, .stAltairChart, .stPyplotChart {
        width: 100% !important;
    }

}
</style>
"""

st.markdown(mobile_css, unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
<div style="padding: 20px; border-radius: 12px; 
background: linear-gradient(90deg, #4CAF50, #81C784);
margin-bottom: 15px;">
    <h1 style="color:white; text-align:center; margin:0;">💵 Payments Dashboard</h1>
    <p style="color:white; text-align:center; margin:0;">Mobile‑first version — optimized for smartphones</p>
</div>
""", unsafe_allow_html=True)

# ------------------ CONSTANTS ------------------
EXCEL_FILE = "payments_records.xlsx"
SHEET = "Records"
COLUMNS = ["Timestamp", "Client", "Service", "Amount Paid (USD)"]

# ------------------ UTIL FUNCTIONS ------------------
@st.cache_data
def load_data():
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
        df["Amount Paid (USD)"] = pd.to_numeric(df["Amount Paid (USD)"], errors="coerce")
        return df
    return pd.DataFrame(columns=COLUMNS)

def save_record(client, service, amount):
    new = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "Client": client,
        "Service": service,
        "Amount Paid (USD)": float(amount),
    }])

    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([df, new], ignore_index=True)
    else:
        df = new

    df.to_excel(EXCEL_FILE, index=False)

def usd(x):
    return f"${x:,.2f}"

df = load_data()

# ------------------ LAYOUT ------------------
is_mobile = st.session_state.get("mobile_width", False)

# Always use single column layout → better for phones
container = st.container()

# ======================================================
# FORM SECTION
# ======================================================
with container:
    st.markdown("## 📝 Add Payment")

    with st.form("add_payment", clear_on_submit=True):
        client = st.text_input("Client Name")
        service = st.text_area("Service Description")
        amount = st.number_input("Amount Paid (USD)", min_value=0.0, step=1.0)
        submitted = st.form_submit_button("💾 Save Payment")

    if submitted:
        if not client or not service:
            st.error("Please fill all fields.")
        else:
            save_record(client, service, amount)
            st.success("Payment saved successfully 🎉")
            st.experimental_rerun()

# ======================================================
# DASHBOARD SECTION
# ======================================================
st.markdown("## 📊 Dashboard & Reports")

if df.empty:
    st.info("No payments yet. Add one above.")
    st.stop()

df["Date"] = df["Timestamp"].dt.date
df["YearMonth"] = df["Timestamp"].dt.to_period("M").astype(str)

# Filters
with st.container():
    st.markdown("### 🔎 Filters")

    f1, f2 = st.columns(2)

    date_range = st.date_input("Date Range", (df["Date"].min(), df["Date"].max()))
    client_filter = st.selectbox("Filter by Client", ["All"] + df["Client"].unique().tolist())
    service_filter = st.selectbox("Filter by Service", ["All"] + df["Service"].unique().tolist())

mask = (df["Date"] >= date_range[0]) & (df["Date"] <= date_range[1])
if client_filter != "All":
    mask &= df["Client"] == client_filter
if service_filter != "All":
    mask &= df["Service"] == service_filter

filtered = df[mask]

# KPI Cards
st.markdown("### 📌 Key Metrics")

k1, k2, k3 = st.columns(3)

k1.metric("Total (USD)", usd(filtered["Amount Paid (USD)"].sum()))
k2.metric("Records", len(filtered))

avg = filtered["Amount Paid (USD)"].mean() if len(filtered) else 0
k3.metric("Avg Ticket", usd(avg))

# Table
st.markdown("### 📄 Records")
st.dataframe(filtered, use_container_width=True)

# Charts
st.markdown("### 📈 Charts")

c1, c2 = st.columns(2)

with c1:
    st.markdown("#### Total by Client")
    st.bar_chart(filtered.groupby("Client")["Amount Paid (USD)"].sum())

with c2:
    st.markdown("#### Total by Service")
    st.bar_chart(filtered.groupby("Service")["Amount Paid (USD)"].sum())

st.markdown("#### Monthly Summary")
st.line_chart(df.groupby("YearMonth")["Amount Paid (USD)"].sum())

