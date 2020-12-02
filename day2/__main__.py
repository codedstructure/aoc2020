from utils import get_text_pairs


def is_valid1(criteria, password):
    counts, value = criteria.split(None, 1)
    min_c, max_c = map(int, counts.split('-', 1))
    return min_c <= password.count(value) <= max_c


def puzzle1():
    pairs = get_text_pairs('day2', ':')
    print(len(list(filter(lambda p: is_valid1(*p), pairs))))


def is_valid2(criteria, password):
    pos, value = criteria.split(None, 1)
    pos_1, pos_2 = map(int, pos.split('-', 1))
    match_1 = password[pos_1 - 1] == value
    match_2 = password[pos_2 - 1] == value
    return (match_1 or match_2) and not (match_1 and match_2)


def puzzle2():
    pairs = get_text_pairs('day2', ':')
    print(len(list(filter(lambda p: is_valid2(*p), pairs))))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
