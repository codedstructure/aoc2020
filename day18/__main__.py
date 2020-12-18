from utils import get_lines


OPEN_PAREN = '('
CLOSE_PAREN = ')'


def tokenize(expr):
    tokens = expr.split()
    for token in tokens:
        if token[0] == '(':
            yield OPEN_PAREN
            yield from tokenize(token[1:])
        elif token[-1] == ')':
            yield from tokenize(token[:-1])
            yield CLOSE_PAREN
        elif token in ('+', '*'):
            yield token
        else:
            yield int(token)


def linear_eval(tokens):
    if len(tokens) == 1:
        return tokens[0]
    if tokens[1] == '+':
        return linear_eval([tokens[0] + tokens[2]] + tokens[3:])
    elif tokens[1] == '*':
        return linear_eval([tokens[0] * tokens[2]] + tokens[3:])


def add_mul(tokens):
    if len(tokens) == 1:
        return tokens[0]
    if tokens[1] == '+':
        return add_mul([tokens[0] + tokens[2]] + tokens[3:])
    elif tokens[1] == '*':
        return tokens[0] * add_mul(tokens[2:])


def evaluate(tokens, flatten=linear_eval):
    stack = [[]]  # list of sub-expressions
    for token in tokens:
        if token == OPEN_PAREN:
            stack.append([])
        elif token == CLOSE_PAREN:
            sub_expr = stack.pop()
            stack[-1].append(evaluate(sub_expr, flatten=flatten))
        else:
            stack[-1].append(token)
    assert len(stack) == 1
    return flatten(stack[0])


def puzzle1():
    lines = get_lines('day18')
    total = 0
    for expr in lines:
        tokens = tokenize(expr)
        total += evaluate(tokens)
    print(total)


def puzzle2():
    lines = get_lines('day18')
    total = 0
    for expr in lines:
        tokens = tokenize(expr)
        total += evaluate(tokens, flatten=add_mul)
    print(total)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
