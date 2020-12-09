from collections import deque
from utils import get_int_inputs


class InvalidXmas(Exception):
    pass


class XmasSequence:
    def __init__(self, seq, preamble=25):
        self.preamble = 25
        self.seq = seq
        self.partial = deque(maxlen=preamble)
        self.invalid = None

    def is_sum(self, val):
        # is val a sum of two (different) values in self.partial?
        for i, a in enumerate(self.partial):
            for j, b in enumerate(self.partial):
                if j == i:
                    continue
                if a + b == val:
                    return True
        return False

    def iter_valid(self):
        for idx, val in enumerate(self.seq):
            if idx < self.preamble:
                self.partial.append(val)
                continue
            # check validity
            if self.is_sum(val):
                self.partial.append(val)
                yield(val)
            else:
                self.invalid = val
                break

    def find_consecutive(self, target):
        tail = 0
        head = 0
        accum = 0

        while True:
            if accum == target:
                return self.seq[tail:head + 1]
            elif accum > target:
                # bust, increment tail and start again
                tail += 1
                accum = self.seq[tail]
                head = tail
            else:
                head += 1
                accum += self.seq[head]
            print(tail, head, accum)


def puzzle1():
    xmas = get_int_inputs('day9')
    seq = XmasSequence(xmas)
    for s in seq.iter_valid():
        print(s)
    print(seq.invalid)


def puzzle2():
    xmas = get_int_inputs('day9')
    seq = XmasSequence(xmas)
    consec = seq.find_consecutive(41682220)
    print(consec, min(consec) + max(consec))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
