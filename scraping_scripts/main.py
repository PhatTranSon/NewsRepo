import mysql.connector
import boto3
from article import NewsArticle
from persistence import RDSPersistence

# Main
if __name__ == "__main__":
    # Create some articles
    articles = [
        NewsArticle("http://google.com", "Hello World", "The End is There", "John C. Ena", "http://google.com"),
        NewsArticle("http://google.com", "Hello New World", "The End is Now", "John C. Ena", "http://google.com")
    ]

    # Insert to db
    persistence = RDSPersistence()
    persistence.save(articles)

    

