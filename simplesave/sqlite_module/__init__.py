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

import sqlite3

from simplesave import DefaultStorageFunctions


class SQLiteStorage(DefaultStorageFunctions):

    def __init__(self, **kwargs):
        if kwargs.__contains__("file_path"):
            file_path = kwargs["file_path"]
        else:
            file_path = "simplesave.sqlite"
        self._connection = sqlite3.connect(file_path)
        super().__init__()

    def get_value(self, path: str) -> any:
        pass

    def get_value_by_index(self, path: str, index: int):
        pass

    def set_value(self, path: str, value: any):
        pass

    def add_value(self, path: str, value: any):
        pass

    def exists_path(self, path: str) -> bool:
        pass

    def get_value_type(self, path: str) -> type:
        pass

    def delete(self, path):
        pass

    def remove_value_by_value(self, path: str, value: any):
        pass

    def remove_value_by_index(self, path: str, index: int):
        pass

    def null(self, path: str):
        pass

    def save(self):
        pass
