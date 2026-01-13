# 🔥 Análise de Incêndios e Queimadas (1998–2017)

Projeto de análise de dados sobre incêndios e queimadas no Brasil entre **1998 e 2017**, utilizando uma **arquitetura de Data Lake na AWS**, com processamento de dados via **AWS Glue**, armazenamento otimizado em **Parquet** e visualização no **Power BI**.

---

## 🎯 Objetivo
Construir um pipeline de dados completo para ingestão, tratamento e análise de dados históricos de queimadas, permitindo análises geográficas e temporais para apoio à tomada de decisão.

---

## 🏗️ Tecnologias Utilizadas
- **AWS S3** – Data Lake (camadas *raw* e *processed*)
- **AWS Glue Crawler** – Inferência automática de schema
- **AWS Glue Job (Python)** – ETL e tratamento dos dados
- **Apache Parquet** – Formato colunar otimizado
- **Power BI** – Visualização e dashboard
- **Python** – Processamento de dados

---

## 🔄 Pipeline de Dados

### 1️⃣ AWS Glue Crawler
Crawler executado para leitura dos dados brutos armazenados no S3 e criação automática do schema no **Glue Data Catalog**.

### 2️⃣ AWS Glue Job – Transformação
Job de ETL desenvolvido em Python para:
- Remoção de registros duplicados  
- Tratamento de valores nulos  
- Escrita dos dados tratados em formato **Parquet** na camada *processed*

### 3️⃣ Power BI – Dashboard Final
Dashboard construído a partir dos dados tratados, contendo:
- KPI de total de registros  
- Análise de incêndios por estado  
- Análise temporal de incêndios por ano  

---

## 📊 Principais Análises
- Distribuição de incêndios por estado
- Evolução anual das queimadas (1998–2017)
- Identificação de padrões e períodos críticos

---

## 🖼️ Evidências do Projeto
Os prints das execuções e do dashboard estão disponíveis na pasta `/images`:
- AWS Glue Crawler
- AWS Glue Job
- Schema no Glue Data Catalog
- Dashboard final no Power BI
