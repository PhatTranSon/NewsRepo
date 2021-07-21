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