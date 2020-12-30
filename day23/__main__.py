from utils import get_lines


class CupCircle:
    def __init__(self, seq):
        self.seq = seq
        self.current = 0

    def iterate(self):
        label = self.seq[self.current]
        three = self.take_three()

        target = label - 1
        while True:
            try:
                dest = self.seq.index(target)
                break
            except ValueError:
                target -= 1
                if target < min(self.seq):
                    target = max(self.seq)

        self.seq = self.seq[:dest + 1] + three + self.seq[dest + 1:]

        # current may have moved; re-establish its location
        self.current = self.seq.index(label)
        # advance it clockwise
        self.current = (self.current + 1) % len(self.seq)

    def __getitem__(self, idx):
        return self.seq[idx % len(self.seq)]

    def take_three(self):
        taken = []
        remain = []

        for idx in range(3):
            taken.append(self[self.current + 1 + idx])

        for val in self.seq:
            if val not in taken:
                remain.append(val)

        assert len(taken) == 3
        assert len(remain) == len(self.seq) - 3

        self.seq = remain
        return taken

    def __str__(self):
        return ''.join(str(i) for i in self.seq)

    def final_str(self):
        final = []
        one = self.seq.index(1)
        for idx in range(len(self.seq) - 1):
            final.append(self[one + 1 + idx])
        return ''.join(str(i) for i in final)


class Cup:
    __slots__ = ('value', 'next')

    def __init__(self, value):
        self.value = value
        self.next = None


class OptimisedCupCircle:
    def __init__(self, seq):
        self.cup_count = len(seq)

        head = None
        first_value = None
        self.label_cup = {}
        for val in seq:
            c = Cup(val)
            if head:
                head.next = c
            else:
                first_value = val
            head = c
            self.label_cup[val] = c
        self.current = self.label_cup[first_value]
        # wrap around from last cup to first
        c.next = self.current

    def iterate(self):
        # This whole function needs to be sub-linear...
        three = self.take_three()

        # Determine destination cup label
        dest_label = self.current.value
        while True:
            dest_label -= 1
            if dest_label <= 0:
                dest_label = self.cup_count
            if dest_label not in (cup.value for cup in three):
                break
        # Find next position clockwise from dest_label
        dest_cup = self.label_cup[dest_label]

        # insert at the found location
        self.insert_three(dest_cup, three)

        # Pick next cup
        self.current = self.current.next

    def insert_three(self, dest_cup, three):
        three[2].next, dest_cup.next = dest_cup.next, three[0]

    def take_three(self):
        taken = []

        # Extract three following current
        ptr = self.current.next
        for _ in range(3):
            taken.append(ptr)
            ptr = ptr.next

        # And bypass these three
        self.current.next = ptr

        assert len(taken) == 3
        return taken

    def find_star_multiple(self):
        one_ptr = self.label_cup[1]
        return one_ptr.next.value * one_ptr.next.next.value


def puzzle1():
    cups = get_lines('day23')[0]  # only one line today.

    # cups = '389125467'  # sample data
    cups = list(int(x) for x in cups)
    cc = CupCircle(cups)
    for move in range(100):
        cc.iterate()

    print(cc.final_str())


def puzzle2():
    cups = get_lines('day23')[0]  # only one line today.

    # cups = '389125467'  # sample data
    cups = list(int(x) for x in cups)

    max_cup = max(cups)
    for remain in range(1_000_000 - len(cups)):
        cups.append(remain + max_cup + 1)
    assert len(cups) == 1_000_000

    cc = OptimisedCupCircle(cups)
    for move in range(10_000_000):
        cc.iterate()

    print(cc.find_star_multiple())


if __name__ == '__main__':
    puzzle1()
    puzzle2()
