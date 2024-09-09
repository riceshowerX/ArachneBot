# src/crawler/simple_crawler.py
import requests
from .base_crawler import BaseCrawler
from config.settings import Settings

class SimpleCrawler(BaseCrawler):
    def fetch(self, url):
        try:
            response = requests.get(url, headers=Settings.HEADERS, timeout=Settings.TIMEOUT)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse(self, content):
        # 假设抓取的是HTML页面，解析可以使用BeautifulSoup
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find_all('a')  # 简单示例，返回所有链接

    def save(self, data):
        # 将数据保存为文本文件
        with open("data/processed/links.txt", "w") as file:
            for link in data:
                file.write(f"{link.get('href')}\n")
