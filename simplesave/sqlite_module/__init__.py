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
from sqlite3 import OperationalError

from simplesave.default_functions import DefaultStorageFunctions


class SQLiteStorage(DefaultStorageFunctions):

    def __init__(self, **kwargs):
        if "file_path" in kwargs:
            file_path = kwargs["file_path"]
        else:
            file_path = "simplesave.sqlite"
        self.autocommit = True
        if "autocommit" in kwargs:
            if isinstance(kwargs["autocommit"], bool):
                self.autocommit = kwargs["autocommit"]
        self._connection: sqlite3.Connection = sqlite3.connect(file_path)
        self._table_structure: dict[str, dict[str, any]] = {}
        super().__init__()

    def get_value(self, path: str) -> any:
        try:
            self._connection.execute("SELECT * FROM user").fetchall()
        except OperationalError as err:
            if "no such table" in err.args[0]:
                print("table not found")
            else:
                print("no", err.args)

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
        self._connection.commit()

    def close(self):
        self.save()
        self._connection.close()

    def _autocommit(self):
        if self.autocommit:
            self._connection.commit()

    def _create_table(self, table: str):
        pass

    def _delete_table(self, table: str):
        pass

    def rename_table(self, table: str):
        pass

    def _add_column(self, table: str, column: str, col_type: any):
        pass

    def _change_column(self, table: str, column: str, col_type: any):
        pass

    def _delete_column(self, table: str, column: str, col_type: any):
        pass

    def rename_column(self, table: str, column_old_name: str, column_new_name: str):
        pass
