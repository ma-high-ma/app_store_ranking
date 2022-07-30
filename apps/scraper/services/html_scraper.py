import os

from scrapingbee import ScrapingBeeClient

from apps.scraper.models import BrowseAppsPageHtml


class HTMLScraper:

    def scrape_page(self):
        client = self.get_client()
        url = self.get_url()
        for page in range(1, 6):
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

        # response_obj = client.get(
        #     url_with_page_no,
        # )
        print('SCRAPING COMPLETE')
        return

    def get_client(self):
        print('99999999999 inside CLIENT')
        return ScrapingBeeClient(api_key=os.environ['SCRAPING_BEE_API_KEY'])

    def get_url(self):
        # return 'https%3A%2F%2Fapps.shopify.com%2Fbrowse'
        print('99999999999 inside get_url')
        return 'https://apps.shopify.com/browse'
