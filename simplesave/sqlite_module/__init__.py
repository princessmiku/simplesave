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
import sqlite3
from datetime import datetime
from sqlite3 import OperationalError

from simplesave.default_functions import DefaultStorageFunctions


def _key_type_to_str(key_type: any):
    if key_type == int:
        return "INTEGER"
    if key_type == float:
        return "REAL"
    if key_type == str:
        return "TEXT"
    if key_type == json:
        return "TEXT"
    if key_type == bool:
        return "INTEGER"
    if key_type == datetime:
        return "TEXT"


def _key_str_to_type(key_type: str):

    if key_type == "INTEGER":
        return int
    if key_type == "REAL":
        return float
    if key_type == "TEXT":
        return str


class SQLiteStorage(DefaultStorageFunctions):

    def __init__(self, **kwargs):
        if "file_path" in kwargs:
            file_path = kwargs["file_path"]
        else:
            file_path = "simplesave.sqlite3"
        self.__autocommit = True
        if "autocommit" in kwargs:
            if isinstance(kwargs["autocommit"], bool):
                self.__autocommit = kwargs["autocommit"]
        self._connection: sqlite3.Connection = sqlite3.connect(file_path)
        self._table_structure: dict[str, dict[str, any]] = {}
        self._custom_types: dict[str, dict[str, any]] = {}
        self._generate_storage()
        self._load_structure()
        super().__init__()

    def get_value(self, path: str) -> any:
        _table, _from, _where, _column = self._transform_path(path)
        try:
            if not _from:
                return self._connection.execute(f"SELECT * FROM {_table}").fetchall()
            if not _where:
                return self._connection.execute(f"SELECT {_from} FROM {_table}").fetchall()
            if not _column:
                return self._connection.execute(f"SELECT * FROM {_table} WHERE {_from} = {_where}").fetchone()
            return self._connection.execute(f"SELECT {_column} FROM {_table} WHERE {_from} = {_where}").fetchone()
        except OperationalError as err:
            return self._error_handler(err, _table, _from, _where, _column, None)

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
        if self.__autocommit:
            self._connection.commit()

    def _create_table(self, table: str, primary_key: str, key_type: any):
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS {table}({primary_key} {_key_type_to_str(key_type)})"
        )
        try:
            self._add_custom_type(table, primary_key, key_type)
        except TypeError:
            pass
        if not table in self._table_structure:
            self._table_structure[table] = {}
        self._table_structure[table][primary_key] = key_type
        self._autocommit()

    def _delete_table(self, table: str):
        pass

    def rename_table(self, table: str, new_table: str):
        pass

    def _add_column(self, table: str, column: str, col_type: any):
        if not table in self._table_structure:
            self._create_table(table, column, col_type)
        else:
            if column in self._table_structure[table]:
                return
            col_type_name = _key_type_to_str(col_type)
            if col_type == datetime:
                self._add_custom_type(column, col_type)
            elif col_type == json:
                print("add json")
                self._add_custom_type(column, col_type)
            elif col_type == bool:
                self._add_custom_type(column, col_type)
            self._connection.execute(
                f"ALTER TABLE {table} ADD {column} {col_type_name}"
            )

    def _change_column(self, table: str, column: str, col_type: any):
        pass

    def _delete_column(self, table: str, column: str, col_type: any):
        pass

    def rename_column(self, table: str, column_old_name: str, column_new_name: str):
        pass

    def _error_handler(self, err: OperationalError, _table: str, _from: str,
                       _where: str, _column: str, value_type: any):
        if "no such table" in err.args[0] or "no such column" in err.args[0]:
            if _table and _from:
                vt = str
                if value_type:
                    vt = value_type
                elif _where and _where.isnumeric():
                    vt = int
                self._add_column(_table, _from, vt)
                if _column:
                    c_vt = str
                    if value_type:
                        c_vt = value_type
                    self._add_column(_table, _column, c_vt)
                return
            raise KeyError('table or column not found, not enough information for create one')
        else:
            print("no", err.args)

    def _load_simple_save_table(self):
        result = self._connection.execute(
            f"SELECT name, type FROM pragma_table_info('simplesave_types')"
        ).fetchall()
        if not result:
            return
        self._table_structure["simplesave_types"] = {}
        for _key, _type in result:
            self._table_structure["simplesave_types"][_key] = _key_str_to_type(_type)

    def _load_custom_types(self):
        col_key_val = self._connection.execute(
            "SELECT column_table, column_key, column_type FROM simplesave_types"
        ).fetchall()
        for table, key, val in col_key_val:
            if table not in self._custom_types:
                self._custom_types[table] = {}
            self._custom_types[table][key] = val

    def _load_structure(self):
        self._table_structure = {}
        self._load_custom_types()
        tables = self._connection.execute(
            "SELECT name FROM sqlite_schema WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
        for table in tables:
            table_name = table[0]
            if table_name == "simplesave_types": continue
            self._table_structure[table_name] = {}
            result = self._connection.execute(
                f"SELECT name, type FROM pragma_table_info('{table_name}')"
            ).fetchall()
            for _name, _type, *_ in result:
                if _type == "INTEGER":
                    self._table_structure[table_name][_name] = int
                elif _type == "REAL":
                    self._table_structure[table_name][_name] = float
                elif _type == "TEXT":
                    self._table_structure[table_name][_name] = str
                else:
                    if table_name in self._custom_types and _name in self._custom_types[_name]:
                        val_type = self._custom_types[table_name][_name]
                        if val_type == "DATE":
                            self._table_structure[table_name][_name] = datetime
                        elif val_type == "JSON":
                            self._table_structure[table_name][_name] = json
                        elif val_type == "BOOLEAN":
                            self._table_structure[table_name][_name] = bool
                        else:
                            self._table_structure[table_name][_name] = str
                    else:
                        self._table_structure[table_name][_name] = str

    def _generate_storage(self):
        self._load_simple_save_table()
        self._add_column("simplesave_types", "column_table", str)
        self._add_column("simplesave_types", "column_key", str)
        self._add_column("simplesave_types", "column_type", str)
        self._load_simple_save_table()
        self._load_custom_types()

    def _add_custom_type(self, col_table: str, col_key: str, col_type: any):
        if not col_type in [datetime, json, bool]:
            raise TypeError('Unsupported type for custom types')
        col_type_name = ""
        if col_type == datetime:
            col_type_name = "DATETIME"
        elif col_type == json:
            col_type_name = "JSON"
        elif col_type == bool:
            col_type_name = "BOOLEAN"
        else:
            TypeError('Unsupported type for custom types')
        self._connection.execute(
            f"INSERT INTO simplesave_types (column_table, column_key, column_type) "
            f"VALUES('{col_table}', '{col_key}', '{col_type_name}')"
        )
        self._connection.commit()
        if col_table not in self._custom_types:
            self._custom_types[col_table] = {}
        self._custom_types[col_table][col_key] = col_type
        return

    @staticmethod
    def _transform_path(path: str) -> tuple[str, str | None, str | None, str | None]:
        if path.count(".") > 3 or path == '':
            raise KeyError('SQLite storage does only support a 1-4 deep path x.x.x.x')
        _table, _from, _where, _column, *e = path.split(".") + [None, None, None]
        return _table, _from, _where, _column
