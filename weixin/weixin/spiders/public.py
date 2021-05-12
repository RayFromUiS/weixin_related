
from PIL import Image

import time
from datetime import datetime
import scrapy
from weixin.items import  WeixinItem,OilCrossItem,LngConItem,CnpcNewsItem,EnergyExpressItem,PetroTradingItem,\
                        HaiBeiItem,OffshoreEnergyItem,HaiBoItem,CRSLItem,OilCubicItem,OilLinkItem
from weixin.model import db_connect,create_table,WeiXinData,WeiXinOilCross,WeiXinLngCon,WeiXinCnpcNews,WeiXinEnergyExpress, \
                        WeiXinPetroTrading,WeiXinHaiBei,WeiXinOffshoreEnergy,WeiXinHaiBo,WeiXinCRSL, \
                        WeiXinOilCubic,WeiXinOilLink
from scrapy.http import HtmlResponse
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
from selenium.webdriver.support.ui import WebDriverWait
from weixin.helpers import WeChatParams


import pymongo
from scrapy.utils.project import get_project_settings



class PublicSpider(scrapy.Spider):
    name = 'public'
    # start_urls = []
    query_names = [('cnpc_news', '中国石油报'), ('energy_express', '能源快讯'), ('petro_trading', '石油商报'),
                   ('haibei', '海贝能源'), ('offshore_energy', '海洋能源与工程咨询平台'), ('haibo', '海波谈LNG'),
                   ('crsl', '克拉克森研究CRSL'), ('oil_cubic', '石油圈'), ('oil_link', '石油link'),
                   ('oil_cross', '油气经纬'), ('lng_con', '天然气咨询')]

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'public_wechat'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def start_requests(self):
        '''request url from database'''
        docs = self.db[self.collection].find()

        for doc in docs:

            url = doc.get('link')
            # print(url)
            result = self.session.query(WeiXinData) \
                .filter(WeiXinData.url == url) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )
    def parse(self, response):
        # from scrapy.shell import puinspect_response
        # inspect_response(response,self)
        item = WeixinItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  OilCrossSpider(scrapy.Spider):
    name = 'oil_cross'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinOilCrossPipeline': 301},
    }
    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'oil_cross'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinOilCross) \
                .filter(or_(WeiXinOilCross.url == url,WeiXinOilCross.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = OilCrossItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  LngConSpider(scrapy.Spider):
    name = 'lng_con'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinLngConPipeline': 302},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'lng_con'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:
            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinLngCon) \
                .filter(or_(WeiXinLngCon.url == url,WeiXinLngCon.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = LngConItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item

class  CnpcNewsSpider(scrapy.Spider):
    name = 'cnpc_news'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinCnpcNewsPipeline': 303},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'cnpc_news'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinCnpcNews) \
                .filter(or_(WeiXinCnpcNews.url == url,WeiXinCnpcNews.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = CnpcNewsItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  PetroTradingSpider(scrapy.Spider):
    name = 'petro_trading'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinPetroTradingPipeline': 304},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'petro_trading'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinPetroTrading) \
                .filter(or_(WeiXinPetroTrading.url == url,WeiXinPetroTrading.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = PetroTradingItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  EnergyExpressSpider(scrapy.Spider):
    name = 'energy_express'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinEnergyExpressPipeline': 305},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'energy_express'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinEnergyExpress) \
                .filter(or_(WeiXinEnergyExpress.url == url,WeiXinEnergyExpress.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = EnergyExpressItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item



class  HaiBeiSpider(scrapy.Spider):
    name = 'haibei'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinHaiBeiPipeline': 306},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'haibei'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinHaiBei) \
                .filter(or_(WeiXinHaiBei.url == url,WeiXinHaiBei.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = HaiBeiItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item

class  WeiXinOffshoreEnergySpider(scrapy.Spider):
    name = 'offshore_energy'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinOffshoreEnergyPipeline': 307},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'offshore_energy'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinOffshoreEnergy) \
                .filter(or_(WeiXinOffshoreEnergy.url == url,WeiXinOffshoreEnergy.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = OffshoreEnergyItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item



class  HaiBoSpider(scrapy.Spider):
    name = 'haibo'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinHaiBoPipeline': 308},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'offshore_energy'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinHaiBo) \
                .filter(or_(WeiXinHaiBo.url == url,WeiXinHaiBo.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = HaiBoItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item

class  CRSLSpider(scrapy.Spider):
    name = 'crsl'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinCRSLPipeline': 309},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'crsl'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinCRSL) \
                .filter(or_(WeiXinCRSL.url == url,WeiXinCRSL.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = CRSLItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  OilCubicSpider(scrapy.Spider):
    name = 'oil_cubic'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinOilCubicPipeline': 310},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'oil_cubic'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:
            url = doc.get('link')
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinOilCubic) \
                .filter(or_(WeiXinOilCubic.url == url,WeiXinOilCubic.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = OilCubicItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item




class  OilLinkSpider(scrapy.Spider):
    name = 'oil_link'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinOilLinkPipeline': 311,
                           'scrapy.pipelines.images.ImagesPipeline': 1,},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'oil_link'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link').strip()
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinOilLink) \
                .filter(or_(WeiXinOilLink.url == url,WeiXinOilLink.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = OilLinkItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['preview_img_link'] = None
        item['image_urls'] = response.css('div#js_content').css('img::attr(data-src)').getall()
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        item['categories'] = None
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item


class  ImageDownloaderSpider(scrapy.Spider):
    name = 'img_downloader'

    custom_settings = {
        'ITEM_PIPELINES': {'weixin.pipelines.WeiXinOilLinkPipeline': 311},
    }

    def __init__(self):
        self.engine = db_connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        create_table(self.engine)
        # self.mysql_db = 'WeiXinData'
        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = 'oil_link'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def start_requests(self):
        docs = self.db[self.collection].find()
        for doc in docs:

            url = doc.get('link').strip()
            title = doc.get('title')
            # print(url)
            result = self.session.query(WeiXinOilLink) \
                .filter(or_(WeiXinOilLink.url == url,WeiXinOilLink.title == title)) \
                .first()
            if not result:
                yield SeleniumRequest(url=url,
                                      callback=self.parse,
                                      wait_time=30,
                                      wait_until=EC.presence_of_element_located(
                                          (By.ID, 'js_content'))
                                      )

    def parse(self, response):
        item = OilLinkItem()
        item['url'] = response.url
        item['author'] = response.css('span#profileBt a::text').get().strip()
        item['title'] = response.css('h2#activity-name::text').get().strip()
        item['pub_time'] = response.css('em#publish_time::text').get()
        item['image_urls'] = response.css('div#js_content').css('img::attr(data-src)').getall()
        item['pre_title'] = None
        item['content'] = response.css('div#js_content').get()
        # item['images'] =
        item['crawl_time'] = datetime.now().strftime('%m/%d/%Y %H:%M')

        yield item





