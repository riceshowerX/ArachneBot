# src/ui/event_handler.py
from src.crawler.simple_crawler import SimpleCrawler

class EventHandler:
    def __init__(self, ui):
        self.ui = ui

    def start_crawl(self):
        self.ui.append_text("Starting crawl...")
        crawler = SimpleCrawler()
        content = crawler.fetch("https://example.com")
        if content:
            links = crawler.parse(content)
            self.ui.append_text(f"Found {len(links)} links.")
            crawler.save(links)
        else:
            self.ui.append_text("Failed to fetch content.")
