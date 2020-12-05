from utils import get_lines


class BoardingPass:
    def __init__(self, location):
        self.location = location

    def parse(self):
        row = 0
        for idx in range(7):
            if self.location[idx] == 'B':  # upper half
                row += 2 ** (6 - idx)
        col = 0
        for idx in range(3):
            if self.location[7 + idx] == 'R':  # upper half
                col += 2 ** (2 - idx)
        return row, col

    def get_id(self):
        row, col = self.parse()
        return row * 8 + col


def puzzle1():
    max_id = 0
    for bp in get_lines('day5'):
        bp_id = BoardingPass(bp).get_id()
        if bp_id > max_id:
            max_id = bp_id
    print(max_id)


def puzzle2():
    bp_ids = []
    for bp in get_lines('day5'):
        bp_ids.append(BoardingPass(bp).get_id())
    bp_ids.sort()
    for val in bp_ids:
        if val + 1 not in bp_ids:
            print(val + 1)
            break


if __name__ == '__main__':
    puzzle1()
    puzzle2()
