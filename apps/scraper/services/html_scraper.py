import os

from scrapingbee import ScrapingBeeClient

from apps.scraper.models import BrowseAppsPageHtml


class HTMLScraper:

    def scrape_page(self, start_page_no, last_page_no):
        client = self.get_client()
        url = self.get_url()
        for page in range(start_page_no, last_page_no+1):
            try:
                print('page_no=', page)
                url_with_page_no = f'{url}?page={str(page)}'
                response_object = client.get(
                    url_with_page_no,
                )
                BrowseAppsPageHtml.objects.create(
                    page_no=page,
                    content=response_object.content
                )
            except Exception as e:
                print('EXCEPTION: ', str(e))

        print('SCRAPING COMPLETE')
        return

    def get_client(self):
        return ScrapingBeeClient(api_key=os.environ['SCRAPING_BEE_API_KEY'])

    def get_url(self):
        return 'https://apps.shopify.com/browse'
