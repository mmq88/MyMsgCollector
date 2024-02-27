import tomlkit

class DataManager:
    def __init__(self):
        self.data = None
        self.__load('./local/config.toml')

    def __load(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self.data = tomlkit.parse(f.read())