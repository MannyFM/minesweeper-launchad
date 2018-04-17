import random


class Minesweeper:
    def __init__(self, size, n_bomb):
        self.size = size
        self.n_bomb = n_bomb
        self.remaining = size * size - n_bomb
        self.status = 'N'
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.is_mine = [[False for _ in range(size)] for _ in range(size)]
        self.is_visible = [[False for _ in range(size)] for _ in range(size)]
        self.is_flag = [[False for _ in range(size)] for _ in range(size)]

    def welcome(self):
        print("------------------------------")
        print("    Welcome to Minesweeper    ")
        print("------------------------------")
        print()

    def build(self):
        bombs = random.sample(range(0, self.size * self.size), self.n_bomb)
        # print(bombs)
        # print(self.is_mine)
        for bomb in bombs:
            x = (bomb % self.size)
            y = (bomb // self.size)
            # print(x, y)
            self.is_mine[y][x] = True
            self.board[y][x] = 'M'
        # print(self.is_mine)

        for i in range(self.size):
            for j in range(self.size):
                if not self.is_mine[i][j]:
                    self.board[i][j] = self.count_mines(j, i)

    def start(self):
        self.status = 'S'
        self.welcome()
        self.build()
        # self.print_board()
        # self.print_visible()

    def count_mines(self, x, y):
        count = 0
        # print(x, y, end="=")
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < self.size and 0 <= y + dy < self.size:
                    # print(x + dx, y + dy, end=", ")
                    if self.is_mine[y + dy][x + dx]:
                        count += 1
        # print()
        return count

    def print_visible(self):
        print("    0 1 2 3 4 5 6 7")
        print("    ---------------")
        for i in range(self.size):
            print("{} | ".format(i), end="")
            for j in range(self.size):
                pp = '.'
                if self.is_visible[i][j]:
                    pp = self.board[i][j]
                print("{} ".format(pp), end="")
            print("|")
        print("    ---------------\n")

    def print_board(self):
        print("    0 1 2 3 4 5 6 7")
        print("    ---------------")
        for i in range(self.size):
            print("{} | ".format(i), end="")
            for j in range(self.size):
                print("{} ".format(self.board[i][j]), end="")
            print("|")
        print("    ---------------\n")

    def flag(self, x, y):
        if self.is_visible[y][x] or self.status == 'G':
            return False
        self.is_flag[y][x] = True
        self.is_visible[y][x] = True
        self.board[y][x] = '!'
        return True

    def choose(self, x, y):
        if self.is_visible[y][x] or self.status == 'G':
            return False
        if self.is_mine[y][x]:
            self.status = 'G'
            self.is_visible[y][x] = True
        else:
            self.reveal(x, y)
        if self.remaining == 0:
            self.status = 'W'
        return True

    def reveal(self, x, y):
        if self.is_visible[y][x] or self.is_mine[y][x]:
            return
        self.is_visible[y][x] = True
        self.remaining -= 1
        if self.board[y][x] != 0:
            return
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= x + dx < self.size and 0 <= y + dy < self.size:
                    self.reveal(x + dx, y + dy)


if __name__ == "__main__":
    sweeper = Minesweeper(8, 10)
    sweeper.start()
    status = sweeper.flag(3, 3)
    sweeper.print_visible()
    print(status)

    status = sweeper.flag(3, 3)
    sweeper.print_visible()
    print(status)
