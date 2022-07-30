# from html.parser import HTMLParser
from bs4 import BeautifulSoup

from apps.scraper.models import BrowseAppsPageHtml, ShopifyApps
# from apps.scraper.services.html_scraper import HTMLScraper
# from urllib.parse import urlparse, parse_qs
from urllib import parse


class HTMLProcessor:
    def process_each_page(self, page_no, browse_page_html_obj):
        # browse_page_html_obj = BrowseAppsPageHtml.objects.get(page_no=page_no)
        soup = BeautifulSoup(browse_page_html_obj.content)
        all_app_cards_of_the_page = soup.find_all('div', {'class': 'ui-app-card'})
        for app_card in all_app_cards_of_the_page:
            rank = (24 * (page_no-1)) if page_no != 1 else 0
            app_name = app_card.find('p', {'class': 'ui-app-card__name'}).text
            developed_by = app_card.find('div', {'class': 'ui-app-card__developer-name'}).text
            pricing_format = app_card.find('div', {'class': 'ui-app-pricing--format-short'}).text
            first_link = app_card['data-target-href']
            parsed_url = parse.urlparse(first_link)
            query_params = parse.parse_qs(parsed_url.query)
            rank += int(query_params['surface_intra_position'][0])
            reviews_rating_str = app_card.find('span', {'class': 'ui-star-rating__rating'}).text
            reviews_rating = float(reviews_rating_str.split(' ')[0])
            reviews_count_str = app_card.find('span', {'class': 'ui-review-count-summary'}).text
            reviews_count = int(reviews_count_str.split('reviews')[0][1:])

            ShopifyApps.objects.update_or_create(
                name=app_name,
                developed_by=developed_by,
                defaults={
                    'rank': rank,
                    'pricing_format': pricing_format,
                    'reviews_rating': reviews_rating,
                    'reviews_count': reviews_count
                }
            )

    def process(self):
        all_pages = BrowseAppsPageHtml.objects.all()
        for each_page in all_pages:
            self.process_each_page(
                page_no=each_page.page_no,
                browse_page_html_obj=each_page
            )
