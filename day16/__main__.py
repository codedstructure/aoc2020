from collections import defaultdict
from utils import get_blank_sep_lines


def puzzle1():
    info_lines, my_ticket, nearby_tickets = get_blank_sep_lines('day16')
    my_ticket = my_ticket[1:]
    nearby_tickets = [list(map(int, line.split(',')))
                      for line in nearby_tickets[1:]]
    info = {}
    for line in info_lines:
        key, value = line.split(':', 1)
        ranges = value.split()
        r1 = ranges[0].split('-')
        r2 = ranges[-1].split('-')
        info[key] = [(int(r1[0]), int(r1[1])), (int(r2[0]), int(r2[1]))]

    error_sum = 0
    for ticket in nearby_tickets:
        for item in ticket:
            valid = False
            for check1, check2 in info.values():
                if ((check1[0] <= item <= check1[1]) or
                        (check2[0] <= item <= check2[1])):
                    valid = True
                    break
            if not valid:
                error_sum += item

    print(error_sum)


def puzzle2():
    info_lines, my_ticket, nearby_tickets = get_blank_sep_lines('day16')
    my_ticket = list(map(int, my_ticket[1].split(',')))
    nearby_tickets = [list(map(int, line.split(',')))
                      for line in nearby_tickets[1:]]
    info = {}
    for line in info_lines:
        key, value = line.split(':', 1)
        ranges = value.split()
        r1 = ranges[0].split('-')
        r2 = ranges[-1].split('-')
        info[key] = [(int(r1[0]), int(r1[1])), (int(r2[0]), int(r2[1]))]

    valid_tickets = []
    for ticket in nearby_tickets:
        valid = True
        for item in ticket:
            item_valid = False
            for check1, check2 in info.values():
                if ((check1[0] <= item <= check1[1]) or
                        (check2[0] <= item <= check2[1])):
                    item_valid = True
                    break
            if not item_valid:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    # transpose so we can easily look at a column at a time
    columns = list(zip(*valid_tickets))

    # Check each info type for which columns it could possibly be
    possibles = defaultdict(set)
    for key, (check1, check2) in info.items():
        for idx, values in enumerate(columns):
            if all((check1[0] <= v <= check1[1]) or
                   (check2[0] <= v <= check2[1]) for v in values):
                possibles[key].add(idx)

    # Make a (valid on this data) assumption that we don't have to
    # 'sudoku' the whole thing and can just consider the values
    # as monotonically less constrained.
    found = {}
    seen = set()
    for key, possible in sorted(possibles.items(), key=lambda x: len(x[1])):
        loc = (possible - seen).pop()
        found[key] = loc
        seen.add(loc)

    # Determine product of values starting with 'departure'
    product = 1
    for key, val in found.items():
        if key.startswith('departure'):
            product *= my_ticket[val]
    print(product)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
