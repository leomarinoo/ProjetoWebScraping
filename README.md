# ProjetoWebScraping

Este README fornece uma visão geral clara e detalhada do projeto, incluindo a arquitetura, a estrutura de diretórios, as instruções de execução e uso dos comandos para Web Scraping e Pandas.

## Uma ETL em Python para Monitoramento de Preço dos Tenis de corrida masculino no Mercado Livre.

Solução em Python para estratégias de pricing.
Temos uma pipeline e uma ETL em Python que coleta, consolida e gera insights
sobre determinada cadeira de produtos até a pagina 10 do site. 

## Arquitetura
Um ETL em Python para Web Scraping

- Extração - Scrapy
- Transformação - Pandas
- Load - Python e SQLite3
- Dashboard - Streamlit 

### Diagrama

![arquitetura](/pics/diagrama.jpeg) 

### Estrutura de Diretórios
```plaintext
Pipeline ETL Python - Web Scraping/
├── ProjetoWebScraping/
│   ├── spiders/
│   │   └── mercadolivre.py
│   ├── items.py
│   ├── settings.py
├── transformacao/
│   ├── main.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md 
```

## Como usar

1- Para rodar o Web Scraping tem que escrever no terminal:

'''bash
scrapy crawl mercadolivre -o ../../data/data.jasonl
'''

2- Para rodar o pandas tem que escrever no terminal (dentro da pasta SRC):

'''bash
python transformacao/main.py
'''

### Extração

Início rápido 

Ler documentação - https://scrapy.org/ 