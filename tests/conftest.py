from typing import List


def get_input(filepath: str, split="\n") -> List[str]:
    with open(filepath, "r") as fp:
        string = fp.read()
    if not split:
        return string
    return string.split(split)


def bin2int(binary: str) -> int:
    return int(binary, base=2)
