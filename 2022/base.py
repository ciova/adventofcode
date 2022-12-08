

class Helper:
    @staticmethod
    def get_input(day):
        with open(f"inputs/day{day}.txt") as f:
            return f.readlines()
        