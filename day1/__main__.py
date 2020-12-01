from utils import get_int_inputs


def find_sum(inputs, target):
    """
    given a list of input integers, find the (first) two numbers
    which sum to the given target, and return them as a 2-tuple.

    Return None if the sum could not be made.
    """
    for i in inputs:
        if i < target // 2 + 1:
            if target - i in inputs:
                return (i, target - i)


def puzzle1():
    ints = get_int_inputs('day1')
    a, b = find_sum(ints, 2020)
    print(a * b)


def puzzle2():
    ints = get_int_inputs('day1')
    for i in ints:
        if i <= 1010:
            # At least one of the entries must be under half.
            # Assume we've got that, look for the other two.
            result = find_sum(ints, 2020 - i)
            if result:
                print(i * result[0] * result[1])
                break


if __name__ == '__main__':
    puzzle1()
    puzzle2()
