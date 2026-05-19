# =========================================================
# IMPORTS
# =========================================================

import streamlit as st
import pandas as pd
import sys
import os

# =========================================================
# PATH CONFIG
# =========================================================

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# =========================================================
# IMPORT PIPELINE
# =========================================================

from app.pipeline import run_pipeline
from app.chat_agent import ask_agents

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Agente Autônomo de Inventário",

    page_icon="📦",

    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""

<style>

.main {
    background-color: #0E1117;
}

div[data-testid="metric-container"] {

    background-color: #1E1E1E;

    padding: 15px;

    border-radius: 10px;

    border: 1px solid #333333;
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🏭 Supply Chain AI")

    st.markdown("---")

    st.markdown("""

    ### Módulos do Sistema

    - Previsão de Demanda
    - Simulação de Inventário
    - Análise de Risco
    - Procurement Autônomo
    - Inteligência Logística
    - RAG Empresarial
    - Agentes IA

    """)

    st.markdown("---")

    st.info("""

    Sistema autônomo de gerenciamento
    de inventário impulsionado por IA.

    """)

# =========================================================
# TITLE
# =========================================================

st.title("📦 Agente Autônomo de Inventário")

st.caption(
    "Plataforma de decisão em supply chain impulsionada por IA"
)

# =========================================================
# RUN PIPELINE
# =========================================================

result = run_pipeline()

# =========================================================
# LOAD DATA
# =========================================================

agents = result["agents"]

simulation = agents["simulation"]

risk = agents["risk_analysis"]

decision = agents["replenishment_decision"]

# =========================================================
# TOP KPIs
# =========================================================

st.markdown("## 📊 KPIs Operacionais")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(

        "Estoque Final",

        simulation["final_stock"]
    )

with col2:

    st.metric(

        "Falta de Estoque",

        simulation["stockouts"]
    )

with col3:

    st.metric(

        "Pedidos Criados",

        len(simulation["orders"])
    )

with col4:

    st.metric(

        "Nível de Risco",

        risk["risk_level"]
    )

# =========================================================
# FORECAST + SIMULATION
# =========================================================

col1, col2 = st.columns(2)

# =========================================================
# FORECAST
# =========================================================

with col1:

    st.markdown("## 📈 Previsão de Demanda")

    st.info(

        f"Demanda Prevista: "
        f"{agents['forecast']['predicted_demand']} unidades"
    )

# =========================================================
# SIMULATION
# =========================================================

with col2:

    st.markdown("## 🏭 Simulação de Supply Chain")

    history_df = pd.DataFrame(

        simulation["stock_history"]
    )

    st.line_chart(

        history_df.set_index("day")["stock"]
    )

# =========================================================
# RISK + AUTONOMOUS DECISION
# =========================================================

col1, col2 = st.columns(2)

# =========================================================
# RISK ANALYSIS
# =========================================================

with col1:

    st.markdown("## ⚠️ Risco Operacional")

    st.error(

        f"Nível de Risco: "
        f"{risk['risk_level']}"
    )

    st.write(risk)

# =========================================================
# AUTONOMOUS PROCUREMENT
# =========================================================

with col2:

    st.markdown("## 🤖 Procurement Autônomo")

    st.success(

        f"Decisão: "
        f"{decision['decision']}"
    )

    st.write(decision)

# =========================================================
# MULTI AGENT WORKFLOW
# =========================================================

st.markdown("## 🔄 Fluxo de Trabalho Multi-Agente")

workflow_col1, workflow_col2, workflow_col3 = st.columns(3)

with workflow_col1:

    st.info("📊 Agente de Demanda")

    st.info("📦 Agente de Inventário")

with workflow_col2:

    st.info("💰 Agente de Custo")

    st.info("🚚 Agente de Logística")

with workflow_col3:

    st.info("⚠️ Agente de Risco")

    st.info("🤖 Agente de Procurement")

# =========================================================
# AI EXPLANATION
# =========================================================

st.markdown("## 🧠 Explicação de Negócio com IA")

st.write(result["explanation"])

# =========================================================
# CHAT SECTION
# =========================================================

st.markdown("## 💬 Chat com Agentes IA")

question = st.text_input(

    "Pergunte sobre inventário, risco, logística ou procurement:"
)

if question:

    answer = ask_agents(

        question,

        agents
    )

    st.success(answer)

# =========================================================
# EXPANDERS
# =========================================================

with st.expander("📚 Base de Conhecimento Empresarial"):

    st.markdown("""

    ### Fontes de Conhecimento

    - Políticas de supply chain
    - Procedimentos de inventário
    - Regras de logística
    - Diretrizes de procurement
    - Workflows operacionais

    """)

with st.expander("🧠 Decisões Históricas"):

    st.write(
        result["previous_decision"]
    )

with st.expander("🔍 Estado Completo do Agente"):

    st.json(agents)