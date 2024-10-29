from flask import Flask
import scrapy
from scrapy.crawler import CrawlerProcess

from goodonyou_bs4 import get_score

keywords = input("Describe the item you want to replace: ").strip().split(" ")
brand_name = input("What is the brand of your original item?: ").title()
# max_price = float(input("What is your maximum price?: "))

search_query = "+".join(keywords)
search_url = f"https://www.google.com/search?tbm=shop&q={search_query}+ethical+sustainable"


class Alternatives(scrapy.Spider):
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 6
    }

    name = 'alternatives'
    allowed_domains = ["www.google.com"]
    start_urls = [search_url]

    data = []

    def parse(self, response):
        next_page_url = response.xpath("//a[@class='lYtaR']/@href").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
        products = response.xpath("//div[@class='u30d4']")

        for product in products:
            company_name = product.xpath(".//div[@class='dD8iuc']/text()").get().split("from ")[1]
            product_link = f"https://google.com{product.xpath(".//div[@class='rgHvZc']/a/@href").get()}"
            query_name = "-".join(company_name.split(" ")).lower()

            result = get_score(query_name)
            if result:
                self.data.append({
                    company_name: {"scores": result, "link": product_link}})

        yield None


process = CrawlerProcess()
process.crawl(Alternatives)
process.start()
print(Alternatives.data)
filtered_data = [d for d in Alternatives.data if brand_name not in d.keys()]
print(filtered_data)




