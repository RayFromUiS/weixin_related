# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from weixin.model import  WeiXinData,WeiXinOilCross,WeiXinLngCon,WeiXinCnpcNews,WeiXinEnergyExpress, \
                        WeiXinPetroTrading,WeiXinHaiBei, WeiXinOffshoreEnergy,WeiXinHaiBo,WeiXinCRSL,\
                        WeiXinOilCubic,WeiXinOilLink


class WeiXinPublicPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinData(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'))

        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()



class WeiXinOilCrossPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinOilCross(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

class WeiXinLngConPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinLngCon(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

class WeiXinCnpcNewsPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinCnpcNews(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()


class WeiXinPetroTradingPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinPetroTrading(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()




class WeiXinEnergyExpressPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinEnergyExpress(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()


class WeiXinHaiBeiPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinHaiBei(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()


class WeiXinOffshoreEnergyPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinOffshoreEnergy(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

class WeiXinHaiBoPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinHaiBo(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()


class WeiXinCRSLPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinCRSL(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

class WeiXinOilCubicPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinOilCubic(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))


        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

class WeiXinOilLinkPipeline:
    def process_item(self, item, spider):

        new_item = WeiXinOilLink(title=item.get('title'), author=item.get('author'), pre_title=item.get('pre_title'), \
                            preview_img_link=item.get('preview_img_link'), pub_time=item.get('pub_time'), \
                            content=item.get('content'), crawl_time=item.get('crawl_time'), url=item.get('url'), \
                            categories=item.get('categories'),images_url=str(item.get('image_urls')),images=str(item.get('images')))

        adapter = ItemAdapter(item)

        try:
            if adapter.get('content'):
                spider.session.add(new_item)
                spider.session.commit()
            else:
                raise (f"Missing content in {item}")
        except:
            spider.session.rollback()
        return item

    def close_spider(self, spider):
        spider.session.close()

