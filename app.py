import streamlit as st
import pandas as pd
from datetime import datetime, date
import os
from io import BytesIO

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Payments Tracker (USD)",
    page_icon="💵",
    layout="wide"
)

# ------------------ Header ------------------
st.markdown("""
<div style="padding: 20px; border-radius: 10px; background: linear-gradient(90deg,#4CAF50,#66BB6A);">
    <h1 style="color: white; text-align:center; margin:0;">💵 Payments Registry Dashboard</h1>
    <p style="color:white; text-align:center; margin:0;">Track payments, services and clients in a modern and visual dashboard</p>
</div>
""", unsafe_allow_html=True)

# ------------------ Constants ------------------
EXCEL_FILE = "payments_records.xlsx"
SHEET = "Records"
COLUMNS = ["Timestamp", "Client", "Service", "Amount Paid (USD)"]

# ------------------ Utility Functions ------------------
@st.cache_data
def load_data():
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET, engine="openpyxl")
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
        df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET, engine="openpyxl")
        df = pd.concat([df, new], ignore_index=True)
    else:
        df = new
        
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name=SHEET, index=False)

def usd(x):
    return f"${x:,.2f}"

# ------------------ Load Data ------------------
df = load_data()

# ------------------ Layout ------------------
left, right = st.columns([1, 2])

# ======================================================
# LEFT - FORM (Now visual and beautiful)
# ======================================================
with left:
    
    st.markdown("## 📝 Add New Payment")

    st.markdown("""
    <div style="padding:15px; background:#ffffff; border-radius:10px; 
    border:1px solid #e0e0e0; box-shadow:2px 2px 8px rgba(0,0,0,0.05);">
    """, unsafe_allow_html=True)

    with st.form("add_payment", clear_on_submit=True):
        client = st.text_input("Client name:")
        service = st.text_area("Service description:")
        amount = st.number_input("Amount paid (USD):", min_value=0.0, step=1.0)
        submit = st.form_submit_button("💾 Save Payment")

    st.markdown("</div>", unsafe_allow_html=True)

    if submit:
        if not client or not service:
            st.error("Please fill in all fields")
        else:
            save_record(client, service, amount)
            st.success("Payment saved successfully 🎉")
            st.rerun()

# ======================================================
# RIGHT - DASHBOARD + REPORTS (Now much more visual)
# ======================================================
with right:

    st.markdown("## 📊 Dashboard & Reports")

    if df.empty:
        st.info("No records yet. Add a payment to begin.")
        st.stop()

    df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date
    df["YearMonth"] = pd.to_datetime(df["Timestamp"]).dt.to_period("M").astype(str)

    # Filters box
    st.markdown("""
    <div style="padding:15px; background:white; border-radius:10px; border:1px solid #ddd;">
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    with f1:
        date_range = st.date_input("📅 Date range:", (min_date, max_date))
    with f2:
        client_filter = st.selectbox("👤 Filter by client:", ["All"] + df["Client"].unique().tolist())
    with f3:
        service_filter = st.selectbox("🛠 Filter by service:", ["All"] + df["Service"].unique().tolist())

    st.markdown("</div>", unsafe_allow_html=True)

    # Mask
    mask = (df["Date"] >= date_range[0]) & (df["Date"] <= date_range[1])
    if client_filter != "All":
        mask &= df["Client"] == client_filter
    if service_filter != "All":
        mask &= df["Service"] == service_filter

    filtered = df[mask]

    # KPI CARDS
    st.markdown("### 📌 Key Metrics")

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Total (USD)", usd(filtered["Amount Paid (USD)"].sum()))
    k2.metric("Records", len(filtered))
    k3.metric("Average Ticket", usd(filtered["Amount Paid (USD)"].mean() if len(filtered) > 0 else 0))

    today = date.today()
    current_ym = f"{today.year}-{today.month:02d}"
    month_total = df[df["YearMonth"] == current_ym]["Amount Paid (USD)"].sum()

    k4.metric(f"This Month ({current_ym})", usd(month_total))

    # TABLE
    st.markdown("### 📄 Filtered Records")
    st.dataframe(filtered, use_container_width=True)

    # CHARTS
    st.markdown("### 📈 Visual Charts")

    chart1, chart2 = st.columns(2)

    with chart1:
        st.markdown("#### 🔹 Total by Client")
        st.bar_chart(filtered.groupby("Client")["Amount Paid (USD)"].sum())

    with chart2:
        st.markdown("#### 🔹 Total by Service")
        st.bar_chart(filtered.groupby("Service")["Amount Paid (USD)"].sum())

    # Monthly Summary
    st.markdown("#### 📆 Monthly Summary (USD)")
    st.line_chart(df.groupby("YearMonth")["Amount Paid (USD)"].sum())


