# NewsArticle object
class NewsArticle:
    def __init__(self, image, text, title, authors, url, date):
        self.image = image
        self.text = text
        self.title = title
        self.authors = authors
        self.url = url
        self.date = date

    def __repr__(self):
        return f"{self.title}: {self.text}"