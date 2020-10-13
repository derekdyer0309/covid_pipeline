import scrapy
import logging


class TotalsSpider(scrapy.Spider):
    name='totals'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        total_cases = response.xpath('(//span)[5]/text()').get()
        total_deaths = response.xpath('(//span)[6]/text()').get()
        total_recovered = response.xpath('(//span)[7]/text()').get()

        yield {
            "total_cases": total_cases,
            "total_deaths": total_deaths,
            "total_recovered": total_recovered
        }