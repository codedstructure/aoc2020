from itertools import count
from utils import get_lines


def find_loop_size(pk):
    val = 1
    for ls in count():
        if val == pk:
            return ls
        val = transform_step(7, val)


def transform_step(sn, value):
    return (value * sn) % 20201227


def transform(sn, loop_size):
    value = 1
    for ll in range(loop_size):
        value = transform_step(sn, value)
    return value


def puzzle1():
    lines = get_lines('day25')

    card_pk, door_pk = (int(x) for x in lines)
    card_loop_size = find_loop_size(card_pk)
    door_loop_size = find_loop_size(door_pk)

    assert card_pk == transform(7, card_loop_size)
    assert door_pk == transform(7, door_loop_size)

    enc_key = transform(door_pk, card_loop_size)
    print(enc_key)


def puzzle2():
    pass


if __name__ == '__main__':
    puzzle1()
    puzzle2()
