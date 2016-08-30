# -*- coding: utf-8 -*-

from lxml import html
import json
import requests

class HttpClient:

  def get_request(url):
    return requests.get(url)

  def parse_result(content):
    return html.fromstring(content)

  def get_element_by_xpath(tree, xpath_string):
    return tree.xpath(xpath_string)[0].strip()
