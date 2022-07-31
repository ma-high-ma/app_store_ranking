# from html.parser import HTMLParser
from bs4 import BeautifulSoup

from apps.scraper.models import BrowseAppsPageHtml, ShopifyApps
# from apps.scraper.services.html_scraper import HTMLScraper
# from urllib.parse import urlparse, parse_qs
from urllib import parse

from apps.scraper.models.app_delta import AppDelta


class HTMLProcessor:
    def process_each_page(self, page_no, browse_page_html_obj):
        print('page_no = ', page_no)
        # browse_page_html_obj = BrowseAppsPageHtml.objects.get(page_no=page_no)
        soup = BeautifulSoup(browse_page_html_obj.content)
        all_app_cards_of_the_page = soup.find_all('div', {'class': 'ui-app-card'})
        for app_card in all_app_cards_of_the_page:
            rank = (24 * (page_no - 1)) if page_no != 1 else 0
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

            app_data = {
                'name': app_name,
                'developed_by': developed_by,
                'rank': rank,
                'pricing_format': pricing_format,
                'reviews_rating': reviews_rating,
                'reviews_count': reviews_count,
            }

            shopify_app_obj = ShopifyApps.objects.filter(
                name=app_name,
                developed_by=developed_by
            ).first()
            if shopify_app_obj is not None:
                if shopify_app_obj.rank != rank:
                    print('change detected in app = ', app_name)
                    new_details = {
                        'reviews_rating': reviews_rating,
                        'reviews_count': reviews_count,
                    }
                    old_details = {
                        'reviews_rating': shopify_app_obj.reviews_rating,
                        'reviews_count': shopify_app_obj.reviews_count,
                        'signifiers': shopify_app_obj.signifiers,
                        'extras': shopify_app_obj.extras
                    }
                    # make an entry in the table
                    AppDelta.objects.create(
                        app_name=app_name,
                        previous_rank=shopify_app_obj.rank,
                        new_rank=rank,
                        app_previous_details=old_details,
                        app_new_details=new_details
                    )
                shopify_app_obj.update(**app_data)
                shopify_app_obj.save()

            else:
                print('no change in app = ', app_name)
                ShopifyApps.objects.create(
                    **app_data
                )



    def process(self):
        all_pages = BrowseAppsPageHtml.objects.all()
        for each_page in all_pages:
            self.process_each_page(
                page_no=each_page.page_no,
                browse_page_html_obj=each_page
            )
