import json
import re

class JSONLFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as jsonl_file:
            for line in jsonl_file:
                yield line

class JSONLParser:
    def parse(self, json_str):
        json_data = json.loads(json_str)
        return json_data["data"], {"entities": json_data["label"]}

class JSONLCleaner:
    def clean(self, data):
        return re.sub(r"\\\\\\\\n", "", data)

class JSONLConv:
    def __init__(self, file_path):
        self.file_reader = JSONLFileReader(file_path)
        self.json_parser = JSONLParser()
        self.json_cleaner = JSONLCleaner()

    def convert(self):
        data = []
        for json_str in self.file_reader.read():
            json_data, entities = self.json_parser.parse(json_str)
            json_data = self.json_cleaner.clean(json_data)
            data.append((json_data, entities))
        return data