import unittest
from time import sleep

N = '^'
S = 'v'
E = '>'
W = '<'


def get_data():
    ''''''
    filename = "2024/Day 6: Guard Gallivant/input.txt"
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f]
        return grid


class Board:
    ''''''

    def __init__(self, grid):
        self.grid = grid
        self.obstacles = set()
        self.set_obstacles()

    def get_guard_details(self):
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                if val in {N, S, E, W}:
                    return x, y, val, self

    def set_obstacles(self):
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                if val == '#':
                    self.obstacles.add((x, y))

    def update_guard_position(self, old_x, old_y, new_x, new_y, direction):
        try:
            self.grid[old_y][old_x] = '\033[31m+\033[0m'
            self.grid[new_y][new_x] = direction
        except IndexError:
            return False
        return True

    def __str__(self):
        cols = [str(i)+'|' for i in range(len(self.grid[0]))]
        pretty = ''
        for i, row in enumerate(self.grid):
            pretty = pretty + '\n' + f"{i}: {'|'.join(row)}"

        return f":  {''.join(cols)}{pretty}"


class Guard:
    def __init__(self, x, y, direction, board):
        self.x = x
        self.y = y
        self.direction = direction
        self.board = board
        self.visited = {(self.x, self.y)}
        self.off_board = False

    def move(self):
        next_x, next_y = self.x, self.y

        if self.direction == N:
            next_y -= 1
        elif self.direction == S:
            next_y += 1
        elif self.direction == E:
            next_x += 1
        elif self.direction == W:
            next_x -= 1

        # Check boundary conditions
        if not (0 <= next_x < len(self.board.grid[0]) and 0 <= next_y < len(self.board.grid)):
            self.off_board = True
            print(f"Guard moved off the board at {self.x}, {self.y}")
            return

        if (next_x, next_y) not in self.board.obstacles:
            old_x, old_y = self.x, self.y
            self.x, self.y = next_x, next_y

            # Mark visited positions
            self.board.grid[old_y][old_x] = 'x'  # Mark old position
            if not self.board.update_guard_position(old_x, old_y, self.x, self.y, self.direction):
                self.off_board = True
                return
            self.visited.add((self.x, self.y))
        else:
            print(f"Cannot move to {next_x}, {next_y} - Obstacle present")
            self.turn_right()


    def turn_right(self):
        if self.direction == N:
            self.direction = E
        elif self.direction == S:
            self.direction = W
        elif self.direction == E:
            self.direction = S
        elif self.direction == W:
            self.direction = N




def main():
    ''''''
    data = Board(get_data())
    g = Guard(*data.get_guard_details())
    while not g.off_board:
        g.move()
        # print(data)
        # print(f"Guard position: {g.x}, {g.y}")
        if (g.x, g.y) in data.obstacles:
            # print(f"Guard hit an obstacle at {g.x}, {g.y}")
            break
        # sleep(1/60)
        # print('\x1b[2J\x1b[0;0H')
    print(len(g.visited))


class TestGuardGallivant(unittest.TestCase):
    def test_get_guard_position(self):
        data = Board([
            ['^'],
            ['.']
        ])
        x, y, direction = data.get_guard_details()
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(direction, '^')

        data = Board([
            ['.', 'v'],
            ['^', '.']
        ])
        x, y, direction = data.get_guard_details()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)
        self.assertEqual(direction, 'v')

        data = Board([
            ['.', '.'],
            ['>', '^']
        ])
        x, y, direction = data.get_guard_details()
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)
        self.assertEqual(direction, '>')

        data = Board([
            ['.', '<', '.'],
            ['^', '.', '>']
        ])
        x, y, direction = data.get_guard_details()
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)
        self.assertEqual(direction, '<')

        data = Board([
            ['.', '<', '.'],
            ['^', '>', '>']
        ])
        x, y, direction = data.get_guard_details()
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)
        self.assertEqual(direction, '>')


if __name__ == "__main__":
    main()
    # unittest.main()
