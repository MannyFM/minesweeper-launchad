from minesweeper import Minesweeper
import launchpad_py as launchpad
import time
from copy import copy, deepcopy

SIZE = 8
N_MINE = 10
TIMEOUT = 0.010
color_map = {'.': 3, 'M': 72, '!': 95, 0: 0, 1: 67, 2: 21, 3: 13, 4: 52, 5: 78, 6: 48, 7: 108, 8: 5}


class Game:
    def __init__(self):
        self.sweeper = None
        self.old_board = None
        self.lp = launchpad.LaunchpadMk2()
        if not self.lp.Open():
            print("Error opening LaunchpadMK2")
            exit(1)
        self.lp.LedAllOn(0)

    def start(self):
        self.sweeper = Minesweeper(SIZE, N_MINE)
        self.sweeper.start()
        self.sweeper.print_board()
        self.old_board = [[None for _ in range(SIZE)] for _ in range(SIZE)]
        self.set_color_bar()
        while True:
            self.print_visible()
            x, y = self.read_button()
            y -= 1
            print("you choose", x, y)
            if not (0 <= x < SIZE and 0 <= y < SIZE):
                print("FUCKOFF")
                continue
            self.old_board = deepcopy(self.sweeper.is_visible)
            status = self.choose(x, y)
            print("status", status)
            if self.sweeper.status == 'G':
                self.game_over()
                break
            if self.sweeper.status == 'W':
                self.winner()
                break
            # time.sleep(TIMEOUT)

    def print_board(self):
        bd = self.sweeper.board
        self.lp.LedAllOn(0)
        self.set_color_bar()
        for i in range(SIZE):
            for j in range(SIZE):
                pp = bd[i][j]
                # print(j, i, color_map[pp])
                self.lp.LedCtrlXYByCode(j, i + 1, color_map[pp])
                time.sleep(TIMEOUT)
        self.sweeper.print_board()

    def print_visible(self):
        bd = self.sweeper.board
        # self.lp.LedAllOn(0)
        # self.set_color_bar()
        for i in range(SIZE):
            for j in range(SIZE):
                if self.sweeper.is_visible[i][j] == self.old_board[i][j]:
                    continue
                pp = '.'
                if self.sweeper.is_visible[i][j]:
                    pp = bd[i][j]
                # print(j, i, color_map[pp])
                self.lp.LedCtrlXYByCode(j, i + 1, color_map[pp])
                time.sleep(TIMEOUT)
        self.sweeper.print_visible()

    def set_color_bar(self):
        for i in range(1, 9):
            self.lp.LedCtrlXYByCode(8, i, color_map[i])
            time.sleep(TIMEOUT)

    def choose(self, x, y):
        return self.sweeper.choose(x, y)
    
    def game_over(self):
        time.sleep(0.500)
        self.lp.LedAllOn(72)
        self.lp.LedCtrlString("LOSER", 48, 12, 12, waitms=100)
        for i in range(1):
            self.lp.LedCtrlString("HA", 0, 63, 0, waitms=100)
            self.lp.LedCtrlString("HA", 0, 0, 63, waitms=100)
            self.lp.LedCtrlString("HA", 63, 0, 0, waitms=100)
        self.lp.LedAllOn(0)

    def winner(self):
        time.sleep(0.500)
        self.lp.LedAllOn(4)
        self.lp.LedCtrlString("ZHANAT 1LOVE", 63, 63, 63, waitms=50)
        self.lp.LedAllOn(0)

    def read_button(self):
        while True:
            but = self.lp.ButtonStateXY()
            if len(but) <= 0 or but[2] <= 0:
                continue
            print("|", but, "|")
            but.pop()
            print("|", but, "|")
            return but


if __name__ == "__main__":
    game = Game()
    while True:
        game.start()
