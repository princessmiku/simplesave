import json
import os
from json import JSONDecodeError

from internal_module import InternalStorage


class JsonStorage(InternalStorage):

    def __init__(self, **kwargs):

        if kwargs.__contains__("file_path"):
            file_path = kwargs["file_path"]
        else:
            file_path = "simplesave.json"
        try:
            if os.stat(file_path).st_size == 0:
                json_data = {}
            else:
                json_data = json.load(open(file_path))
        except FileNotFoundError:
            json_data = {}
        except JSONDecodeError as e:
            raise e
        super().__init__(json_data)
        self.__file_path = file_path

    def set_value(self, path: str, value: str | int | bool | float | list | dict):
        if not isinstance(value, (str, int, bool, float, list, dict)):
            raise TypeError("Json only accept str, int, bool, float, list and dict variable types. Make sure if you"
                            "insert a list or a dictionary, there no contains any other variables")
        super().set_value(path, value)

    def save(self):
        print(self._data)
        json.dump(self._data, open(self.__file_path, mode='w'))
