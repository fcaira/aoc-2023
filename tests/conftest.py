import os

from typing import List


class FileRetriever:
    def __init__(self, inputs_path):
        self.inputs_path = inputs_path

    def get_input(self, day: str, split="\n") -> List[str]:
        with open(os.path.join(self.inputs_path, f"{day}"), "r") as fp:
            string = fp.read()
        if not split:
            return string
        return string.split(split)


def bin2int(binary: str) -> int:
    return int(binary, base=2)
