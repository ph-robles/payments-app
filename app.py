import streamlit as st
import pandas as pd
from datetime import datetime, date
import os
from io import BytesIO

# ----------------- Configuração da página -----------------
st.set_page_config(page_title="Payments Tracker (USD)", page_icon="💵", layout="wide")
st.title("💵 Registro de Pagamentos (USD)")
st.caption("Registre Cliente, Serviço e Valor (USD). Gere relatórios por período, mês e gráficos por Cliente/Serviço.")

ARQUIVO_EXCEL = "payments_records.xlsx"
ABA = "Records"

COLUNAS_PADRAO = ["Data/Hora", "Cliente", "Serviço", "Valor Pago (USD)"]

# ----------------- Funções utilitárias -----------------
@st.cache_data
def carregar_dados(caminho=ARQUIVO_EXCEL, aba=ABA) -> pd.DataFrame:
    """Carrega os dados do Excel (ou retorna DataFrame vazio com colunas padrão)."""
    if os.path.exists(caminho):
        try:
            df = pd.read_excel(caminho, sheet_name=aba, engine="openpyxl")
            for c in COLUNAS_PADRAO:
                if c not in df.columns:
                    df[c] = None
            df = df[COLUNAS_PADRAO].copy()
            # Normaliza tipos
            df["Data/Hora"] = pd.to_datetime(df["Data/Hora"], errors="coerce")
            df["Valor Pago (USD)"] = pd.to_numeric(df["Valor Pago (USD)"], errors="coerce")
            return df
        except Exception as e:
            st.warning(f"Não foi possível ler o Excel existente ({e}). Um novo será criado ao salvar.")
    return pd.DataFrame(columns=COLUNAS_PADRAO)

def salvar_registro(cliente: str, servico: str, valor: float, caminho=ARQUIVO_EXCEL, aba=ABA):
    """Anexa um registro ao Excel, criando arquivo/aba se necessário."""
    novo = pd.DataFrame([{
        "Data/Hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Cliente": cliente.strip(),
        "Serviço": servico.strip(),
        "Valor Pago (USD)": float(valor)
    }])

    if os.path.exists(caminho):
        try:
            existente = pd.read_excel(caminho, sheet_name=aba, engine="openpyxl")
            df_final = pd.concat([existente, novo], ignore_index=True)
        except Exception:
            df_final = novo.copy()
    else:
        df_final = novo.copy()

    with pd.ExcelWriter(caminho, engine="openpyxl", mode="w") as writer:
        df_final.to_excel(writer, sheet_name=aba, index=False)

    return df_final

def fmt_usd(x):
    """Formata número em USD: $1,234.56. Retorna '-' se inválido."""
    try:
        return f"${x:,.2f}"
    except Exception:
        return "-"

def to_excel_bytes(df: pd.DataFrame) -> bytes:
    """Converte um DataFrame em bytes de Excel (xlsx) para download."""
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Filtered")
    buffer.seek(0)
    return buffer.getvalue()

# ----------------- Colunas / Layout -----------------
col_form, col_relatorios = st.columns([1, 2], gap="large")

# ----------------- Formulário (Cadastro) -----------------
with col_form:
    st.subheader("Cadastrar novo pagamento")
    with st.form("form_registro", clear_on_submit=True):
        cliente = st.text_input("Cliente*", placeholder="Ex.: Maria Silva")
        servico = st.text_area("Serviço realizado*", placeholder="Ex.: Manutenção preventiva no site XYZ")
        valor = st.number_input("Valor pago (USD)*", min_value=0.0, step=1.0, format="%.2f", help="Informe em dólares americanos (USD).")
        enviado = st.form_submit_button("Salvar registro ✅")

    if enviado:
        erros = []
        if not cliente.strip():
            erros.append("Informe o **nome do cliente**.")
        if not servico.strip():
            erros.append("Descreva o **serviço realizado**.")
        if valor is None or valor < 0:
            erros.append("O **valor** precisa ser zero ou positivo.")

        if erros:
            for e in erros:
                st.error(e)
        else:
            salvar_registro(cliente, servico, valor)
            st.success("Registro salvo com sucesso! 🎉")
            carregar_dados.clear()
            st.rerun()

