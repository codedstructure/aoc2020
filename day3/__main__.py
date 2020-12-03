from utils import get_lines


class TreeGrid:
    def __init__(self, lines):
        self.lines = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def tree_at(self, row, col):
        return self.lines[row][col % self.width] == '#'

    def traverse(self, right, down):
        count = 0
        x_pos = 0
        row = 0
        while row < self.height:
            if self.tree_at(row, x_pos):
                count += 1
            row += down
            x_pos += right
        return count


def puzzle1():
    grid = TreeGrid(get_lines('day3'))

    count = 0
    x_pos = 0
    for row in range(grid.height):
        if grid.tree_at(row, x_pos):
            count += 1
        x_pos += 3
    print(count)


def puzzle2():
    grid = TreeGrid(get_lines('day3'))

    t_11 = grid.traverse(1, 1)
    t_31 = grid.traverse(3, 1)
    t_51 = grid.traverse(5, 1)
    t_71 = grid.traverse(7, 1)
    t_12 = grid.traverse(1, 2)
    print(t_11 * t_31 * t_51 * t_71 * t_12)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
