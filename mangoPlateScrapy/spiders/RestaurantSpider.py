import scrapy
from scrapy.loader import ItemLoader

from mangoPlateScrapy.items import Restaurant


class RestaurantSpider(scrapy.Spider):
    name = "restaurants"

    def start_requests(self):
        start_urls = [
            'http://mangoplate.com/en/restaurants/LseZO3K40L',
            'http://mangoplate.com/en/restaurants/KoY0XYWoNcJV'
            #feed urls
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        loadRestaurant = ItemLoader(item=Restaurant(), response=response)
        loadRestaurant.add_xpath('name', '//section[contains(@class, "restaurant-detail")]//span[contains(@itemprop, "name")]/text()')
        loadRestaurant.add_xpath('telephone', '//section[contains(@class, "restaurant-detail")]//span[contains(@itemprop, "telephone")]/text()')
        loadRestaurant.add_xpath('addressLocality', 'normalize-space(//section[contains(@class, "restaurant-detail")]//span[contains(@itemprop, "addressLocality")]/text())')
        loadRestaurant.add_xpath('priceRange', '//section[contains(@class, "restaurant-detail")]//td[contains(@itemprop, "priceRange")]/text()')
        loadRestaurant.add_xpath('openingHours', '//section[contains(@class, "restaurant-detail")]//td[contains(@itemprop, "openingHours")]/text()')
        loadRestaurant.add_xpath('cuisineType', '//section[contains(@class, "restaurant-detail")]//table/tbody/tr[3]/td/text()')
        return loadRestaurant.load_item()