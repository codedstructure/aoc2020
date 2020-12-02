from importlib.resources import open_text


def get_int_inputs(package):
    with open_text(package, 'inputs.txt') as f:
        return list(map(int, f.readlines()))


def get_text_pairs(package, splitter):
    with open_text(package, 'inputs.txt') as f:
        return [(x[0].strip(), x[1].strip()) for x in
                (line.split(splitter) for line in f.readlines())]
