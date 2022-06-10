def input_two_numbers():
    a, b = [int(x) for x in input("input? ").split()]
    return a,b


def add(a, b):
    return a + b


def output(a, b, sum):
    print(f"{a} + {b} is {sum}")


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
