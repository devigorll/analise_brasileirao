import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Brasileirão 2024",
    layout="wide"
)

df = pd.read_csv("base_tratada.csv")
tc = pd.read_csv("classificacao.csv")

media_gols = np.mean(df["GOLS POR JOGO"])
media_gols_mandante = np.mean(df["GOLS MANDANTE"])
media_gols_visitante = np.mean(df["GOLS VISITANTE"])

tc.index = range(1, len(tc) + 1)
tc.index.name = "Posição"

with st.sidebar:
    st.title("Projeto Estrutura de Dados")
    st.text("Defiinir quais filtros deverão ser aplicados para a análise dos dados.")
    st.divider()
    st.subheader("Filtros")

    st.selectbox("Selecione o time para análise:", options=["Todos"] + sorted(df["MANDANTE"].unique()))

st.title("⚽ Análise Brasileirão 2024 - EM DESENVOLVIMENTO")
st.text("Testar outros tipos de layouts, gráficos e métricas para apresentar os dados de forma mais clara e visualmente atraente.")

st.divider()

left, center, right = st.columns([1.2, 3.5, 2.5],gap="large")

with left:

    st.metric(label="Média de gols por partida", value=f"{media_gols:.2f}")

    st.metric(label="Média de gols mandante", value=f"{media_gols_mandante:.2f}")

    st.metric(label="Média de gols visitante", value=f"{media_gols_visitante:.2f}")

with center:

    st.subheader("🏆 Classificação")

    st.dataframe(tc, use_container_width=True, height=720)

with right:

    st.subheader("📊 Vitórias Mandante x Visitante")

    vitorias = df["VITORIA"].value_counts()

    st.bar_chart(vitorias, use_container_width=True, height=300, color = "blue")

    st.divider()

    st.subheader("⏰ Gols por horário")

    gols_por_hora = (df.groupby("HORA")["GOLS POR JOGO"].mean().reset_index())

    st.area_chart(data=gols_por_hora, x="HORA", y="GOLS POR JOGO", use_container_width=True, height=350, color = "blue")