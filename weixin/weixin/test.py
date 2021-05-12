import scrapy
from scrapy_selenium import SeleniumRequest

res = scrapy.Request(url='https://mp.weixin.qq.com/')


def proxy_res(self, response):
    if response.status == 200:
        return
    else:
        return False