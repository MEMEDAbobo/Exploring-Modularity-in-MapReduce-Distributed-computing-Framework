import json

class DataStore:
    def save(self, key, value):
        pass

    def load(self, key):
        pass

class MemoryDataStore(DataStore):
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def load(self, key):
        return self.data.get(key)


class FileDataStore(DataStore):
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def save(self, key, value):
        self.data[key] = value
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def load(self, key):
        with open(self.filename, 'r') as f:
            self.data = json.load(f)
        return self.data.get(key)

