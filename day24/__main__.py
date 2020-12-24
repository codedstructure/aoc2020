from collections import defaultdict

from utils import get_lines


def parse(moves):
    while moves:
        if moves[0] in ('w', 'e'):
            yield moves[0]
            moves = moves[1:]
            continue
        yield moves[:2]
        moves = moves[2:]


class HexGrid:

    def __init__(self):
        # True = black, False = white.
        # Connectivity within the grid is evaluated based on
        # row (pos_y) being odd or even; 'east' or 'west'
        # diagonals will have x pos offset by one or zero.
        self.grid = defaultdict(bool)
        self.pos_x = 0
        self.pos_y = 0

    def move(self, direction):
        offset_e = self.pos_y % 2
        offset_w = (self.pos_y + 1) % 2

        if direction == 'e':
            self.pos_x += 1
        elif direction == 'w':
            self.pos_x -= 1
        elif direction == 'ne':
            self.pos_y -= 1
            self.pos_x += offset_e
        elif direction == 'nw':
            self.pos_y -= 1
            self.pos_x -= offset_w
        elif direction == 'se':
            self.pos_y += 1
            self.pos_x += offset_e
        elif direction == 'sw':
            self.pos_y += 1
            self.pos_x -= offset_w

    def flip(self):
        self.grid[(self.pos_x, self.pos_y)] = not self.grid[(self.pos_x, self.pos_y)]

    def reset_pos(self):
        self.pos_x = 0
        self.pos_y = 0

    def count(self):
        return sum(self.grid.values())

    def neighbours(self, pos):
        x, y = pos
        offset_e = y % 2
        offset_w = (y + 1) % 2
        yield((x + 1, y))  # E
        yield((x - 1, y))  # W
        yield((x + offset_e, y - 1))  # NE
        yield((x - offset_w, y - 1))  # NW
        yield((x + offset_e, y + 1))  # SE
        yield((x - offset_w, y + 1))  # SW

    def cycle(self):
        to_white = set()
        to_black = set()
        reference = self.grid.copy()

        # we iterate through the known black tiles, but we
        # also need to consider white tiles adjacent to these,
        # including any we haven't yet evaluated.
        white_tiles = set()

        # Set any black tiles to white if zero or more than 2 black neighbours
        # Also build set of white tiles adjacent to a black tile
        for pos, is_black in reference.items():
            if not is_black:
                continue

            black_count = 0
            for neigh in self.neighbours(pos):
                if not self.grid[neigh]:
                    white_tiles.add(neigh)
                if self.grid[neigh]:
                    black_count += 1
            if black_count == 0 or black_count > 2:
                to_white.add(pos)

        # Set any white tiles to black if exactly 2 black neighbours
        for pos in white_tiles:
            black_count = sum(self.grid[neigh] for neigh in self.neighbours(pos))
            if black_count == 2:
                to_black.add(pos)

        # Update
        for pos in to_white:
            self.grid[pos] = False
        for pos in to_black:
            self.grid[pos] = True


def puzzle1():
    lines = get_lines('day24')
    hg = HexGrid()
    for line in lines:
        for instr in parse(line):
            hg.move(instr)
        hg.flip()
        hg.reset_pos()
    print(hg.count())


def puzzle2():
    lines = get_lines('day24')
    hg = HexGrid()
    for line in lines:
        for instr in parse(line):
            hg.move(instr)
        hg.flip()
        hg.reset_pos()

    for day in range(100):
        hg.cycle()
    print(hg.count())


if __name__ == '__main__':
    puzzle1()
    puzzle2()
