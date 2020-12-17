from utils import get_lines


class CubeGrid:
    def __init__(self, lines):
        # set of active cell coords
        self.grid = set()
        for y, line in enumerate(lines):
            for x, cell in enumerate(line):
                if cell == '#':
                    self.grid.add((x, y, 0))

    def neighbour_iter(self, x, y, z):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    if (i, j, k) != (0, 0, 0):
                        yield (x + i, y + j, z + k)

    def extents(self):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        min_z = 0
        max_z = 0

        for i, j, k in self.grid:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j
            if k < min_z:
                min_z = k
            if k > max_z:
                max_z = k
        return ((min_x - 1, max_x + 2),
                (min_y - 1, max_y + 2),
                (min_z - 1, max_z + 2))

    def neighbours(self, x, y, z):
        count = 0
        for cell in self.neighbour_iter(x, y, z):
            if cell in self.grid:
                count += 1
        return count

    def __len__(self):
        return len(self.grid)

    def iterate(self):
        new_grid = set()
        extents = self.extents()
        for x in range(*extents[0]):
            for y in range(*extents[1]):
                for z in range(*extents[2]):
                    n_count = self.neighbours(x, y, z)
                    if (x, y, z) in self.grid:
                        if n_count in (2, 3):
                            new_grid.add((x, y, z))
                    else:
                        if n_count == 3:
                            new_grid.add((x, y, z))

        self.grid = new_grid

    def render(self):
        extents = self.extents()
        for z in range(*extents[2]):
            print(f'z={z}')
            for y in range(*extents[1]):
                line = []
                for x in range(*extents[0]):
                    line.append('#' if (x, y, z) in self.grid else '.')
                print(''.join(line))
            print()


class CubeGrid4d:
    def __init__(self, lines):
        # set of active cell coords
        self.grid = set()
        for y, line in enumerate(lines):
            for x, cell in enumerate(line):
                if cell == '#':
                    self.grid.add((x, y, 0, 0))

    def neighbour_iter(self, x, y, z, w):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                for k in (-1, 0, 1):
                    for ll in (-1, 0, 1):
                        if (i, j, k, ll) != (0, 0, 0, 0):
                            yield (x + i, y + j, z + k, w + ll)

    def extents(self):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        min_z = 0
        max_z = 0
        min_w = 0
        max_w = 0

        for i, j, k, ll in self.grid:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j
            if k < min_z:
                min_z = k
            if k > max_z:
                max_z = k
            if ll < min_w:
                min_w = ll
            if ll > max_w:
                max_w = ll
        return ((min_x - 1, max_x + 2),
                (min_y - 1, max_y + 2),
                (min_z - 1, max_z + 2),
                (min_w - 1, max_w + 2))

    def neighbours(self, x, y, z, w):
        count = 0
        for cell in self.neighbour_iter(x, y, z, w):
            if cell in self.grid:
                count += 1
        return count

    def __len__(self):
        return len(self.grid)

    def iterate(self):
        new_grid = set()
        extents = self.extents()
        for x in range(*extents[0]):
            for y in range(*extents[1]):
                for z in range(*extents[2]):
                    for w in range(*extents[3]):
                        n_count = self.neighbours(x, y, z, w)
                        if (x, y, z, w) in self.grid:
                            if n_count in (2, 3):
                                new_grid.add((x, y, z, w))
                        else:
                            if n_count == 3:
                                new_grid.add((x, y, z, w))

        self.grid = new_grid

    def render(self):
        extents = self.extents()
        for w in range(*extents[3]):
            for z in range(*extents[2]):
                print(f'z={z}, w={w}')
                for y in range(*extents[1]):
                    line = []
                    for x in range(*extents[0]):
                        line.append('#' if (x, y, z, w) in self.grid else '.')
                    print(''.join(line))
                print()


def puzzle1():
    lines = get_lines('day17')
    # lines = ['.#.', '..#', '###']
    grid = CubeGrid(lines)
    for _ in range(6):
        # grid.render()
        grid.iterate()

    print(len(grid))


def puzzle2():
    lines = get_lines('day17')
    # lines = ['.#.', '..#', '###']
    grid = CubeGrid4d(lines)
    for _ in range(6):
        # grid.render()
        grid.iterate()

    print(len(grid))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
