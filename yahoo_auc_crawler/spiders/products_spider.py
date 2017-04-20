import scrapy
from scrapy import signals

class ProductsSpider(scrapy.Spider):
  name = "products"

  start_urls = ['https://auctions.yahoo.co.jp/seller/tolvio0256?ngram=1']

  def parse(self, response):
    for href in response.css('.a1wrp>h3>a::attr(href)').extract():
      yield scrapy.Request(response.urljoin(href), callback = self.parse_product)

    next_page = response.css('.next>a::attr(href)').extract_first()
    if next_page is not None:
      next_page = response.urljoin(next_page)
      yield scrapy.Request(next_page, callback = self.parse)

  def parse_product(self, response):
    def extract_with_css(query):
      return response.css(query).extract_first().strip()

    yield {
      'title': extract_with_css('h1.ProductTitle__text::text')
    }
