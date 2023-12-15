def get_input(filepath: str, split: str = "\n") -> list[str]:
    with open(filepath, "r") as fp:
        string = fp.read()
    return string.split(split)


def bin2int(binary: str) -> int:
    return int(binary, base=2)
