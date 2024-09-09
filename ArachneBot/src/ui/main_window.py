# src/ui/main_window.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from .event_handler import EventHandler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArachneBot")
        self.setGeometry(300, 300, 600, 400)

        # 创建UI组件
        self.text_edit = QTextEdit(self)
        self.start_button = QPushButton('Start Crawl', self)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.start_button)

        # 中央窗口
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 事件绑定
        self.event_handler = EventHandler(self)
        self.start_button.clicked.connect(self.event_handler.start_crawl)

    def append_text(self, text):
        self.text_edit.append(text)
