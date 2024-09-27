import os
import json

class FileManager:
    
    def __init__(self, base_dir=None):
        if base_dir: 
            self.base_dir = base_dir
        else:
            self.base_dir = os.getcwd()

    def _get_full_path(self, file_path):
        full_path = os.path.join(self.base_dir, file_path)
        os.makedirs(self.base_dir, exist_ok=True)
        return full_path

    def put_into_json(self, file_path, content):
        file_path = self._get_full_path(file_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(content, file, ensure_ascii=False, indent=4)
    
        print(f'{file_path} created.')
    