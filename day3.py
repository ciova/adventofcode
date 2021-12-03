import os


def read_input():
    with open(f"inputs/{os.path.basename(__file__).split('.')[0]}.txt") as text_input:
        return list(map(lambda k: k.strip("\n"), text_input.readlines()))


def convert_binary_to_decimal(binary_number):
    decimal = 0

    for index, digit in enumerate(binary_number[::-1]):
        decimal += (2 ** index) * int(digit)

    return decimal


def calculate_gama_and_epsilon():
    inputs = read_input()

    count_digit_1 = 0
    count_digit_0 = 0
    epsilon_binary_number = ""
    gama_binary_number = ""

    for i in range(len(inputs[0])):
        for elem in inputs:
            if elem[i] == "1":
                count_digit_1 += 1
            elif elem[i] == "0":
                count_digit_0 += 1

        if count_digit_1 > count_digit_0:
            gama_binary_number += "1"
        else:
            gama_binary_number += "0"

        count_digit_1 = 0
        count_digit_0 = 0

    for digit in gama_binary_number:
        if digit == "1":
            epsilon_binary_number += "0"
        else:
            epsilon_binary_number += "1"

    gama_decimal_number = convert_binary_to_decimal(gama_binary_number)
    epsilon_decimal_number = convert_binary_to_decimal(epsilon_binary_number)

    print(gama_decimal_number * epsilon_decimal_number)


def calculate_oxygen_and_co2(inputs):
    count_digit_1 = 0
    count_digit_0 = 0

    placeholder = inputs[:]

    temp_ones = []
    temp_zeros = []

    oxygen_rating = ""
    co2_rating = ""

    for i in range(len(inputs[0])):
        if len(placeholder) == 1:
            oxygen_rating = placeholder[0]

        for elem in placeholder:
            if elem[i] == "1":
                count_digit_1 += 1
                temp_ones.append(elem)
            elif elem[i] == "0":
                count_digit_0 += 1
                temp_zeros.append(elem)

        if count_digit_1 >= count_digit_0:
            placeholder = temp_ones[:]
        else:
            placeholder = temp_zeros[:]

        temp_ones = []
        temp_zeros = []

        count_digit_1 = 0
        count_digit_0 = 0

    if not oxygen_rating:
        oxygen_rating = placeholder[0]

    placeholder = inputs[:]

    for i in range(len(inputs[0])):
        if len(placeholder) == 1:
            co2_rating = placeholder[0]

        for elem in placeholder:
            if elem[i] == "1":
                count_digit_1 += 1
                temp_ones.append(elem)
            elif elem[i] == "0":
                count_digit_0 += 1
                temp_zeros.append(elem)

        if count_digit_1 >= count_digit_0:
            placeholder = temp_zeros[:]
        else:
            placeholder = temp_ones[:]

        temp_ones = []
        temp_zeros = []

        count_digit_1 = 0
        count_digit_0 = 0

    if not co2_rating:
        co2_rating = placeholder[0]

    print(convert_binary_to_decimal(co2_rating) * convert_binary_to_decimal(oxygen_rating))


if __name__ == "__main__":
    calculate_gama_and_epsilon()
    calculate_oxygen_and_co2(read_input())