# ----------------- Dados / Relatórios -----------------
with col_relatorios:
    st.subheader("Relatórios e Filtros")

    df = carregar_dados()
    if df.empty:
        st.info("Nenhum registro ainda. Use o formulário ao lado para começar.")
    else:
        # Preparação de campos auxiliares
        df["Data"] = pd.to_datetime(df["Data/Hora"], errors="coerce").dt.date
        df["AnoMes"] = pd.to_datetime(df["Data/Hora"], errors="coerce").dt.to_period("M").astype(str)

        # ----- Filtros (sidebar local) -----
        f1, f2, f3 = st.columns([1.2, 1, 1])

        # Período padrão: do primeiro registro ao último
        min_data = df["Data"].min() or date.today()
        max_data = df["Data"].max() or date.today()

        with f1:
            data_inicial, data_final = st.date_input(
                "Período",
                value=(min_data, max_data),
                min_value=min_data,
                max_value=max_data
            )

        # Filtros opcionais por Cliente/Serviço
        with f2:
            clientes_unicos = sorted([c for c in df["Cliente"].dropna().unique()])
            clientes_sel = st.multiselect("Cliente (opcional)", options=clientes_unicos, default=[])

        with f3:
            servicos_unicos = sorted([s for s in df["Serviço"].dropna().unique()])
            servicos_sel = st.multiselect("Serviço (opcional)", options=servicos_unicos, default=[])

        # Aplica filtros
        mask = (df["Data"] >= data_inicial) & (df["Data"] <= data_final)
        if clientes_sel:
            mask &= df["Cliente"].isin(clientes_sel)
        if servicos_sel:
            mask &= df["Serviço"].isin(servicos_sel)

        df_filtrado = df.loc[mask].copy()

        # ----- KPIs -----
        c1, c2, c3, c4 = st.columns(4)
        total_periodo = df_filtrado["Valor Pago (USD)"].sum(skipna=True)
        qtd_registros = len(df_filtrado)
        media_registro = df_filtrado["Valor Pago (USD)"].mean(skipna=True) if qtd_registros > 0 else 0.0

        # Total do mês atual (independente do filtro de período)
        hoje = date.today()
        ano_mes_atual = f"{hoje.year}-{hoje.month:02d}"
        total_mes_atual = df.loc[df["AnoMes"] == ano_mes_atual, "Valor Pago (USD)"].sum(skipna=True)

        c1.metric("Total no período (USD)", fmt_usd(total_periodo))
        c2.metric("Registros no período", f"{qtd_registros}")
        c3.metric("Ticket médio (USD)", fmt_usd(media_registro))
        c4.metric(f"Total do mês atual ({ano_mes_atual})", fmt_usd(total_mes_atual))

        st.divider()

        # ----- Tabela filtrada -----
        st.markdown("### 📄 Registros (filtrados)")
        mostrar = df_filtrado[COLUNAS_PADRAO].copy()
        # Formatar valores
        mostrar["Valor Pago (USD)"] = mostrar["Valor Pago (USD)"].apply(lambda x: fmt_usd(x) if pd.notnull(x) else "-")
        st.dataframe(mostrar, use_container_width=True, hide_index=True)

        # Downloads
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            # Excel completo
            with open(ARQUIVO_EXCEL, "rb") as f:
                st.download_button(
                    label="📥 Baixar Excel (completo)",
                    data=f,
                    file_name=ARQUIVO_EXCEL,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
        with col_dl2:
            # Excel filtrado
            bytes_filtrado = to_excel_bytes(df_filtrado[COLUNAS_PADRAO])
            st.download_button(
                label="📥 Baixar Excel (filtrado)",
                data=bytes_filtrado,
                file_name="payments_filtered.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

        st.divider()

        # ----- Gráficos: por Cliente e por Serviço -----
        st.markdown("### 📊 Gráficos")

        gc, gs = st.columns(2)
        # Por Cliente
        with gc:
            st.markdown("**Total por Cliente (USD)**")
            grp_cli = (df_filtrado
                       .groupby("Cliente", dropna=True)["Valor Pago (USD)"]
                       .sum()
                       .sort_values(ascending=False)
                      )
            if grp_cli.empty:
                st.info("Sem dados para este gráfico.")
            else:
                st.bar_chart(grp_cli, use_container_width=True)

        # Por Serviço
        with gs:
            st.markdown("**Total por Serviço (USD)**")
            grp_srv = (df_filtrado
                       .groupby("Serviço", dropna=True)["Valor Pago (USD)"]
                       .sum()
                       .sort_values(ascending=False)
                      )
            if grp_srv.empty:
                st.info("Sem dados para este gráfico.")
            else:
                st.bar_chart(grp_srv, use_container_width=True)

        st.divider()

        # ----- Resumo mensal (soma do mês) -----
        st.markdown("### 🗓️ Resumo mensal (USD)")
        resumo_mensal = (df
                         .groupby("AnoMes", dropna=True)["Valor Pago (USD)"]
                         .sum()
                         .reset_index()
                         .sort_values("AnoMes"))
        if resumo_mensal.empty:
            st.info("Ainda não há dados suficientes para o resumo mensal.")
        else:
            col_m1, col_m2 = st.columns([1, 2])
            with col_m1:
                # Mostra tabela com formatação
                tmp = resumo_mensal.copy()
                tmp["Total (USD)"] = tmp["Valor Pago (USD)"].apply(fmt_usd)
                st.dataframe(tmp[["AnoMes", "Total (USD)"]], use_container_width=True, hide_index=True, height=280)
            with col_m2:
                chart_df = resumo_mensal.set_index("AnoMes")["Valor Pago (USD)"]
                st.line_chart(chart_df, use_container_width=True)

st.caption("Dica: salve o arquivo .xlsx numa pasta sincronizada (OneDrive/Google Drive/SharePoint) para backup automático.")