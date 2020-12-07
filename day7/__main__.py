from utils import get_lines


class RuleParser:
    def __init__(self, rules):
        self.parse(rules)

    def parse(self, lines):
        self.rules = {}
        for line in lines:
            bag, contents = line.split(' bags contain ', 1)
            valid = set()
            if contents != 'no other bags.':
                for bag_type in contents.split(','):
                    bag_type = bag_type.strip()
                    count, col_1, col_2, _ = bag_type.split()
                    count = int(count)
                    valid.add((f'{col_1} {col_2}', count))
            self.rules[bag] = valid

    def can_directly_contain(self, bag_type, inner):
        for inner_col, count in self.rules[bag_type]:
            if inner_col == inner:
                return True
        return False

    def bag_types(self):
        return list(self.rules.keys())

    def can_contain(self, bag_type, inner):
        if self.can_directly_contain(bag_type, inner):
            return True
        for bag_type, count in self.rules[bag_type]:
            if self.can_contain(bag_type, inner):
                return True
        return False

    def get_nested_count(self, bag_type):
        count = 0
        for inner_bt, inner_count in self.rules[bag_type]:
            count += inner_count
            count += inner_count * self.get_nested_count(inner_bt)
        return count


def puzzle1():
    rules = get_lines('day7')
    rp = RuleParser(rules)

    count = 0
    for bt in rp.bag_types():
        if rp.can_contain(bt, 'shiny gold'):
            count += 1

    print(count)


def puzzle2():
    rules = get_lines('day7')
    rp = RuleParser(rules)

    print(rp.get_nested_count('shiny gold'))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
