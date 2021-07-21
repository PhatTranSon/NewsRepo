from abc import abstractmethod
from newspaper.api import fulltext
import requests
from article import NewsArticle

class Converter:
    @abstractmethod
    def convert(self, object):
        # This method receive the object from Scraper and parse it into list of news articles
        pass


class NewsArticleConverter(Converter):
    def convert_one(self, item):
        # Download and then parse articles
        item.download()
        item.parse()

        # Get the text
        html = requests.get(item.url).text
        text = fulltext(html)

        print("URL: " + item.url)
        print(text)
        print("_____________________")

        # Convert to news article object
        news_article = NewsArticle(item.top_image, text, item.title, ", ".join(item.authors), item.url)
        return None if text is None or len(text) == 0 else news_article

    def convert(self, items):
        converted = []
        for item in items:
            article = self.convert_one(item)
            if article:
                converted.append(article)
        return converted