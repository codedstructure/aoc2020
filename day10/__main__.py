import functools
from utils import get_int_inputs


def puzzle1():
    adapters = get_int_inputs('day10')
    adapters.sort()
    ones = 0
    threes = 0
    prev = 0
    for joltage in adapters:
        delta = joltage - prev
        if delta < 1:
            print(f"--- {delta}")
        elif delta == 1:
            ones += 1
        elif delta == 3:
            threes += 1
        elif delta > 3:
            print(f"*** {delta}")
        prev = joltage
    threes += 1  # built-in adapter always 3 higher...
    print(ones * threes)


# This memoization is *essential* to good performance.
@functools.lru_cache()
def prefix_joltage_ways(jolts, adapters):
    adapter_count = len(adapters)
    if adapter_count <= 1:
        # Only one way of adding the last (or no) adapter
        return 1
    ways = 0
    could_skip_1 = adapters[1] - jolts <= 3
    could_skip_2 = adapter_count > 2 and adapters[2] - jolts <= 3

    ways += prefix_joltage_ways(adapters[0], adapters[1:])
    if could_skip_1:
        ways += prefix_joltage_ways(adapters[1], adapters[2:])
    if could_skip_2:
        ways += prefix_joltage_ways(adapters[2], adapters[3:])
    return ways


def puzzle2():
    adapters = get_int_inputs('day10')
    adapters.sort()
    # Note we use a tuple as required for memoization key.
    print(prefix_joltage_ways(0, tuple(adapters)))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
