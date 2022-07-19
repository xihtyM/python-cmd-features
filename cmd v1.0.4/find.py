# Find nth occurence in a string

def find(text: str, tofind: str, occurences: int) -> int:
    start = 0;
    while(occurences >= 0):
        start = text.find(tofind, start + len(tofind));
        occurences -= 1;
    return start + 1;
