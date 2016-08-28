import scrapy


def first(sel, xpath):
    return sel.xpath(xpath).extract_first()


class KabumNotebooklLister(scrapy.Spider):
    name='Spider_Kabum'
    start_urls = ['http://www.kabum.com.br/computadores/notebooks-ultrabooks?ordem=5&limite=100&dep=04&sec=35&cat=&sub=&pagina=1&string=']

    def parse(self, response):
        for box_page in response.css(".listagem-box"):
            yield {
                'link': box_page.css('.listagem-titulo_descr a::attr(href)').extract_first(),
                'description': box_page.css('.listagem-titulo_descr a::text').extract_first(),
            }

