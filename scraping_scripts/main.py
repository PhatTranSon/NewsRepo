from persistence import RDSPersistence
from converter import NewsArticleConverter
from scraper import NewsArticleScraper
from autoscraper import AutoScraper
import requests
from newspaper import Article, fulltext

# Main
if __name__ == "__main__":
    
    # Create auto scraper
    scraper = AutoScraper(
        NewsArticleScraper(),
        NewsArticleConverter(),
        RDSPersistence()
    )

    # Run
    scraper.run()
    

    

