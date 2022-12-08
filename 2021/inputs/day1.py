import os


def read_input():
    with open(f"inputs/{os.path.basename(__file__).split('.')[0]}.txt") as text_input:
        return list(map(lambda k: int(k.strip("\n")), text_input.readlines()))


def count_increases():
    inputs = read_input()
    counts = 0

    for index, measure in enumerate(inputs):
        if index == 0:
            continue

        if measure > inputs[index - 1]:
            counts += 1

    print(counts)


def count_three_sized_window_increases():
    inputs = read_input()
    counts = 0

    for index, measure in enumerate(inputs):
        if index + 3 > len(inputs) - 1:
            break

        current_window_sum = inputs[index] + inputs[index + 1] + inputs[index + 2]
        next_window_sum = inputs[index + 1] + inputs[index + 2] + inputs[index + 3]

        if current_window_sum < next_window_sum:
            counts += 1

    print(counts)


if __name__ == "__main__":
    count_increases()
    count_three_sized_window_increases()
