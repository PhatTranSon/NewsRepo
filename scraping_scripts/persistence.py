from abc import abstractmethod
import mysql.connector
import os

# TODO: Implement saving to mysql database
class Persistence:
    @abstractmethod
    def save(self, news_articles):
        pass

class RDSPersistence(Persistence):
    def __init__(self):
        # Get database information fro environment
        self._host = os.environ.get("NEWSDB_HOST") or "localhost"
        self._database = os.environ.get("NEWSDB_NAME") or "newsrepo_db"
        self._username = os.environ.get("NEWSDB_USER") or "root"
        self._password = os.environ.get("NEWSDB_PASSWORD") or "Rm!t2012781357"

        # Initialize setup
        self.create_database()
        self.create_table()

    def create_database(self):
        # Create database
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._username,
            password=self._password
        )

        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS newsrepo_db")

    def get_db_connection(self):
        # Create table
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._username,
            password=self._password,
            database=self._database
        )

        return mydb

    def create_table(self):
        # Create table
        mydb = self.get_db_connection()

        # Get cursor and create table
        cursor = mydb.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles(
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                image VARCHAR(500),
                text TEXT,
                authors TEXT,
                url VARCHAR(500),
                date DATE
            )
        """)

    @abstractmethod
    def save(self, news_articles):
        # This method saves the news_article into a Database (cloud or local)
        mydb = self.get_db_connection()
        cursor = mydb.cursor()

        # Iterate through articles, add them to db
        sql = "INSERT INTO articles VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)"
        for article in news_articles:
            values = (article.title, article.image, article.text, article.authors, article.url, article.date)
            cursor.execute(sql, values)

        # Commit transaction
        mydb.commit()

