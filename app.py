import streamlit as st
import pandas as pd
from datetime import datetime, date
import os
from io import BytesIO

# ----------------- Page Config -----------------
st.set_page_config(page_title="Payments Tracker (USD)", page_icon="💵", layout="wide")
st.title("💵 Payments Registry (USD)")
st.caption("Register Clients, Services and Payments. Generate reports by date range, month, and graphs by Client/Service.")

EXCEL_FILE = "payments_records.xlsx"
SHEET = "Records"

COLUMNS = ["Timestamp", "Client", "Service", "Amount Paid (USD)"]

# ----------------- Utility Functions -----------------
@st.cache_data
def load_data(path=EXCEL_FILE, sheet=SHEET) -> pd.DataFrame:
    """Load data from Excel or return empty DataFrame."""
    if os.path.exists(path):
        try:
            df = pd.read_excel(path, sheet_name=sheet, engine="openpyxl")
            for col in COLUMNS:
                if col not in df.columns:
                    df[col] = None
            df = df[COLUMNS].copy()
            df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
            df["Amount Paid (USD)"] = pd.to_numeric(df["Amount Paid (USD)"], errors="coerce")
            return df
        except Exception as e:
            st.warning(f"Unable to read existing Excel file ({e}). A new one will be created when saving.")
    return pd.DataFrame(columns=COLUMNS)

def save_record(client: str, service: str, amount: float, path=EXCEL_FILE, sheet=SHEET):
    """Append a new record to the Excel file."""
    new = pd.DataFrame([{
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Client": client.strip(),
        "Service": service.strip(),
        "Amount Paid (USD)": float(amount)
    }])

    if os.path.exists(path):
        try:
            existing = pd.read_excel(path, sheet_name=sheet, engine="openpyxl")
            df_final = pd.concat([existing, new], ignore_index=True)
        except Exception:
            df_final = new.copy()
    else:
        df_final = new.copy()

    with pd.ExcelWriter(path, engine="openpyxl", mode="w") as writer:
        df_final.to_excel(writer, sheet_name=sheet, index=False)

    return df_final

def usd_format(x):
    """Return formatted USD value."""
    try:
        return f"${x:,.2f}"
    except:
        return "-"

def df_to_excel_bytes(df: pd.DataFrame) -> bytes:
    """Convert a DataFrame to Excel bytes for download."""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Filtered")
    buffer.seek(0)
    return buffer.getvalue()

# ----------------- Layout -----------------
left, right = st.columns([1, 2], gap="large")

# ----------------- Registration Form -----------------
with left:
    st.subheader("New Payment Entry")

    with st.form("form_entry", clear_on_submit=True):
        client = st.text_input("Client*", placeholder="Ex: Maria Smith")
        service = st.text_area("Service Provided*", placeholder="Ex: Preventive maintenance at site XYZ")
        amount = st.number_input("Amount Paid (USD)*", min_value=0.0, step=1.0, format="%.2f")

        submitted = st.form_submit_button("Save Record ✅")

    if submitted:
        errors = []
        if not client.strip():
            errors.append("Please enter the client's name.")
        if not service.strip():
            errors.append("Please describe the service.")
        if amount is None or amount < 0:
            errors.append("Amount must be zero or greater.")

        if errors:
            for e in errors:
                st.error(e)
        else:
            save_record(client, service, amount)
            st.success("Record saved successfully! 🎉")
            load_data.clear()
            st.rerun()

