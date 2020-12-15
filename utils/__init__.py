from importlib.resources import open_text


def get_int_inputs(package):
    with open_text(package, 'inputs.txt') as f:
        return list(map(int, f.readlines()))


def get_int_list(package, sep=','):
    values = []
    with open_text(package, 'inputs.txt') as f:
        for line in f:
            values.extend(int(x) for x in line.split(sep) if x)
        return values


def get_text_pairs(package, sep):
    with open_text(package, 'inputs.txt') as f:
        return [(x[0].strip(), x[1].strip()) for x in
                (line.split(sep) for line in f.readlines())]


def get_lines(package):
    with open_text(package, 'inputs.txt') as f:
        return [line.strip() for line in f.readlines()]


def get_blank_sep_fields(package):
    with open_text(package, 'inputs.txt') as f:
        result = {}
        for line in f:
            if not line.strip():
                yield result
                result = {}
                continue
            for pair in line.split():
                key, value = pair.split(':', 1)
                result[key] = value
        if result:
            yield result


def get_blank_sep_lines(package):
    with open_text(package, 'inputs.txt') as f:
        result = []
        for line in f:
            line = line.strip()
            if not line:
                yield result
                result = []
                continue
            result.append(line)
        if result:
            yield result
