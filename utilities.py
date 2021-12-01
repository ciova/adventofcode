def read_input():
    with open("input.txt") as text_input:
        return list(map(lambda k: int(k.strip("\n")), text_input.readlines()))