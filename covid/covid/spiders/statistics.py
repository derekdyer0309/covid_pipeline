import scrapy
import logging

class StatisticsSpider(scrapy.Spider):
    name = 'statistics'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus/']

    def parse(self, response):
        countries = response.xpath("//li[@class='news_li']/strong/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield response.follow(link, callback=self.parse_country, meta={"country_name": name})

    def parse_country(self, response):

        name = response.request.meta['country_name']
        cases = response.xpath("(//div//span)[5]/text()").get()
        deaths = response.xpath("(//div//span)[6]/text()").get()
        recovered = response.xpath("(//div//span)[7]/text()").get()

        yield {
            'name': name,
            'cases': cases,
            'deaths': deaths,
            'recovered': recovered
        }
        

