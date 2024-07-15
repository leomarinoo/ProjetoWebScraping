import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    #Request do site
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    #Variavel de pagina inicial do site e maximo de paginas para não tomar um banimento do site
    page_count = 1
    max_pages = 10

    #Pegando o bloco dentro do site
    def parse(self, response):
        products = response.css('div.ui-search-result__content') #54 produtos no total

        #Categorizando produtos
        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall() 

            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(), 
                'nome': product.css('h2.ui-search-item__title::text').get(),
                'old_price_reais': prices[0] if len(prices) > 0 else None,
                'old_prices_centavos': cents[0] if len(cents) > 0 else None,
                'new_price_reais': prices[1] if len(prices) > 1 else None,
                'new_price_centavos': cents[1] if len(cents) > 1 else None,
                'reviews_rating_number': product.css('span.ui-search-reviews__rating-number::text').get(),
                'reviews_amount': product.css('span.ui-search-reviews__amount::text').get()
            } 

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse) 


    

