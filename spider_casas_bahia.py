<<<<<<< HEAD
# coding: utf-8 
=======
# coding: utf-8
>>>>>>> dcd5983e4dc16d30105621a2f1fbe1f01ee3674d
import scrapy

# RODE ESTE ARQUIO DA SEGUINTE FORMA :
# scrapy runspider spider_casas_banhia.py -o tabela_links.csv



class SpiderCasasBahia(scrapy.Spider):
    name = 'spider'
    start_urls = [
<<<<<<< HEAD
        'http://www.casasbahia.com.br/Informatica/Notebook/?Filtro=C56_C57'
    ]
    download_delay = 1.5
    
=======
        'http://www.casasbahia.com.br/Informatica/Notebook/?Filtro=C56_C57&paginaAtual=6&ComparacaoProdutos=&AdicionaListaCasamento='
    ]
    download_delay = 1.5

>>>>>>> dcd5983e4dc16d30105621a2f1fbe1f01ee3674d

    def parse(self, response):
        for vitrine in response.css('.hproduct'):
            yield {
                #'Descrição': vitrine.css('strong::text').extract_first(),
<<<<<<< HEAD
		'Descrição': vitrine.css('a::attr("title")').extract_first(),
                'link': vitrine.css('a::attr("href")').extract_first(),
            }
	link_next = response.css('ul.ListaPaginas a::attr("href")').extract_first()
=======
		        'Descrição': vitrine.css('a::attr("title")').extract_first(),
                'link': vitrine.css('a::attr("href")').extract_first(),
            }
	link_next = response.css('li.next a::attr("href")').extract_first()
>>>>>>> dcd5983e4dc16d30105621a2f1fbe1f01ee3674d
        if link_next:
            yield scrapy.Request(link_next)
