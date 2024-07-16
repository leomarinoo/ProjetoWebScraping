import pandas as pd
from datetime import datetime
import sqlite3

#Definir caminho para o arquivo json
df = pd.read_json('../data/data.jsonl', lines=True)

#Adicionar a coluna _source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

#Adicionar a coluna _data_coleta com a hora e data atual
df['_data_coleta'] = datetime.now()

#Tratar os valores nulos para colunas numericas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_prices_centavos'] = df['old_prices_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float) 

#Remover os parenteses da coluna 'reviews_amount'
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '',regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int) 

#Tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_prices_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

#Remover colunas antigas de preços 
df.drop(columns=['old_price_reais', 'old_prices_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

#Conectar ao banco de dados SQLite3 
conn= sqlite3.connect('../data/quotes.db') 

#Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

#Fechar a conexão com o banco de dados
conn.close() 

print(df.head()) 