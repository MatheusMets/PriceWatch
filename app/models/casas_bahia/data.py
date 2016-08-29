# coding: utf-8
import scrapy
import re


class SpiderCasasBahia(scrapy.Spider):

  name = 'spider'
  start_urls = ['http://www.casasbahia.com.br/Informatica/Notebook/Notebook-Positivo-Stilo-One-XC3550-com-Intel-Atom-Quad-Core-2GB-32GB-SSD-Leitor-de-Cartoes-HDMI-Bluetooth-Webcam-LED-14-e-Windows-10-9233539.html']
  download_delay = 1.5

  def get_storage(response):
    ssd = response.xpath('//*[@class="Memoria-Flash--SSD-"]/dd/text()')
    hd = response.xpath('//*[@class="Disco-rigido--HD-"]/dd/text()')

    # se não tiver ssd
    if (re.search('N.o se aplica', ssd) == None):
      return ['hd', hd]

    # se não tiver hd
    elif (re.search('N.o se aplica', hd) == None):
      return ['ssd', ssd]

    return None


  def get_availability(response):
    price = response.xpath('//*[@class="sale price"]/text()')
    price = re.sub('\,', '.', price)
    try:
      float(price)
      return [True, price]
    except ValueError:
      return [False, 0]

  def get_brand(product_name):
    data_list = DataList()
    brands_regex = data_list.get_brands_regex()
    return re.search(brands_regex, product_name)

  def is_valid_brand(self, string=""):
    return (string.lower() in get_brands_list())

  def get_brands_regex():
    return '/' + '|'.join(map(str, get_brands_list())) + '/'

  def get_brands_list():
    return ['acer', 'asus', 'apple', 'dell', 'hp', 'samsung']



  def parse(self, response):
    data = {}
    data['name'] = response.xpath('//*[@itemprop="name"]/text()')
    print data

    data['color'] = response.xpath('//*[@class="Cor"]/dd/text()')
    print data

    data['display_size'] = response.xpath('//*[@class="Tamanho-da-tela even"]/dd/text()')
    print data

    data['display_feature'] = response.xpath('//*[@class="Tipo-de-tela even"]/dd/text()')
    print data

    data['processor'] = response.xpath('//*[@class="Processador even"]/dd/text()')
    print data

    data['graphics_processor'] = response.xpath('//*[@class="Placa-de-video even"]/dd/text()')
    print data

    data['operating_system'] = response.xpath('//*[@class="Sistema-operacional"]/dd/text()')
    print data

    data['ram_memory'] = response.xpath('//*[@class="Memoria-RAM even"]/dd/text()')
    print data

    data['url'] = response.url
    print data

    data['image_url'] = response.xpath('//*[@itemprop="image"]//image/@src').extract()
    print data

    storage = get_storage(response)
    if storage != None: data['storage'], data['storage_type'] = storage
    print data

    money_value = get_availability(response)
    data['available'], data['price'] = money_value
    print data

    data['brand'] = get_brand(data['name'])
    print data

    yield data


