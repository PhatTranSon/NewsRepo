class AutoScraper:
    def __init__(self, scraper, converter, persistence):
        self._scraper = scraper
        self._converter = converter
        self._persistence = persistence

    def run(self):
        # First get the news using scraper
        raw_articles = self._scraper.scrape()
        # Convert them to right format
        converted_articles = self._converter.convert(raw_articles)
        # Save into database
        self._persistence.save(converted_articles)
