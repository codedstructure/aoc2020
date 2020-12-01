from importlib.resources import open_text


def get_int_inputs(package):
    with open_text(package, 'inputs.txt') as f:
        return list(map(int, f.readlines()))
