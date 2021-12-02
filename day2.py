import os


def read_input():
    with open(f"inputs/{os.path.basename(__file__).split('.')[0]}.txt") as text_input:
        return list(map(lambda k: k.strip("\n").split(), text_input.readlines()))


def calculate_position():
    inputs = read_input()

    horizontal_position = 0
    depth = 0

    for position in inputs:
        if position[0] == "forward":
            horizontal_position += int(position[1])
        elif position[0] == "up":
            depth -= int(position[1])
        elif position[0] == "down":
            depth += int(position[1])

    print(horizontal_position * depth)


def calculate_position_with_aim():
    inputs = read_input()

    horizontal_position = 0
    depth = 0
    aim = 0

    for position in inputs:
        if position[0] == "forward":
            horizontal_position += int(position[1])

            if aim != 0:
                depth += aim * int(position[1])

        elif position[0] == "up":
            aim -= int(position[1])
        elif position[0] == "down":
            aim += int(position[1])

    print(horizontal_position * depth)


if __name__ == "__main__":
    calculate_position()
    calculate_position_with_aim()
