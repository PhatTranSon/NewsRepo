import mysql.connector
import boto3
import newspaper
from abc import abstractmethod

from newspaper.utils import memoize_articles

# NewsArticle object
class NewsArticle:
    def __init__(self, image, text, title, authors, url):
        self.image = image
        self.text = text
        self.title = title
        self.authors = authors
        self.url = url

    def __repr__(self):
        return f"{self.title}: {self.text}"

# Interfaces
class Scraper:
    @abstractmethod
    def scrape(self):
        # This scraper scrapers the web to get news articles
        pass

class Converter:
    @abstractmethod
    def convert(self, object):
        # This method receive the object from Scraper and parse it into list of news articles
        pass

class Persistence:
    @abstractmethod
    def save(self, news_articles):
        # This method saves the news_article into a Database (cloud or local)
        pass

# Implementation
class NewsArticleScraper(Scraper):
    def __init__(self):
        self.publishers = [
            "http://cbs.com",
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

class NewsArticleConverter(Converter):
    def convert_one(self, item):
        # Download and then parse articles
        item.download()
        item.parse()

        # Convert to news article object
        news_article = NewsArticle(item.top_image, item.text, item.title, ", ".join(item.authors), item.url)
        return news_article

    def convert(self, items):
        converted = []
        for item in items:
            converted.append(self.convert_one(item))
        return converted

# TODO: Implement saving to mysql database
class RDSPersistence(Persistence):
    def save(self, news_articles):
        pass


# Main
if __name__ == "__main__":
    #  Test
    news = NewsArticleScraper()
    articles = news.scrape()

    converter = NewsArticleConverter()
    converted_articles = converter.convert(articles)

    for item in converted_articles:
        print(item)
    