from utils import get_int_inputs


def find_sum(inputs, target):
    for i in inputs:
        if i < target // 2 + 1:
            if target - i in inputs:
                return (i, target - i)


def main():
    ints = get_int_inputs('day1')
    for i in ints:
        if i <= 1010:
            result = find_sum(ints, 2020 - i)
            if result:
                print(i * result[0] * result[1])
                break


if __name__ == '__main__':
    main()
