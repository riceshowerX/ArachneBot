# src/storage/file_storage.py
import os

class FileStorage:
    def __init__(self, directory='data/processed/'):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def save(self, filename, content):
        path = os.path.join(self.directory, filename)
        with open(path, 'w') as file:
            file.write(content)
        print(f"Data saved to {path}")
