import json
from pathlib import Path


class Localization(object):
    def __init__(self, translation_dir, language="en"):
        self.__translation_dir = Path(translation_dir)
        self.__dictionary = {}
        self._language = language

        self.__load()

    def __getattr__(self, key):
        return self.__dictionary.get(key, "i10n:{}".format(key))

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        self.__load()

    def __load(self):
        file_extension = ".json"
        fine_name = self.language + file_extension
        file_path = self.__translation_dir / fine_name

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.__dictionary = json.load(file)
        except FileNotFoundError:
            msg = "Translation file not found: '{0}'.".format(file_path)
            raise FileNotFoundError(msg)
