from utils import get_blank_sep_lines


class RuleEvaluator:
    def __init__(self, rules):
        self.rules = rules
        self.test_resolve()

    def flatten(self, *a):
        if len(a) == 1:
            return a
        else:
            result = []
            for item in a:
                if isinstance(item, (list, tuple)):
                    result.extend(self.flatten(*item))
                else:
                    result.append(item)
            return tuple(result)

    def resolve(self, *a):
        flat = self.flatten(*a)
        flat = list(filter(None, flat))
        if True in flat:
            return True
        if not flat:
            return False
        if len(flat) == 1:
            return flat[0]
        return flat

    def test_resolve(self):
        assert self.resolve(True, False) is True
        assert self.resolve(False, "stuff") == "stuff"
        assert self.resolve(True, "stuff") is True
        assert self.resolve(True, (False, False)) is True
        assert self.resolve(True, ("a", False)) is True
        assert self.resolve(False, ("a", True)) is True
        assert self.resolve(False, ("a", False)) == "a"
        assert self.resolve(False, (False, "a")) == "a"
        assert self.resolve(False, (False, (False, True))) is True
        assert self.resolve(False, ("abc", (False, "def"))) == ['abc', 'def']
        assert self.resolve(False, ("abc", False, ("def", "ijk"))) == ['abc', 'def', 'ijk']

    def match_seq(self, rule_seq, msg, depth=0):
        # True: message was fully matched - success!
        # False: message was mismatched; abandon
        # str: message matched so far, continue
        rules = list(map(int, rule_seq.split()))
        if not isinstance(msg, list):
            msg = [msg]

        possible = []
        # check validity; may get multiple partial answers, in which
        # case we need to try them all.
        for fork in msg:
            for idx, rule in enumerate(rules):
                fork = self.valid(rule, fork, depth=depth + 1)
                if fork is True and idx == len(rules) - 1:
                    # No need to continue with other forks
                    return True
                elif fork in (False, True):
                    # we mis-matched, or we finished string with more rules.
                    fork = False
                    break
            possible.append(fork)
        return self.resolve(*possible)

    def match_alternate(self, rule, msg, depth=0):
        seq_list = rule.split('|')
        left, right = seq_list
        left_eval = self.match_seq(left.strip(), msg, depth + 1)
        right_eval = self.match_seq(right.strip(), msg, depth + 1)
        return self.resolve(left_eval, right_eval)

    def match_literal(self, rule, msg, depth=0):
        # True: message was fully matched
        # False: message was mismatched
        # str: messages was partially matched, continue
        literal_match = rule[1:-1]
        if msg[0] != literal_match:
            return False
        else:
            if not msg[1:]:
                # Got to the end of the message ok - Success!
                return True
            # ok so far, continue with rest of message
            return msg[1:]

    def valid(self, rule_num, msg, depth=0):
        rule = self.rules[rule_num]
        # print(f"{' ' * depth}Checking {msg} against {rule_num}: {rule}")
        if rule.startswith('"'):
            return self.match_literal(rule, msg, depth + 1)
        elif '|' in rule:
            return self.match_alternate(rule, msg, depth + 1)
        else:
            return self.match_seq(rule, msg, depth + 1)


def puzzle1():
    rules, messages = get_blank_sep_lines('day19')
    rules = {int(x): y.strip() for x, y in
             [rule.split(':') for rule in rules]}
    rule_ev = RuleEvaluator(rules)

    count = 0
    for msg in messages:
        if rule_ev.valid(0, msg) is True:
            count += 1
    print(count)


def puzzle2():
    rules, messages = get_blank_sep_lines('day19')
    rules = {int(x): y.strip() for x, y in
             [rule.split(':') for rule in rules]}
    rules[8] = "42 | 42 8"
    rules[11] = "42 31 | 42 11 31"
    rule_ev = RuleEvaluator(rules)

    count = 0
    for msg in messages:
        if rule_ev.valid(0, msg) is True:
            count += 1
    print(count)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
