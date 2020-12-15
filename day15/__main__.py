from utils import get_int_list


def rindex(list, value):
    for idx, item in enumerate(reversed(list)):
        if item == value:
            return len(list) - idx - 1


class RindexList:
    def __init__(self, seq):
        self.length = len(seq)
        self.seq = seq[:-1]
        self.pending_value = seq[-1]
        self.cache = {}
        self.seen = set(self.seq)

    def tail_rindex(self, value):
        if value in self.cache:
            return self.cache[value]
        result = 0
        for idx, item in enumerate(reversed(self.seq)):
            if item == value:
                result = len(self.seq) - idx - 1
                break
        self.cache[value] = result
        return result

    def head(self):
        return self.pending_value

    def __len__(self):
        return self.length

    def append(self, value):
        # update self.pending_value in the cache
        self.cache[self.pending_value] = len(self) - 1
        self.seq.append(self.pending_value)
        self.seen.add(self.pending_value)
        self.pending_value = value
        self.length += 1

    def __contains__(self, value):
        return value in self.seq or value == self.pending_value

    def in_tail(self, value):
        return value in self.seen

    def __repr__(self):
        return repr(self.seq + [self.pending_value])


def puzzle1():
    nums = get_int_list('day15')
    for turn in range(1, 2020 + 1):
        if turn <= len(nums):
            continue
        last_num, prev_nums = nums[-1], nums[:-1]
        if last_num not in prev_nums:
            nums.append(0)
        else:
            last_spoken = rindex(prev_nums, last_num) + 1
            delta = (turn - 1) - last_spoken
            nums.append(delta)

    print(nums[-1])


def puzzle2():
    nums = get_int_list('day15')
    limit = 30000000
    nums = RindexList(nums)
    for turn in range(1, limit + 1):
        if turn <= len(nums):
            continue
        last_num = nums.head()
        if not nums.in_tail(last_num):
            nums.append(0)
        else:
            last_spoken = nums.tail_rindex(last_num) + 1
            delta = (turn - 1) - last_spoken
            nums.append(delta)

    print(nums.head())


if __name__ == '__main__':
    puzzle1()
    puzzle2()
