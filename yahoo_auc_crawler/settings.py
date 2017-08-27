# -*- coding: utf-8 -*-

# Scrapy settings for yahoo_auc_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yahoo_auc_crawler'

SPIDER_MODULES = ['yahoo_auc_crawler.spiders']
NEWSPIDER_MODULE = 'yahoo_auc_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yahoo_auc_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
LOG_STDOUT = True
LOG_FILE = './scrapy_output.txt'
FEED_URI = 'products.csv'
FEED_EXPORT_ENCODING = 'utf-8'
FEED_FORMAT = 'csv'
FEED_EXPORT_FIELDS = ['カテゴリ', 'タイトル', '説明', '開始価格', '即決価格',
                      '個数', '開催期間', '終了時間', '画像1', '画像２', '画像３',
                      '商品発送元の都道府県', '送料負担', '代金支払い', 'Yahoo!かんたん決済',
                      '銀行振込', 'かんたん取引', '現金書留', '商品代引',
                      '商品の状態', '返品の可否', '入札者評価制限', '悪い評価の割合での制限',
                      '入札者認証制限', '自動延長', '早期終了', '値下げ交渉', '自動再出品',
                      '自動値下げ', '自動値下げ価格変更率', '太字テキスト', '背景色', '贈答品アイコン',
                      '送料固定', 'ネコポス', 'ネコ宅急便コンパクト', 'ネコ宅急便', 'はこBOON', 'はこBOONmini', '発送までの日数',
                      '配送方法1', '配送方法1全国一律価格', '受け取り後決済サービス', '海外発送',
                      'アフィリエイト', 'アフィリエイト報酬率', '出品者情報開示前チェック']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yahoo_auc_crawler.middlewares.YahooAucCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'yahoo_auc_crawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'yahoo_auc_crawler.pipelines.YahooAucCrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
