import pandas as pd
import streamlit as st
import sqlite3

#Conectar ao banco de dados SQLite3
conn= sqlite3.connect('../data/quotes.db')

#Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

#Fechar a conexão com o banco de dados
conn.close()

#Título da aplicação
st.title('Pesquisa de Mercado - Tênis esportivo masculino no Mercado Livre') 

#Melhorar o layout com colunas para KPIs
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3) 

#KPI 1 - Numero total de itens 
total_itens = df.shape[0]
col1.metric(label="Número total de itens", value=total_itens)

#KPI 2 - Numero de marcas unicas 
unique_brands = df['brand'].nunique()
col2.metric(label="Número de marcar únicas", value= unique_brands) 

#KPI 3 - Preço medio novo (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label="Preço médio novo (R$)", value= f"{average_new_price:.2f}") 

#Quais marcas são as mais encontradas até a página 10
st.subheader("Marcas mais encontradas até a 10ª página")
col1, col2 = st.columns([4, 2]) 
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False) 
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands) 

#Qual preço médio por marca
st.subheader("Preço médio por marca")
col1, col2 = st.columns([4, 2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

#Qual a satisfação por marca 
st.subheader("Satisfação por marca")
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand) 