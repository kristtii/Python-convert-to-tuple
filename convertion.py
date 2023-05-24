import pickle
import sys
from jsonl_conv import JSONLConv

class Pickler:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def save(self):
        with open(self.file_name, "wb") as pkl:
            pickle.dump(self.data, pkl)

class Main:
    def __init__(self, jsonl_file_path):
        self.jsonl_file_path = jsonl_file_path

    def run(self):
        converter = JSONLConv(self.jsonl_file_path)
        result = converter.convert()
        pickler = Pickler(result, "result.pkl")
        pickler.save()
        print(result)

jsonl_f = sys.argv[1] if len(sys.argv) > 1 else '.'
main = Main(jsonl_f)
main.run()