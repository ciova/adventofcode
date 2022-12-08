import numpy as np


def read_input():
    with open("inputs/day4.txt") as t_input:
        return t_input.read()


class Bingo:
    def __init__(self):
        self.raw_input = read_input()

    def play(self):
        chosen_numbers = self.random_chosen_numbers()
        boards = self.create_boards()
        marked_boards = {board_number: np.array([[-1] * 5] * 5) for board_number in boards}

        excluded_boards = []
        last_winner_sum = 0

        for number in chosen_numbers:
            for board_number in boards:
                indexes = self.check_number_in_board(number, boards[board_number])
                if indexes:
                    marked_boards[board_number][indexes["row"]][indexes["column"]] = number

                    if board_number not in excluded_boards:
                        if self.validate_board(marked_boards[board_number]):
                            excluded_boards.append(board_number)
                            last_winner_sum = self.get_unmarked_numbers_sum(marked_boards[board_number],
                                                                            boards[board_number]) * number
        return last_winner_sum

    @staticmethod
    def check_number_in_board(number, board):
        for row_index, row in enumerate(board):
            for column_index, column_value in enumerate(row):
                if number == column_value:
                    return {"row": row_index, "column": column_index}

        return {}

    @staticmethod
    def _validate_rows(board):
        winner = False

        for row in board:
            if winner:
                break

            for column in row:
                if column != -1:
                    winner = True
                else:
                    winner = False
                    break

        return winner

    def validate_board(self, board):

        winner = self._validate_rows(board)
        if not winner:
            # validate columns
            transposed_board = board.swapaxes(0, 1)
            return self._validate_rows(transposed_board)

        return winner

    @staticmethod
    def get_unmarked_numbers_sum(marked_board, original_board):
        unmarked_numbers_sum = 0
        original_board_array = np.array(original_board)
        for row_index, row in enumerate(marked_board):
            for column_index, column in enumerate(row):
                if column == -1:
                    unmarked_numbers_sum += original_board_array[row_index][column_index]

        return unmarked_numbers_sum

    def random_chosen_numbers(self):
        return list(map(int, self.raw_input.split("\n")[0].split(",")))

    def create_boards(self):
        boards = {}
        board = []
        board_counter = 1

        for raw in self.raw_input.split("\n")[2:]:
            if raw:
                board.append(list(map(int, raw.split())))

                if len(board) == 5:
                    boards[board_counter] = board
                    board = []
                    board_counter += 1
            else:
                continue

        return boards


if __name__ == "__main__":
    game = Bingo()
    result = game.play()
    print(result)


