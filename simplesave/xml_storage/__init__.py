from default_functions import DefaultStorageFunctions


class XmlStorage(DefaultStorageFunctions):

    def __init__(self, file_path: str = None):
        pass

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

