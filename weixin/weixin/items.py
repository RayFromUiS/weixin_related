# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class WeixinItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#
#     # define the fields for your item here like:
#     preview_img_link = scrapy.Field()
#     url = scrapy.Field()
#     pre_title = scrapy.Field()
#     title = scrapy.Field()
#     # title = scrapy.Field()
#     # sub_title = scrapy.Field()
#     content = scrapy.Field()
#     # img_content = scrapy.Field()
#     categories = scrapy.Field()
#     pub_time = scrapy.Field()
#     author = scrapy.Field()
#     crawl_time = scrapy.Field()

class OilLinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:

    image_urls = scrapy.Field() ##preview img urls
    images = scrapy.Field()
    categories = scrapy.Field()
    url = scrapy.Field()
    preview_img_link = scrapy.Field()
    pre_title = scrapy.Field()
    title = scrapy.Field()
    # title = scrapy.Field()
    # sub_title = scrapy.Field()
    content = scrapy.Field()
    # img_content = scrapy.Field()
     ## categories field
    pub_time = scrapy.Field()
    author = scrapy.Field()
    crawl_time = scrapy.Field()

class OilCrossItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class LngConItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class CnpcNewsItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class EnergyExpressItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class PetroTradingItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class HaiBeiItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class OffshoreEnergyItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class HaiBoItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class CRSLItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
class OilCubicItem(OilLinkItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # define the fields for your item here like:
    pass
# class OilLinkItem(WeixinItem):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#
#     # define the fields for your item here like:
#     pass

