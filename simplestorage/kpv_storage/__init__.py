import json
import os
import re

from default_functions import DefaultStorageFunctions


def load(file_path):
    data = {}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # key value for data
        current_key_set: list[str, str] = None
        # keys that allow multi lines
        multi_keys = ('"', "[", "{")
        multi_keys_end = ('"', "]", "}")
        # counts if it finds the end
        o_c_count = 0
        multi_line_value = ""
        key = None
        # Ending of "
        a_ending = True
        for line in lines:
            # if line is a comment or is empty, skip it
            if line.startswith("#") or line == "\n":
                continue

            if o_c_count == 0:
                if not line.__contains__("="):
                    raise KeyError(f"Line {line} is not formatted correctly")
                # key, value
                kv = line.split("=", 1)
                key = kv[0].lower().rstrip()
                value = kv[1].lstrip()
                r_strip_value = value.replace(" ", "").replace("\n", "").replace("\\\"", "").replace("\t", "")
                if value.startswith(multi_keys[0]):
                    current_key_set = [multi_keys[0], multi_keys_end[0]]
                elif value.startswith(multi_keys[1]):
                    current_key_set = [multi_keys[1], multi_keys_end[1]]
                elif value.startswith(multi_keys[2]):
                    current_key_set = [multi_keys[2], multi_keys_end[2]]
                else:
                    current_key_set = None
                if not current_key_set or (
                        r_strip_value.startswith(current_key_set[0]) and r_strip_value.endswith(current_key_set[1])
                ):
                    data[key] = value.rstrip("\n")
                    continue
            if current_key_set[0] == '"':
                for_for = value if value else line
                for c in for_for.replace("\\\"", ""):
                    if c == '"':
                        if a_ending:
                            a_ending = False
                            o_c_count += 1
                        else:
                            a_ending = True
                            o_c_count -= 1
            else:
                o_c_count = o_c_count + line.count(current_key_set[0]) - line.count(current_key_set[1])
            if value:
                #if current_key_set[0] != '"':
                #    value.rstrip("\n")
                multi_line_value += value
                value = None
            else:
                multi_line_value += line
            if o_c_count == 0:
                if multi_keys[0] == current_key_set[0]:
                    data[key] = multi_line_value.rstrip("\n")
                else:
                    data[key] = json.loads(multi_line_value.rstrip("\n"))
                multi_line_value = ""
                a_ending = True
    return data


class KpvStorage(DefaultStorageFunctions):

    def __init__(self, file_path: str = None):
        self._data = {}
        if file_path is None:
            file_path = "simplestorage.kvp"
        self.__file_path = file_path
        try:
            if os.stat(file_path).st_size > 0:
                self._data = load(self.__file_path)
        except FileNotFoundError:
            pass
        print(self._data)

    def get_value(self, path: str) -> any:
        pass

    def set_value(self, path: str, value: any):
        pass

    def exists_value(self, path: str) -> bool:
        pass

    def delete(self, path):
        pass

    def save(self):
        pass
