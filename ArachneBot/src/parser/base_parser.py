# src/parser/base_parser.py
from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, data):
        """解析爬虫抓取到的数据"""
        pass
