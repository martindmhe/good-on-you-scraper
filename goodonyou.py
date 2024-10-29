import scrapy
from scrapy.crawler import CrawlerProcess


def get_score(brand):

    class GoodOnYouScore(scrapy.Spider):
        name = 'api'
        allowed_domains = ["directory.goodonyou.eco"]
        start_urls = [f"https://directory.goodonyou.eco/brand/{brand}"]

        scores = []

        def parse(self, response):

            result = response.xpath("//span[contains(@class, 'LabelMeter__TextScore-sc-6zrovj-2')]/text()").getall()

            self.scores.append({
                'planet': int(result[0].split(" ")[0]),
                'people': int(result[1].split(" ")[0]),
                'animals': int(result[2].split(" ")[0])
            })


            yield None

    process = CrawlerProcess()
    process.crawl(GoodOnYouScore)
    process.start()

    if len(GoodOnYouScore.scores) > 0:
        return GoodOnYouScore.scores[0]
    else:
        return False
