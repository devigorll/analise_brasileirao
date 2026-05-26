# 📊 Projeto Estrutura de Dados: Análise Brasileirão 2024

![Status do Projeto](https://img.shields.io/badge/Status-Concluido-green)
![Linguagem](https://img.shields.io/badge/Language-Python-blue)
![Área](https://img.shields.io/badge/Area-Análise-purple)

Este projeto foi desenvolvido como trabalho final para a disciplina de **Estrutura de Dados**, no 2º semestre do curso de **Ciência de Dados** na **FATEC Jundiaí**.

O objetivo principal é realizar a Análise Exploratória de Dados (EDA), tratamento, manipulação e visualização estatística dos dados do Campeonato Brasileiro de Futebol de 2024 (Brasileirão), culminando em um dashboard interativo para apresentação dos resultados.

---

## 👥 Autores

* **Igor Cruz** - [GitHub](https://github.com/devigorll)
* **Guilherme Santos** - [GitHub](https://github.com/)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi construído utilizando o ecossistema Python voltado para Ciência de Dados:

* **Manipulação e Análise de Dados:** `pandas`, `numpy`, `csv`
* **Visualização Gráfica e Estatística:** `matplotlib`, `seaborn`
* **Interface do Usuário e Dashboard:** `streamlit`

---

## 📁 Estrutura do Projeto

O repositório está organizado com a seguinte estrutura de diretórios e arquivos:

```text
├── data/                  # Base de dados brutas e tratadas (arquivos .csv)
│   ├── base_tratada.csv
│   ├── base.csv
│   ├── classificacao.csv
│   └── tabela_times.csv
├── eda_limpeza/           # Notebooks dedicados à Análise Exploratória e Limpeza
│   └── tratamento.ipynb
├── src/                   # Código-fonte principal da aplicação
│   └── main.py            # Executável do Dashboard (Streamlit)
└── README.md              # Documentação do projeto
