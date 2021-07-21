from abc import abstractmethod
import newspaper


# Interfaces
class Scraper:
    @abstractmethod
    def scrape(self):
        # This scraper scrapers the web to get news articles
        pass

# Implementation
class NewsArticleScraper(Scraper):
    def __init__(self):
        self.publishers = [
            "https://www.nytimes.com",
            "https://apnews.com/"
        ]

    def scrape(self, only_new=False):
        arcticles = []

        for publisher in self.publishers:
            # Load publishers
            source = self.create_source(publisher, only_new)
            # Get ten articles from publisher 
            top_articles = self.get_top_articles(source)
            # Push into arrays
            arcticles += top_articles

        return arcticles

    def create_source(self, publisher, only_new):
        return newspaper.build(publisher, memoize_articles=only_new)

    def get_top_articles(self, source, total=10):
        return source.articles[:total]