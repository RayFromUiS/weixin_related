import os
import re
import time
from fake_useragent import UserAgent
from selenium.webdriver import Firefox
import requests as req
import pymongo
import random
import json
# from weixin.model import WeiXinData,db_connect,create_table
from sqlalchemy.orm import sessionmaker

import urllib3
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from scrapy.utils.project import get_project_settings
from scrapy import Request
from selenium.webdriver.common.proxy import Proxy, ProxyType

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def set_cookies(cookie_file):
    '''get cookie
    '''

    with webdriver.Firefox() as driver:
        # res = SeleniumRequest(url=self.URL)
        driver.get(URL)
        time.sleep(120)
        cookie_items = driver.get_cookies()
        post_cookie = {}
        for cookie_item in cookie_items:
            post_cookie[cookie_item['name']] = cookie_item['value']
        cookie_str = json.dumps(post_cookie)
        with open(cookie_file, 'w', encoding='utf-8') as f:
            f.write(cookie_str)
        print(driver.current_url)

    return post_cookie


def get_token(cookie_file):
    '''get token from cookie'''
    with open(cookie_file, 'r', encoding='utf-8') as f:
        cookie = f.read()
        cookies = json.loads(cookie)

    res = req.get(url=URL,
                  cookies=cookies,
                  # proxies=self.proxy,
                  verify=False)
    token = re.findall(r'token=(\d+)', str(res.url))[0]

    return token, cookies


class WeChatParams:
    '''wechat link will grap the search keywords such as
    "石油圈",
    '''

    def __init__(self, query_name, cookie, token, proxy_file='spiders/proxies.text'):
        self.query_name = query_name[1]
        #         self.driver = None
        self.proxy_file = proxy_file
        self.cookies = cookie
        self.token = token
        # self.links = []

        self.mongo_uri = get_project_settings().get('MONGO_URI')
        self.mongo_db = get_project_settings().get('MONGO_DATABASE_WECHAT')
        self.collection = query_name[0]
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def update_proxies(self):
        '''is not functioning'''
        # with open(self.proxy_file, 'r') as f:
        #     org_proxies = f.read().splitlines()
        # # while len(org_proxies)>=1:
        #         self.proxies = org_proxies
        #         self.proxy = {'http': random.choice(org_proxies),
        #                       'https': random.choice(org_proxies)
        #                       }
        # self.proxy = {'http':'http://111.7.175.36:80',
        #                 'https':'http://111.7.175.36:80'}
        self.proxy = None

    def set_headers(self):
        useragent = UserAgent()
        self.headers = {
            "HOST": "mp.weixin.qq.com",
            "Origin": "https://mp.weixin.qq.com",
            "User-Agent": useragent.random,
            "Connection": "keep-live"
        }

    # def set_token(self):
    #     '''set token for further request'''
    #     with open('cookie.txt', 'r', encoding='utf-8') as f:
    #         cookie = f.read()
    #         cookies = json.loads(cookie)
    #     print(self.cookies)
    #     #         print(cookies)
    #     print(self.token)
    #     if not self.token:
    #         res = req.get(url=URL,
    #                       cookies=cookies,
    #                       proxies=self.proxy,
    #                       verify=False)
    #         print(res.url)
    #         self.token = re.findall(r'token=(\d+)', str(res.url))[0]
    #         print(self.token)

    def set_query_params(self):
        '''set query_params for request'''
        self.query_params = {
            'action': 'search_biz',
            'token': self.token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            #         'random': random.randint(1,10),
            'query': self.query_name,
            'begin': '0',
            'count': '5'
        }

    def set_fakeid(self):
        '''get the fake id'''
        res = req.get(url=SearchUrl,
                      cookies=self.cookies,
                      headers=self.headers,
                      params=self.query_params,
                      proxies=self.proxy,
                      verify=False,
                      timeout=60)
        # res = req.get(url=self.SearchUrl,
        #               headers=self.headers,
        #               proxies=self.proxy,
        #               body=self.query_params,
        #               cookies=self.cookies)
        fake_id_dict = res.json().get('list')[0]
        self.fakeid = fake_id_dict.get('fakeid')

    def set_article_params(self):
        '''set article params'''

        self.article_params = {
            "action": 'list_ex',
            "begin": 0,
            "count": 5,
            "fakeid": self.fakeid,
            "type": 9,
            'token': self.token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
        }

    def set_app_nums(self):
        '''get the page number related parameter'''
        res = req.get(url=ArticleUrl,
                      cookies=self.cookies,
                      headers=self.headers,
                      params=self.article_params,
                      proxies=self.proxy,
                      verify=False,
                      timeout=60
                      )
        # res = req.get(url=self.ArticleUrl,
        #               headers=self.headers,
        #               body=self.article_params,
        #               proxies=self.proxy,
        #               ve
        #               cookies=self.cookies)

        # print(res.json())
        if res.status_code == 200:
            print(res.json())
            self.app_sums = res.json().get('app_msg_cnt')
        else:
            print(res.json)

    def get_links(self):
        # article_params = self.article_params
        results = []

        for i in range(10,15,1):
            article_params = self.article_params
            article_params['begin'] = 5*i
            try:
                articles_res = req.get(ArticleUrl,
                           cookies=self.cookies,
                           headers=self.headers,
                           proxies=self.proxy,
                           params=article_params)

                article_list = articles_res.json().get('app_msg_list')
                            # print(article_list)
                if article_list:
                    for item in article_list:
                        result = self.db[self.collection].find_one({'title': item.get('title')})
                        print('the item is',item, '/n')
                          # <-- should return: True
                        # result_and = self.db[self.collection].find_one({'title': item.get('title')})
                        results.append(result)
                        if not result :
                            insert_one = self.db[self.collection].insert_one(item)
                            print(insert_one.acknowledged)
                            self.links.append(item.get('link'))

                        else:
                            continue
            except:
                continue

            finally:
                time.sleep(30)



    # def get_links(self):
    #     results = []
    #     begin = 0
    #     if self.app_sums:
    #         num = int(self.app_sums) // 5
    #         print(num)
    #         for i in range(num):
    #             article_params = self.article_params
    #             article_params['begin'] = i*5
    #
    #             try:
    #                 articles_res = req.get(ArticleUrl,
    #                                        cookies=self.cookies,
    #                                        headers=self.headers,
    #                                        proxies=self.proxy,
    #                                        params=article_params)
    #
    #                 article_list = articles_res.json().get('app_msg_list')
    #                 # print(article_list)
    #                 if article_list:
    #                     for item in article_list:
    #                         result = self.db[self.collection].find_one({'title': item.get('title')})
    #                         print('the item is',item, '/n')
    #                           # <-- should return: True
    #                         # result_and = self.db[self.collection].find_one({'title': item.get('title')})
    #                         results.append(result)
    #                         if not result :
    #                             insert_one = self.db[self.collection].insert_one(item)
    #                             print(insert_one.acknowledged)
    #                             self.links.append(item.get('link'))
    #
    #                         else:
    #                             continue
    #
    #             except:
    #                 continue
    #
    #             finally:
    #                 time.sleep(60)
    #
    #             # else:
    #             #     # all result is  not scraped, then flip pass in new pargrams
    #             #     if len([result for result in results if result is None]) == len(results):
    #             #         break
    #
    #     # return self.links


