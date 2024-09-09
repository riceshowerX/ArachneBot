# src/crawler/base_crawler.py
from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    @abstractmethod
    def fetch(self, url):
        """抓取网页数据"""
        pass

    @abstractmethod
    def parse(self, content):
        """解析抓取到的数据"""
        pass

    @abstractmethod
    def save(self, data):
        """保存数据"""
        pass
