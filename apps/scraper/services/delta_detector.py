from apps.scraper.services.html_processor import HTMLProcessor
from apps.scraper.services.html_scraper import HTMLScraper


class DeltaDetector:
    def detect_and_update(self):
        # Updates BrowseAppsPageHtml table
        HTMLScraper().scrape_page(start_page_no=1, last_page_no=5)
        HTMLProcessor().process()
        print('PROCESS COMPLETE')

