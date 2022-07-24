class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

    @staticmethod
    def get_gcd(a, b):
        if b == 0:
            return a
        return Fraction.get_gcd(b, a % b)

    def simplify(self):
        gcd = Fraction.get_gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd
        return self

    def __add__(self, frac):
        return Fraction(
            self.num * frac.den + frac.num * self.den,
            self.den * frac.den
        )


class EgyFrac:
    def __init__(self, fracs: list[Fraction]):
        self.fracs = fracs
        self.sum = self.get_sum()

    def get_sum(self):
        sum = self.fracs[0]
        for i in range(1, len(self.fracs)):
            sum += self.fracs[i]
        return sum.simplify()

    def __str__(self):
        return ' + '.join(f"{i.num}/{i.den}" for i in self.fracs) + f" = {self.sum.num}/{self.sum.den}"


class EgyFracs(list):
    def __init__(self, egy_fracs: list[list[Fraction]]):
        self.items = [EgyFrac(e) for e in egy_fracs]


def input_frac():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Please enter valid count of egpytian fractions")
            continue

    egy_fracs = []
    for _ in range(n):
        while True:
            try:
                m = int(input())
                assert m > 0
                break
            except:
                print("Please enter valid number of fractions")
                continue

        while True:
            try:
                fracs = [Fraction(1, int(i)) for i in input().strip().split()]
            except:
                print("Please enter valid integer denominators")
                continue
            if len(fracs) != m:
                print("Enter correct count of denominators as specified in the above line")
                continue
            break
        egy_fracs.append(fracs)

    return egy_fracs


def output(fracs):
    for f in fracs.items:
        print(f)


def main():
    fracs = EgyFracs(input_frac())
    output(fracs)


if __name__ == "__main__":
    main()
