from itertools import product, count
from utils import get_lines


class SeatingLayout:
    def __init__(self, lines):
        self.rows = list(map(list, lines))
        self.width = len(self.rows[0])  # assume rectangular

    def immediate_neighbours(self, row, col):
        neighbours = 0
        x_pos = set((0,))
        y_pos = set((0,))
        if col >= 1:
            x_pos.add(-1)
        if col < self.width - 1:
            x_pos.add(1)
        if row >= 1:
            y_pos.add(-1)
        if row < len(self.rows) - 1:
            y_pos.add(1)

        for x, y in product(x_pos, y_pos):
            if (x, y) != (0, 0) and self.rows[row + y][col + x] == '#':
                neighbours += 1

        return neighbours

    def visible_neighbours(self, row, col):
        neighbours = 0
        dir_list = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)]
        for y, x in dir_list:
            for mult in count(1):
                try:
                    # Python is unhelpful here; I forgot about negative
                    # indices being 'valid' when I was expecting an
                    # IndexError to flag out-of-range. Hack to reinstate
                    # this behaviour...
                    if row + mult * y < 0:
                        raise IndexError
                    if col + mult * x < 0:
                        raise IndexError

                    seat_type = self.rows[row + mult * y][col + mult * x]
                    if seat_type == '#':
                        neighbours += 1
                        break
                    elif seat_type == 'L':
                        # can't see past empty seats
                        break
                except IndexError:
                    # We've gone as far as we can in this direction
                    break

        return neighbours

    def iterate(self, neigh_algo=None, tolerance=4):
        if neigh_algo is None:
            neigh_algo = self.immediate_neighbours
        changed = False

        # deep-copy rows for next iteration
        next_rows = []
        for row in self.rows:
            next_rows.append(row.copy())

        for row, seats in enumerate(self.rows):
            for col, seat in enumerate(seats):
                if seat == '.':
                    # minor optimisation, can ignore floor
                    continue
                n_count = neigh_algo(row, col)
                if seat == 'L' and n_count == 0:
                    # empty seat with no occupied neighbours
                    next_rows[row][col] = '#'
                    changed = True
                elif seat == '#' and n_count >= tolerance:
                    # occupied seat will be vacated
                    next_rows[row][col] = 'L'
                    changed = True

        self.rows = next_rows
        return changed

    @property
    def occupied(self):
        occ_count = 0
        for row in self.rows:
            occ_count += row.count('#')
        return occ_count


def puzzle1():
    lines = get_lines('day11')
    sl = SeatingLayout(lines)
    while sl.iterate():
        pass
    print(sl.occupied)


def puzzle2():
    lines = get_lines('day11')
    sl = SeatingLayout(lines)
    while sl.iterate(neigh_algo=sl.visible_neighbours, tolerance=5):
        pass
    print(sl.occupied)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
