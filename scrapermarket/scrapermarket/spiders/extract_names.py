import scrapy
from typing import Generator
from urllib.parse import urljoin

class MarketItems(scrapy.Spider):
    name = "extract_names"

    def start_requests(self) -> Generator[scrapy.Request, None, None]:
        base_url = "https://steamcommunity.com/market/search"
        query_params = {
            "category_730_ItemSet[]": "any",
            "category_730_ProPlayer[]": "any",
            "category_730_StickerCapsule[]": "any",
            "category_730_TournamentTeam[]": "any",
            "category_730_Weapon[]": "any",
            "appid": "730",
            "q": "Knife"
        }
        totalPage = 244
        
        for page_num in range(0, totalPage):
            query_params["start"] = page_num * 10  # Assuming each page shows 10 items
            url = base_url + "?" + "&".join(f"{key}={value}" for key, value in query_params.items())
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items_name = response.css('span.market_listing_item_name::text').getall()
        for item in items_name:
            print(item.strip())  # Use strip() to remove extra whitespace if needed
