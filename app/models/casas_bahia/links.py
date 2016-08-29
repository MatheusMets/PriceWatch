# coding: utf-8
import scrapy

class SpiderCasasBahia(scrapy.Spider):

  name = 'spider'
  start_urls = ['http://www.casasbahia.com.br/Informatica/Notebook/?Filtro=C56_C57&paginaAtual=6&ComparacaoProdutos=&AdicionaListaCasamento=']
  download_delay = 1.5

  def parse(self, response):
    for vitrine in response.css('.hproduct'):
      yield vitrine.css('a::attr("href")').extract_first()

  link_next = response.css('li.next a::attr("href")').extract_first()
    if link_next:
      yield scrapy.Request(link_next)