if __name__ == '__main__':

    cookie_file = 'cookie.txt'
    query_names = [
                   ('haibei', '海贝能源'),('offshore_energy', '海洋能源与工程咨询平台'), ('haibo', '海波谈LNG'),
                   ('crsl', '克拉克森研究CRSL'), ('oil_cubic', '石油圈'), ('oil_link', '石油link'),
                   ('oil_cross', '油气经纬'), ('lng_con', '天然气咨询'),('cnpc_news', '中国石油报'),
                     ('energy_express', '能源快讯'), ('petro_trading', '石油商报')]

    URL = 'https://mp.weixin.qq.com/'
    SearchUrl = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    ArticleUrl = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'

    # try_times = 0
    token = None
    while not token:
        try:
            os.path.exists(cookie_file)
            token, cookies = get_token(cookie_file)
        except:
            cookies = set_cookies(cookie_file)
            token = get_token(cookie_file)
        # finally:

    # print(token,cookies)
    for query_name in query_names:
        wechat_link = WeChatParams(query_name, cookies, token)
        # wechat_link = WeChatParams('石油圈')
        wechat_link.update_proxies()
        # print(wechat_link.proxy)
        wechat_link.set_headers()
        # print(wechat_link.set_headers)
        wechat_link.set_query_params()
        print(wechat_link.query_params)
        wechat_link.set_fakeid()
        print(wechat_link.fakeid)
        wechat_link.set_article_params()
        # print(wechat_link.article_params)
        wechat_link.set_app_nums()
        print(wechat_link.app_sums)
        try:
            wechat_link.get_links()
        except:
            print(f'such query name is crawled', query_name)
            continue
        time.sleep(60)
