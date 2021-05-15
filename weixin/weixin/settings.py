# Scrapy settings for weixin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from shutil import which
BOT_NAME = 'weixin'

SPIDER_MODULES = ['weixin.spiders']
NEWSPIDER_MODULE = 'weixin.spiders'



# ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = True
SELENIUM_DRIVER_NAME = 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
SELENIUM_DRIVER_ARGUMENTS = ['-headless']  # '--headless' if using chrome instead of firefox
RETRY_TIMES = 3
# Retry on most error codes since proxies fail
# for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
PROXY_LIST = 'weixin/spiders/proxies.text'
PROXY_MODE = 0  # different proxy for each request
RANDOM_UA_PER_PROXY = True
FAKEUSERAGENT_FALLBACK = 'Mozillapip install scrapy_proxies'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sci_abs.middlewares.SciAbsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sci_abs.middlewares.SciAbsDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    #    'news_oil_gas.middlewares.NewsOilGasDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 900,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy_proxies.RandomProxy': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 710,
    'scrapy_selenium.SeleniumMiddleware': 750,
    # 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    # 'scrapy.downloadermiddlewares.cookies.PersistentCookiesMiddleware': 751,
    # 'scrapy_splash.SplashCookiesMiddleware': 650,
    # 'scrapy_splash.SplashMiddleware': 652,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'weixin.pipelines.WeiXinPublicPipeline': 300,
    'weixin.pipelines.WeiXinOilCrossPipeline': 301,
    'weixin.pipelines.WeiXinLngConPipeline': 302,
    'weixin.pipelines.WeiXinCnpcNewsPipeline': 303,
    'weixin.pipelines.WeiXinPetroTradingPipeline': 304,
    'weixin.pipelines.WeiXinEnergyExpressPipeline': 305,
    'weixin.pipelines.WeiXinHaiBeiPipeline': 306,
    'weixin.pipelines.WeiXinOffshoreEnergyPipeline': 307,
    'weixin.pipelines.WeiXinHaiBoPipeline': 308,
    'weixin.pipelines.WeiXinCRSLPipeline': 309,
    'weixin.pipelines.WeiXinOilCubicPipeline': 310,
    'weixin.pipelines.WeiXinOilLinkPipeline': 311

}
SQL_CONNECT_STRING = 'mysql+pymysql://root:jinzheng1706@139.198.191.224:3308/news_oil'
SQL_DB_NAME = 'news_oil'

MONGO_URI = 'mongodb://root:jinzheng1706@139.198.191.224:27017/'
MONGO_DATABASE_WECHAT = 'wechat'

IMAGES_STORE = 'root1/mnt/weixin_images'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weixin (+http://www.yourdomain.com)'
#

COOKIES_ENABLED = True
COOKIES_PERSISTENCE = True
COOKIES_PERSISTENCE_DIR = 'cookies'
COOKIES_STORAGE = 'scrapy_cookies.storage.in_memory.InMemoryStorage'
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
DOWNLOADER_MIDDLEWARES.update({
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy_cookies.downloadermiddlewares.cookies.CookiesMiddleware': 700,
})

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weixin.middlewares.WeixinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weixin.middlewares.WeixinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'weixin.pipelines.WeixinPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
