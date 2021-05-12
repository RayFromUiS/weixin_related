from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner,CrawlerProcess
from scrapy.utils.log import configure_logging

from weixin.spiders.public import  OilCrossSpider,LngConSpider,CnpcNewsSpider,PetroTradingSpider,\
    EnergyExpressSpider,HaiBeiSpider,WeiXinOffshoreEnergySpider,HaiBoSpider,\
    CRSLSpider,OilCubicSpider,OilLinkSpider
from scrapy.settings import Settings
from weixin import settings


def run_scraper():
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    configure_logging()
    # runner = CrawlerRunner(settings=crawler_settings)
    # task = LoopingCall(lambda: runner.crawl(NewsOeOffshoreSpider))
    # task.start(6000 * 100)
    # reactor.run()
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(OilCrossSpider)
    process.crawl(LngConSpider)
    process.crawl(CnpcNewsSpider)
    process.crawl(PetroTradingSpider)

    process.crawl(EnergyExpressSpider)
    process.crawl(HaiBeiSpider)
    process.crawl(WeiXinOffshoreEnergySpider)

    process.crawl(HaiBoSpider)
    process.crawl(CRSLSpider)
    process.crawl(OilCubicSpider)
    process.crawl(OilLinkSpider)

    process.start()


if __name__ == "__main__":
    run_scraper()
