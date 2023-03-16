from random import randrange
from dataclasses import dataclass


### CONFIG ###
BOARD_HEIGHT = 8
BOARD_WIDTH = 8

EMPTY = " "
PLAYER_1_CHECKER = "@"
PLAYER_2_CHECKER = "#"

IN_A_ROW_TO_WIN = 4
#############


@dataclass
class Player:
    human: bool
    checker: str
    win_count: int
    player_num: int

    def score_str(self):
        player_type = "Human" if self.human else "Computer"
        return f"Player {str(self.player_num)} ({player_type}) Score: {str(self.win_count)}"


class Board:
    def __init__(self) -> None:
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.grid = [[EMPTY for _ in range(0, self.height)]
                     for _ in range(0, self.width)]

    def __str__(self) -> str:
        string = "\n"
        for y in range(self.height-1, -1, -1):
            string += "|"
            for x in range(0, self.width):
                cell = self.grid[x][y]
                string += f" {cell} |"
            string += "\n"

        string += "-" * (self.width * 4 + 1)
        string += "\n"

        for num in range(0, self.width):
            string += f"  {num+1} "
        return string

    def drop_checker(self, column: int, player: Player):
        if EMPTY not in self.grid[column]:
            raise ValueError

        for index, y in enumerate(self.grid[column]):
            if y == EMPTY:
                self.grid[column][index] = player.checker
                return


def main():
    board = Board()
    player1 = Player(human=True, checker=PLAYER_1_CHECKER,
                     win_count=0, player_num=1)
    player2 = Player(human=False, checker=PLAYER_2_CHECKER,
                     win_count=0, player_num=2)
    game_loop(board, player1, player2)


def game_loop(board: Board, player1: Player, player2: Player):
    print(board)

    game_over = False
    current_player = player1
    while not game_over:
        take_turn(board, current_player)
        print(board)
        # check win
        current_player = swap_current_player(current_player, player1, player2)


def swap_current_player(current: Player, player1: Player, player2: Player):
    return player2 if current == player1 else player1


def take_turn(board: Board, player: Player):
    while True:
        try:
            column = get_human_input() if player.human else get_computer_input()
            board.drop_checker(column, player)
        except ValueError:
            if player.human:
                print("Invalid Move!")
            continue
        return


def get_computer_input():
    # dumb
    return randrange(0, BOARD_WIDTH)


def get_human_input() -> int:
    while True:
        print(f'Enter column (1-{BOARD_WIDTH}):')
        str_in = input('> ')

        int_in = int(str_in)

        if int_in < 1 or int_in > BOARD_WIDTH:
            raise ValueError

        return int_in-1


def game_has_winner(board: Board) -> bool:
    pass

    # check cols
    for col in board.grid:

        # check rows

        # check diags


def has_winner(checkers: list[str]) -> bool:
    for index in range(0, len(checkers)-IN_A_ROW_TO_WIN):
        checker = checkers[index]
        if checker == EMPTY:
            continue
        winner = False
        for i in range(index, index+IN_A_ROW_TO_WIN):





if __name__ == '__main__':
    main()
