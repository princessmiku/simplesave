from abc import ABC, abstractmethod


class DefaultStorageFunctions(ABC):

    @abstractmethod
    def get_value(self, path: str) -> any:
        pass

    @abstractmethod
    def set_value(self, path: str, value: any):
        pass

    @abstractmethod
    def exists_value(self, path: str) -> bool:
        pass

    @abstractmethod
    def delete(self, path):
        pass

    @abstractmethod
    def save(self):
        pass
