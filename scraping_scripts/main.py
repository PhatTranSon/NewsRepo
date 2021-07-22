from persistence import RDSPersistence
from converter import NewsArticleConverter
from scraper import NewsArticleScraper
from autoscraper import AutoScraper
import time

# Time to sleep in second (2 hours)
SLEEP_TIME = 3600 * 2

# Main
if __name__ == "__main__":
    # Create auto scraper
    scraper = AutoScraper(
        NewsArticleScraper(),
        NewsArticleConverter(),
        RDSPersistence()
    )

    while True:
        # Run
        scraper.run()

        # Display message
        print("__________Done scraping for current ieration__________")

        # Sleep for 2 hours
        time.sleep(SLEEP_TIME)
    

    

