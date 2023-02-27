from .default_functions import DefaultStorageFunctions
from .internal import InternalStorage

INTERNAL = "internal"
SQLITE = "SQLite"
JSON = "json"
CSV = "csv"
XML = "xml"


class Storage:

    def __init__(self, connection_type: str, file_path: str = None):
        if connection_type == INTERNAL:
            self.__data: DefaultStorageFunctions = InternalStorage()
        #elif connection_type == JSON:
            #self.__data: DefaultStorageFunctions = JsonStorage()

    def get(self, path: str | list[str], *, fill: list[str | int] = None) -> any:
        path: str = self._build_path(path, fill)
        return self.__data.get_value(path)

    def set(self, path: str | list[str], value: any, *, fill: list[str | int] = None):
        path: str = self._build_path(path, fill)
        self.__data.set_value(path, value)

    def exists(self, path: str | list[str], *, fill: list[str | int] = None) -> bool:
        path: str = self._build_path(path, fill)
        return self.__data.exists_value(path)

    def save(self):
        self.__data.save()

    @staticmethod
    def _build_path(path: str | list[str], fill: list[str | int] = None) -> str:
        if isinstance(path, list):
            path: str = ".".join(path)
        if not fill and not path.__contains__("?"):
            return path
        if path.__contains__("?") and not fill:
            raise TypeError("The path string contains ? variables, but therese no fill options for it")
        elif fill and not path.__contains__("?"):
            raise AttributeError("There fill options available, but the path string does not contains ? variables")
        if path.count("?") != len(fill):
            raise IndexError("The length of ? variables in path are not the same length in fill")
        fill = list(map(str, fill))
        return ''.join(elem if elem != '?' else fill.pop(0) for elem in path)