# ----------------- Reports -----------------
with right:
    st.subheader("Reports & Filters")

    df = load_data()

    if df.empty:
        st.info("No records yet. Use the form on the left to add entries.")
    else:
        df["Date"] = pd.to_datetime(df["Timestamp"], errors="coerce").dt.date
        df["YearMonth"] = pd.to_datetime(df["Timestamp"], errors="coerce").dt.to_period("M").astype(str)

        # -------- Filters --------
        f1, f2, f3 = st.columns([1.2, 1, 1])

        min_date = df["Date"].min()
        max_date = df["Date"].max()

        with f1:
            start_date, end_date = st.date_input(
                "Date Range",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )

        with f2:
            clients_unique = sorted(df["Client"].dropna().unique().tolist())
            selected_clients = st.multiselect("Client (optional)", options=clients_unique, default=[])

        with f3:
            services_unique = sorted(df["Service"].dropna().unique().tolist())
            selected_services = st.multiselect("Service (optional)", options=services_unique, default=[])

        # Apply filters
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        if selected_clients:
            mask &= df["Client"].isin(selected_clients)
        if selected_services:
            mask &= df["Service"].isin(selected_services)

        df_filtered = df.loc[mask].copy()

        # -------- KPIs --------
        k1, k2, k3, k4 = st.columns(4)
        total_period = df_filtered["Amount Paid (USD)"].sum()
        count_records = len(df_filtered)
        avg_ticket = df_filtered["Amount Paid (USD)"].mean() if count_records > 0 else 0.0

        # Current month total
        today = date.today()
        ym_current = f"{today.year}-{today.month:02d}"
        total_this_month = df.loc[df["YearMonth"] == ym_current, "Amount Paid (USD)"].sum()

        k1.metric("Total in Period (USD)", usd_format(total_period))
        k2.metric("Records in Period", f"{count_records}")
        k3.metric("Average Ticket (USD)", usd_format(avg_ticket))
        k4.metric(f"Total This Month ({ym_current})", usd_format(total_this_month))

        st.divider()

        # -------- Filtered Table --------
        st.markdown("### 📄 Filtered Records")
        table = df_filtered[COLUMNS].copy()
        table["Amount Paid (USD)"] = table["Amount Paid (USD)"].apply(usd_format)

        st.dataframe(table, use_container_width=True, hide_index=True)

        # -------- Downloads --------
        dl1, dl2 = st.columns(2)

        with dl1:
            with open(EXCEL_FILE, "rb") as f:
                st.download_button(
                    "📥 Download Full Excel",
                    data=f,
                    file_name=EXCEL_FILE,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        with dl2:
            filtered_bytes = df_to_excel_bytes(df_filtered[COLUMNS])
            st.download_button(
                "📥 Download Filtered Excel",
                data=filtered_bytes,
                file_name="filtered_records.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.divider()

        # -------- Charts --------
        st.markdown("### 📊 Charts")

        ch1, ch2 = st.columns(2)

        with ch1:
            st.markdown("**Total by Client (USD)**")
            grp_client = df_filtered.groupby("Client")["Amount Paid (USD)"].sum().sort_values(ascending=False)
            if grp_client.empty:
                st.info("No data available for this chart.")
            else:
                st.bar_chart(grp_client)

        with ch2:
            st.markdown("**Total by Service (USD)**")
            grp_service = df_filtered.groupby("Service")["Amount Paid (USD)"].sum().sort_values(ascending=False)
            if grp_service.empty:
                st.info("No data available for this chart.")
            else:
                st.bar_chart(grp_service)

        st.divider()

        # -------- Monthly Summary --------
        st.markdown("### 🗓️ Monthly Summary (USD)")
        monthly = df.groupby("YearMonth")["Amount Paid (USD)"].sum().reset_index()

        if monthly.empty:
            st.info("Not enough data for monthly summary.")
        else:
            cm1, cm2 = st.columns([1, 2])

            with cm1:
                tmp = monthly.copy()
                tmp["Total (USD)"] = tmp["Amount Paid (USD)"].apply(usd_format)
                st.dataframe(tmp[["YearMonth", "Total (USD)"]], hide_index=True)

            with cm2:
                monthly_chart = monthly.set_index("YearMonth")["Amount Paid (USD)"]
                st.line_chart(monthly_chart)

st.caption("Tip: Use cloud folders (OneDrive, Google Drive, SharePoint) to automatically back up your Excel file.")
