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

from abc import ABC, abstractmethod


class DefaultStorageFunctions(ABC):

    @abstractmethod
    def get_value(self, path: str) -> any:
        """
        Get a value from the storage
        :param path:
        :return:
        """
        pass

    @abstractmethod
    def get_value_by_index(self, path: str, index: int):
        """
        Get a value from the storage, if this a list, get the item at the position
        :param path:
        :param index:
        :return:
        """
        pass

    @abstractmethod
    def set_value(self, path: str, value: any):
        """
        Set a value on the given path, its override the value if there's one
        :param path:
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def add_value(self, path: str, value: any):
        """
        Add a value the list in a path, its generate automatically a list (without data loss), if there's no list
        :param path:
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def exists_path(self, path: str) -> bool:
        """
        Check if path exists
        :param path:
        :return:
        """
        pass

    @abstractmethod
    def get_value_type(self, path: str) -> type:
        """
        Get the type of the value
        :param path:
        :return:
        """
        pass

    @abstractmethod
    def delete(self, path):
        """
        Delete all data in the path with the path itself (not the complete only the last)
        :param path:
        :return:
        """

    @abstractmethod
    def remove_value_by_value(self, path: str, value: any):
        """
        Remove from a list a value by the value
        :param path:
        :param value:
        :return:
        """
        pass

    @abstractmethod
    def remove_value_by_index(self, path: str, index: int):
        """
        Remove from a list a value with the index
        :param path:
        :param index:
        :return:
        """
        pass

    @abstractmethod
    def null(self, path: str):
        """
        Set a path entry to null, its delete all sub data
        :param path:
        :return:
        """
        pass

    @abstractmethod
    def save(self):
        """
        Save the current storage
        :return:
        """
        pass



