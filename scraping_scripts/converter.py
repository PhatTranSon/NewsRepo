from abc import abstractmethod
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

        # Convert to news article object
        news_article = NewsArticle(item.top_image, item.text, item.title, ", ".join(item.authors), item.url)
        return news_article

    def convert(self, items):
        converted = []
        for item in items:
            converted.append(self.convert_one(item))
        return converted