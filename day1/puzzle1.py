from utils import get_int_inputs


def main():
    ints = get_int_inputs('day1')
    for i in ints:
        if i <= 1010 and 2020 - i in ints:
            print(i * (2020 - i))
            break


if __name__ == '__main__':
    main()
