# src/parser/html_parser.py
from .base_parser import BaseParser
from bs4 import BeautifulSoup

class HtmlParser(BaseParser):
    def parse(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        return soup.find_all('p')  # 返回页面中的所有段落
