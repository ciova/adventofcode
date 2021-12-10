import numpy as np


def read_input():
    with open("inputs/day5.txt") as t_input:
        return t_input.read()


def create_list_with_coords():
    inputs = read_input()
    all_values = []

    x_groups = []
    y_groups = []

    for line in inputs.split("\n"):
        x_group = []
        y_group = []

        for coord in line.split(" -> "):
            all_values += [int(coord[0]), int(coord[2])]

            x_group.append(int(coord[0]))
            y_group.append(int(coord[2]))

        x_groups.append(x_group)
        y_groups.append(y_group)

    return max(all_values), zip(x_groups, y_groups)


def determine_points():
    max_number, inputs = create_list_with_coords()
    print(inputs.__next__())


if __name__ == "__main__":
    determine_points()
