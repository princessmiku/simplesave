# Copyright (c) 2023 Miku
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os
from json import JSONDecodeError

from simplesave.internal_module import InternalStorage


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
