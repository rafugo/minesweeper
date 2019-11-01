# Class for game

from random import randint

class Game:

    # initializes
    def __init__(self, m, n, num_bombs):
        self.bomb_grid = []
        self.user_grid = []
        self.num_grid = []
        self.m = m
        self.n = n

        # generate grids
        for i in range(m):
            self.bomb_grid.append([0]*n)
            self.user_grid.append(['*']*n)
            self.num_grid.append([0]*n)

        count = 0
        # populate bombs
        while count < num_bombs:
            x = randint(0, m-1)
            y = randint(0, n-1)

            if self.bomb_grid[x][y] == 0:
                self.bomb_grid[x][y] = 1
                count += 1

        # precompute the num_grid
        for i in range(m):
            for j in range(n):
                count = 0

                if self.bomb_grid[i][j] == 1:
                    self.num_grid[i][j] = 'b'
                else:

                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if k == 0 and l == 0:
                                continue

                            u = i + k
                            v = j + l

                            if u < m and u >= 0 and \
                                v < n and v >= 0:

                                if self.bomb_grid[u][v] == 1:
                                    count += 1

                    self.num_grid[i][j] = count

    # returns -1 if bomb hit, 0 otherwise
    def make_move(self, x, y):

        # did we hit a bomb
        if self.bomb_grid[x][y] == 1:
            return -1

        else:
            # update user_grid
            self.update_user_grid(x, y)

            return 0

    # updates user_grid when user selects x,y
    def update_user_grid(self, x, y):

        # if the cell is empty
        if self.num_grid[x][y] == 0:
            self.user_grid[x][y] = '.'

            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k != 0 or l != 0:
                        i = x + k
                        j = y + l

                        if i < self.m and i >= 0 and \
                            j < self.n and j >= 0:

                            if self.user_grid[i][j] == '*':
                                self.update_user_grid(i, j)

        elif self.num_grid[x][y] != 'b':
            self.user_grid[x][y] = str(self.num_grid[x][y])

    def mark_bomb(self, x, y):
        if self.user_grid[x][y] == 'X':
            self.user_grid[x][y] = '*'
        elif self.user_grid[x][y] == '*':
            self.user_grid[x][y] = 'X'

    def check_win(self):
        for i in range((self.m)):
            for j in range((self.n)):
                if self.bomb_grid[i][j] == 1:
                    if self.user_grid[i][j] != 'X':
                        return False

        return True

    # prints out the board
    def print_board(self):
        to_print = ''
        for i in range(self.m):
            for j in range(self.n):
                to_print += self.user_grid[i][j]

            to_print += '\n'

        print(to_print)

    def print_bombs(self):
        to_print = ''
        for i in range(self.m):
            for j in range(self.n):
                to_print += str(self.bomb_grid[i][j])

            to_print += '\n'

        print(to_print)
