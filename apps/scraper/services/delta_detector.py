import datetime
from datetime import date, timedelta

from apps.scraper.models import ShopifyApps, AppDelta
from apps.scraper.services.html_processor import HTMLProcessor
from apps.scraper.services.html_scraper import HTMLScraper


class DeltaDetector:
    def detect_and_update(self):
        # Updates BrowseAppsPageHtml table
        HTMLScraper().scrape_page(start_page_no=1, last_page_no=5)
        HTMLProcessor().process()
        print('PROCESS COMPLETE')


class AppDeltaProcessor:
    def process(self):
        today = date.today()
        shopify_apps_scraped_today = ShopifyApps.objects.filter(created_at=today)
        print("today's apps = ", shopify_apps_scraped_today)
        shopify_apps_scraped_yesterday = ShopifyApps.objects.filter(created_at=today - timedelta(days=1))
        print("yesterday's apps = ", shopify_apps_scraped_yesterday)

        for app_yesterday in shopify_apps_scraped_yesterday:
            app_today = shopify_apps_scraped_today.filter(name=app_yesterday.name, developed_by=app_yesterday.developed_by).first()
            if not app_today:
                # App was present in scraped page yesterday, but it in not present in the scraped page today
                # Then we can say the rank of the app > 24 * no_of_pages_scraped_since_page_1
                # The rank of these apps is considered 999999
                print('This app existed yesterday, not today. Name = ', app_yesterday.name, 'Dev by = ', app_yesterday.developed_by)
                ShopifyApps.objects.create(
                    name=app_yesterday.name,
                    developed_by=app_yesterday.developed_by,
                    rank=999999,
                    created_at=datetime.date.today()
                )
            else:
                if app_yesterday.rank != app_today.rank:
                    print('Rank changed for this app = ', app_today.name)
                    AppDelta.objects.create(
                        app=app_today,
                        previous_rank=app_yesterday.rank,
                        new_rank=app_today.rank,
                        rank_delta=(app_today.rank-app_yesterday.rank),
                        app_previous_details=self.get_app_details(app_yesterday),
                        app_new_details=self.get_app_details(app_today)
                    )
        print('DELTA PROCESSING COMPLETE')

    def get_app_details(self, app_obj):
        return {
            "reviews_rating": app_obj.reviews_rating,
            "reviews_count": app_obj.reviews_count,
            "pricing_format": app_obj.pricing_format,
            "signifiers": app_obj.signifiers,
            "extras": app_obj.extras
        }
