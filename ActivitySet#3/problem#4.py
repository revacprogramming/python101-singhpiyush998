

def decode(s: list[int]):
    res = ''
    i = 0
    while i < len(s):
        if s[i] == 0:
            if s[i + 1] == 0:
                res += '0 '
                i += 2
            else:
                n = s[i + 1]
                c = s[i + 2]
                for _ in range(n):
                    res += f'{c} '
                i += 3

        else:
            res += f'{s[i]} '
            i += 1

    return res


def input_code():
    while True:
        try:
            n = int(input().strip())
            assert n > 0
            break
        except:
            print("Enter a valid positve integer")
            continue

    inp = []
    for _ in range(n):
        while True:
            try:
                m = int(input().strip())
                assert m > 0
                break
            except:
                print("Enter a valid positive length of the code")
                continue

        while True:
            try:
                code = [int(i) for i in input().strip().split()]
                if len(code) != m:
                    print("Please enter correct number of integers")
                    continue
                break
            except:
                print("Please enter only integers")
                continue

        inp.append(code)

    return inp


def main():
    for i in input_code():
        print('\n')
        print(*i)
        print(decode(i) + '\n')


if __name__ == "__main__":
    main()
