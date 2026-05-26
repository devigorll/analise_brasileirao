import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Brasileirão 2024",
    layout="wide"
)

df = pd.read_csv("../data/base_tratada.csv")
tc = pd.read_csv("../data/classificacao.csv")
te = pd.read_csv("../data/tabela_times.csv")

media_gols = np.mean(df["GOLS POR JOGO"])
media_gols_mandante = np.mean(df["GOLS MANDANTE"])
media_gols_visitante = np.mean(df["GOLS VISITANTE"])

tc.index = range(1, len(tc) + 1)
tc.index.name = "Posição"

with st.sidebar:
    st.title("Projeto Estrutura de Dados")
    st.subheader("Desenvolvido por:\nIgor Cruz e Guilherme Santos")
    st.divider()
    st.subheader("Filtros")

    filtro_time = st.selectbox("Selecione o time para análise:", options=["Todos"] + sorted(df["MANDANTE"].unique()))



st.title("⚽🏆 Análise Brasileirão 2024")
st.text("Projeto final Estrutura de Dados - Análise do Campeonato Brasileiro 2024")

st.divider()

left, center, right = st.columns([1.2, 3.5, 2.5],gap="large")

if filtro_time == "Todos":

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

        st.subheader("⏰ Gols por Período do Jogo")

        gols_por_periodo = (df.groupby("PERIODO JOGO")["GOLS POR JOGO"].count().reset_index())

        st.area_chart(data=gols_por_periodo, x="PERIODO JOGO", y="GOLS POR JOGO", use_container_width=True, height=350, color = "blue")

elif filtro_time == "Ath Paranaense":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )
elif filtro_time == "Atl Goianiense":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Atlético Mineiro":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Bahia":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Botafogo (RJ)":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Corinthians":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Criciúma":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Cruzeiro":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )    

elif filtro_time == "Cuiabá":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )  

elif filtro_time == "Flamengo":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Fluminense":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Fortaleza":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Grêmio":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Internacional":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Juventude":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Palmeiras":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "RB Bragantino":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "São Paulo":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Vasco da Gama":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )

elif filtro_time == "Vitória":

    media_gols_time = te[te["TIME"] == filtro_time]["MEDIA GOLS"].values[0]
    gols_feitos = te[te["TIME"] == filtro_time]["GOLS FEITOS"].values[0]
    gols_sofridos = te[te["TIME"] == filtro_time]["GOLS SOFRIDOS"].values[0]

    with left:

        st.metric(label="Média de gols por partida", value=f"{media_gols_time:.2f}")

        st.metric(label="Gols feitos", value=f"{gols_feitos}")

        st.metric(label="Gols sofridos", value=f"{gols_sofridos}")

    with center:

        st.subheader(f"🏆 Classificação - {filtro_time}")

        st.dataframe(tc[tc["TIME"] == filtro_time], use_container_width=True, )

    with right:

        st.subheader("📊 Vitórias Mandante x Visitante")

        time_filtrado = te[te["TIME"] == filtro_time]

        grafico = pd.DataFrame({
            "RESULTADO": ["VITÓRIAS", "EMPATES", "DERROTAS"],
            "TOTAL": [
                time_filtrado["VITORIAS"].values[0],
                time_filtrado["EMPATES"].values[0],
                time_filtrado["DERROTAS"].values[0]
            ]
        })

        st.bar_chart(
            data=grafico,
            x="RESULTADO",
            y="TOTAL",
            use_container_width=True
        )