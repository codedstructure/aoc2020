from utils import get_blank_sep_lines


def puzzle1():
    count = 0
    for declaration in get_blank_sep_lines('day6'):
        yeses = set()
        for person in declaration:
            yeses |= set(person)
        count += len(yeses)
    print(count)


def puzzle2():
    count = 0
    everything = set('abcdefghijklmnopqrstuvwxyz')
    for declaration in get_blank_sep_lines('day6'):
        yeses = everything.copy()
        for person in declaration:
            nos = (everything - set(person))
            yeses -= nos
        count += len(yeses)
    print(count)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
