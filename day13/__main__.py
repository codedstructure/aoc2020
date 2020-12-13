from math import gcd
from utils import get_lines


def puzzle1():
    lines = get_lines('day13')
    earliest = int(lines[0])
    bus_ids = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    min_bus = 0
    min_delay = 1e12
    for bus_id in bus_ids:
        delay = bus_id - (earliest % bus_id)
        if delay < min_delay:
            min_delay = delay
            min_bus = bus_id
    print(min_bus * min_delay)


def lcm(x, y):
    return (x * y) // gcd(x, y)


def puzzle2():
    lines = get_lines('day13')
    bus_ids = [int(bus) if bus != 'x' else None
               for bus in lines[1].split(',')]

    ts = 0
    delta = bus_ids[0]  # assume not None...
    for idx, val in enumerate(bus_ids[1:], 1):
        while True:
            if val is None:
                break
            if (ts + idx) % val == 0:
                delta = lcm(delta, val)
                break
            ts += delta
    print(ts)


def puzzle2_naive(bus_ids):
    # naive approach used for testing
    t = 0
    while True:
        for idx, constraint in enumerate(bus_ids):
            if constraint is not None:
                if (t + idx) % constraint != 0:
                    # fail; try next t
                    t += 1
                    break
        else:
            print(t)
            break


if __name__ == '__main__':
    puzzle1()
    puzzle2()
