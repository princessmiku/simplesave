from simplestorage.default_functions import DefaultStorageFunctions


class InternalStorage(DefaultStorageFunctions):

    def __init__(self, data: dict = None):
        if not data:
            self._data = {}
        else:
            self._data = data

    def get_value(self, path: str) -> any:
        arguments: list[str] = path.split(".")
        arguments_length: int = len(arguments) - 1
        arg: str
        stage = self._data
        for index, arg in enumerate(arguments):
            if index != arguments_length:
                stage = stage.get(arg, {})
            else:
                if arg == "*":
                    return list(stage.values())
                return stage.get(arg, None)
        raise KeyError("Error, path not found, problems with path generation")

    def set_value(self, path: str, value: any):
        arguments: list[str] = path.split(".")
        arguments_length: int = len(arguments) - 1
        arg: str
        stage = self._data
        for index, arg in enumerate(arguments):
            if index != arguments_length:
                stage[arg] = stage.get(arg, {})
                stage = stage[arg]
            else:
                stage[arg] = value
        # raise KeyError("Error, path not found, problems with path generation")

    def exists_path(self, path: str) -> bool:
        arguments: list[str] = path.split(".")
        arguments_length: int = len(arguments) - 1
        arg: str
        stage = self._data
        for index, arg in enumerate(arguments):
            if index != arguments_length:
                if not stage.__contains__(arg):
                    return False
                stage = stage.get(arg, {})
            else:
                return True if stage.get(arg) else False
        raise KeyError("Error, path not found, problems with path generation")

    def delete(self, path):
        arguments: list[str] = path.split(".")
        arguments_length: int = len(arguments) - 1
        arg: str
        stage = self._data
        for index, arg in enumerate(arguments):
            if index != arguments_length:
                if not stage.__contains__(arg):
                    return
                stage = stage.get(arg, {})
            else:
                if stage.__contains__(arg):
                    stage.pop(arg)
                return
        raise KeyError("Error, path not found, problems with path generation")

    def save(self):
        raise NotImplementedError(
            "This function is not available in the internal_module mode, because it does not support saving."
        )

    def get_value_by_index(self, path: str, index: int):
        pa_va = self.get_value(path)
        if isinstance(pa_va, list):
            return pa_va[index]
        raise TypeError(f"Path {path} is not a list")

    def add_value(self, path: str, value: any):
        # path value
        pa_va = self.get_value(path)
        if isinstance(pa_va, list):
            pa_va.append(value)
            self.set_value(path, pa_va)
        else:
            self.set_value(path, [pa_va, value])

    def get_value_type(self, path: str) -> type:
        return type(self.get_value(path))

    def remove_value_by_value(self, path: str, value: any):
        pa_va: list = self.get_value(path)
        if isinstance(pa_va, list):
            pa_va.remove(value)
            self.set_value(path, pa_va)
        else:
            raise TypeError(f"Path {path} is not a list")

    def remove_value_by_index(self, path: str, index: int):
        pa_va: list = self.get_value(path)
        if isinstance(pa_va, list):
            pa_va.pop(index)
            self.set_value(path, pa_va)
        else:
            raise TypeError(f"Path {path} is not a list")

    def null(self, path: str):
        self.set_value(path, None)
