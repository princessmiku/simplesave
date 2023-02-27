from json_module import JsonStorage
from kpv_storage import KpvStorage
from .default_functions import DefaultStorageFunctions
from .internal_module import InternalStorage

# Connection types
INTERNAL = "internal_module"
#SQLITE = "SQLite"
JSON = "json_module"
#CSV = "csv"
#XML = "xml"
KPV = "kpv"  # own data storage type, Key Pont Value


class Storage:

    def __init__(self, connection_type: str, file_path: str = None):
        if connection_type == INTERNAL:
            self._data: DefaultStorageFunctions = InternalStorage()
        elif connection_type == JSON:
            self._data: DefaultStorageFunctions = JsonStorage(file_path)
        elif connection_type == KPV:
            self._data: DefaultStorageFunctions = KpvStorage(file_path)
        else:
            raise NameError("Selected connection type are not supported, check if you spell it right")

    def get(self, path: str | list[str], *, fill: list[str | int] = None) -> any:
        path: str = self._build_path(path, fill)
        return self._data.get_value(path)

    def set(self, path: str | list[str], value: any, *, fill: list[str | int] = None):
        path: str = self._build_path(path, fill)
        self._data.set_value(path, value)

    def exists(self, path: str | list[str], *, fill: list[str | int] = None) -> bool:
        path: str = self._build_path(path, fill)
        return self._data.exists_value(path)

    def delete(self, path: str | list[str], *, fill: list[str | int] = None):
        path: str = self._build_path(path, fill)
        self._data.delete(path)

    def save(self):
        self._data.save()

    @staticmethod
    def _build_path(path: str | list[str], fill: list[str | int] = None) -> str:
        if isinstance(path, list):
            path: str = ".".join(path)
        if not fill and not path.__contains__("?"):
            return path.lower()
        if path.__contains__("?") and not fill:
            raise TypeError("The path string contains ? variables, but therese no fill options for it")
        elif fill and not path.__contains__("?"):
            raise AttributeError("There fill options available, but the path string does not contains ? variables")
        if path.count("?") != len(fill):
            raise IndexError("The length of ? variables in path are not the same length in fill")
        fill = list(map(str, fill))
        return ''.join(elem if elem != '?' else fill.pop(0) for elem in path).lower()
