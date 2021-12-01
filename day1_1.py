from utilities import read_input


def count_increases():
    inputs = read_input()
    counts = 0

    for index, measure in enumerate(inputs):
        if index == 0:
            continue

        if measure > inputs[index - 1]:
            counts += 1

    print(counts)


if __name__ == "__main__":
    count_increases()