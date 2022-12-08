from base import Helper


class DayOne(Helper):

    def __init__(self):
        Helper.__init__(self)

        self.input = self.get_input(1)

    def solve_part1(self):
        most_calories = 0
        current_calories = 0

        for i in self.input:
            if i == '\n':
                if current_calories > most_calories:
                    most_calories = current_calories
                current_calories = 0
                continue

            current_calories += int(i.strip('\n'))

        print(most_calories)

    def solve_part2(self):
        calories = []
        current_calories = 0

        for i in self.input:
            if i == '\n':
                calories.append(current_calories)
                current_calories = 0
                continue

            current_calories += int(i.strip('\n'))

        print(sum(sorted(calories)[-3:]))


if __name__ == "__main__":
    day_one = DayOne()
    day_one.solve_part1()
    day_one.solve_part2()
