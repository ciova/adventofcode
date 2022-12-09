from base import Helper


class DayTwo(Helper):
    def __init__(self):
        Helper.__init__(self)

        self.input = self.get_input(2)
        self.choice_points_map = {"X": 1, "Y": 2, "Z": 3}

    def solve_part1(self):
        points = 0
        game_result_map = {
            "A": {"X": 3, "Y": 6, "Z": 0},
            "B": {"X": 0, "Y": 3, "Z": 6},
            "C": {"X": 6, "Y": 0, "Z": 3},
        }
        for game in self.input:
            opponent, me = game.strip('\n').split()
            points += game_result_map[opponent][me] + self.choice_points_map[me]

        print(points)

    def solve_part2(self):

        points = 0
        game_result_map = {
            "A": {3: "X", 6: "Y", 0: "Z"},
            "B": {0: "X", 3: "Y", 6: "Z"},
            "C": {6: "X", 0: "Y", 3: "Z"},
        }
        strategy = {"X": 0, "Y": 3, "Z": 6}

        for game in self.input:
            opponent, me = game.strip('\n').split()
            points += strategy[me] + self.choice_points_map[game_result_map[opponent][strategy[me]]]

        print(points)


if __name__ == "__main__":
    day_two = DayTwo()
    day_two.solve_part1()
    day_two.solve_part2()
