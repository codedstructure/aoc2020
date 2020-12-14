from collections import defaultdict
from utils import get_text_pairs


def puzzle1():
    lines = get_text_pairs('day14', '=')

    memory = defaultdict(int)
    for op, value in lines:
        if op == 'mask':
            or_mask = int(value.replace('X', '0'), 2)
            and_mask = int(value.replace('X', '1'), 2)
        else:
            addr = int(op[4:-1])
            memory[addr] = (int(value) & and_mask) | or_mask
            continue

    print(sum(memory.values()))


def puzzle2():
    lines = get_text_pairs('day14', '=')

    memory = defaultdict(int)
    mask = ''
    for op, value in lines:
        if op == 'mask':
            mask = value
            or_mask = int(value.replace('X', '0'), 2)
        else:
            addr = op[4:-1]
            for i in range(2 ** mask.count('X')):
                float_addr = list('{:036b}'.format(int(addr) | or_mask))
                pos = -1
                for p in range(mask.count('X')):
                    pos = mask.find('X', pos + 1)
                    float_addr[pos] = '1' if ((i >> p) & 1) else '0'
                float_addr = ''.join(float_addr)
                memory[int(float_addr, 2)] = int(value)

    print(sum(memory.values()))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
