import os

from scrapingbee import ScrapingBeeClient


class HTMLScraper:

    def scrape_page(self):
        response_obj = self.get_client().get(
            self.get_url(),
        )
        return response_obj

    def get_client(self):
        print('99999999999 inside CLIENT')
        return ScrapingBeeClient(api_key=os.environ['SCRAPING_BEE_API_KEY'])

    def get_url(self):
        # return 'https%3A%2F%2Fapps.shopify.com%2Fbrowse'
        print('99999999999 inside get_url')
        return 'https://apps.shopify.com/browse'
