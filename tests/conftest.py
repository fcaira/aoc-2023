from typing import List, Union


def get_input(filepath: str, split="\n") -> Union[List[str], str]:
    with open(filepath, "r") as fp:
        string = fp.read()
    if not split:
        return string
    return string.split(split)


def bin2int(binary: str) -> int:
    return int(binary, base=2)
