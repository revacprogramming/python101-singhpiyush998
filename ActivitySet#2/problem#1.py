

def add(a, b):
    return  int(a) + int(b)


def main():
    a = input("Enter 1st Number? ")
    b = input("Enter 2nd Number? ")

    c = add(a, b)
    print(f"sum of {a} and {b} is {c}")

if __name__ == "__main__":
    main()