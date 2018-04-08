# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from urllib.parse import parse_qsl
import scrapy
import requests

class ProductsSpider(scrapy.Spider):
    name = "products"

    product_num = 0

    DETAIL_HTML = open('detail_format.html', 'r', encoding='utf8').read()
    MAX_INIT_PRICE = 8000

    def __init__(self, author_url=None, *args, **kwargs):
        super(ProductsSpider, self).__init__(*args, **kwargs)
        self.start_urls = [author_url]

    def parse(self, response):
        for href in response.css('.a1wrp>h3>a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_product, dont_filter=True)

        next_page = response.css('.next>a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_product(self, response):
        def extract_with_css(query):
            try:
                return response.css(query).extract_first().strip()
            except AttributeError:
                return ""

        category_link = response.css('.acMdNaviBox .st04>a::attr(href)').extract_first()
        query_string = urlparse(category_link).query
        category_str = parse_qsl(query_string)[0][1]

        init_price_str = response.css('.ProductDetail__body .l-right .ProductDetail__description::text').extract()[3].strip()
        init_price = int(init_price_str.replace(' 円', '').replace(',', ''))
        if init_price >= self.MAX_INIT_PRICE:
            return

        self.product_num += 1
        strnumber = str(self.product_num).zfill(4)

        all_info_lines = response.xpath("//*[@class='ProductExplanation']/descendant::text()").extract()
        init_line = 0
        end_line = 0
        for index, line in enumerate(all_info_lines):
            if '商品詳細' in line and init_line == 0:
                init_line = index + 1
            elif '支払詳細' in line:
                end_line = index
            elif '商品詳細' in line:
                init_line += 3
                end_line = index
                break
        product_info = "\n".join(all_info_lines[init_line:end_line])

        images = ['', '', '']
        image_urls = response.css('.ProductImage__inner>img::attr(src)').extract()
        if image_urls:
            for index, image_url in enumerate(image_urls):
                file_name = strnumber + '_' + str(index + 1) + '.jpg'
                file_path = 'images/' + file_name
                with open(file_path, 'wb') as handle:
                    img_response = requests.get(image_url, stream=True)
                    if not img_response.ok:
                        self.logger.error(img_response)
                    images[index] = file_name
                    for block in img_response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

        yield {
            'カテゴリ': category_str,
            'タイトル': extract_with_css('h1.ProductTitle__text::text'),
            '説明': self.DETAIL_HTML.replace('--商品詳細本文--', product_info),
            '開始価格': init_price,
            '即決価格': '',
            '個数': 1,
            '開催期間': 1,
            '終了時間': 21,
            '画像1': images[0],
            '画像２': images[1],
            '画像３': images[2],
            '商品発送元の都道府県': '東京都',
            '送料負担': '出品者',
            '代金支払い': '先払い',
            'Yahoo!かんたん決済': 'はい',
            '銀行振込': 'いいえ',
            'かんたん取引': 'はい',
            '銀行ID1': '',
            '銀行名1': '',
            '現金書留': 'いいえ',
            '商品代引': 'いいえ',
            '商品の状態': response.css('.ProductDetail__body .l-left .ProductDetail__description::text').extract()[0].strip(),
            '返品の可否': '返品可',
            '入札者評価制限': 'はい',
            '悪い評価の割合での制限': 'はい',
            '入札者認証制限': 'はい',
            '自動延長': 'はい',
            '早期終了': 'はい',
            '値下げ交渉': 'いいえ',
            '自動再出品': '3',
            '自動値下げ': 'いいえ',
            '自動値下げ価格変更率': '',
            '太字テキスト': 'いいえ',
            '背景色': 'いいえ',
            '贈答品アイコン': 'いいえ',
            '送料固定': 'はい',
            'ネコポス': 'いいえ',
            'ネコ宅急便コンパクト': 'いいえ',
            'ネコ宅急便': 'いいえ',
            'はこBOON': 'いいえ',
            'はこBOONmini': 'いいえ',
            '発送までの日数': '1日～2日',
            '配送方法1': '当店契約代行業者',
            '受け取り後決済サービス': 'いいえ',
            '海外発送': 'いいえ',
            'アフィリエイト': 'はい',
            'アフィリエイト報酬率': 1,
            '出品者情報開示前チェック': 'いいえ'
        }
