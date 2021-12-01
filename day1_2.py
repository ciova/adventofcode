from utilities import read_input


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
    count_three_sized_window_increases()
