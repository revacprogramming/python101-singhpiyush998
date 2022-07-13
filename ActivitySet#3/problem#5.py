

class Soduku:
    def __init__(self, soduku: list[list[int]]):
        self.soduku = soduku
        self._non_viable = None  # https://stackoverflow.com/a/63954409
        self.category = self._get_category()

    def _analyse(self, category, posn: int, ls: list[int], belongs_to: "str") -> str:
        # Find all the elements which are repeating
        repeaters = {r for r in ls if ls.count(r) > 1}
        if repeaters:
            if len(repeaters) == 1 and 0 in repeaters:
                # 0 is the only repeating number
                if category != "non-viable":
                    category = "incomplete but viable"
            else:
                category = "non-viable"
                self.non_viable = (belongs_to,  posn)
        return category

    def _get_category(self) -> str:
        """
        Returns:
            str: Will be either "complete" or "incomplete but viable" or "non-viable"
        """
        category = None

        # Checking all the rows
        for i in range(9):
            ls = self.soduku[i]
            category = self._analyse(category, i + 1, ls, "rows")

        # Checking all the columns
        for i in range(9):
            ls = [self.soduku[j][i] for j in range(0, 9)]
            category = self._analyse(category, i + 1, ls, "columns")

        # Checking all the sub-matrices
        j = 0
        k = -1
        for i in range(9):
            # generate a sub-matrix
            ls = []
            for _ in range(9):
                k += 1
                ls.append(self.soduku[j][k])

                if k in (2, 5, 8) and j not in (2, 5, 8):
                    j += 1
                    k -= 3

            category = self._analyse(category, i + 1, ls, "sub-matrices")

            if ((i + 1) % 3 == 0):
                j += 1
                k = -1
            else:
                j -= 2

        if category is None:
            category = "complete"
        return category

    @property
    def non_viable(self) -> dict[str, list[int]]:
        if self._non_viable is None:
            raise AttributeError("Attribute not yet initalised")
        return self._non_viable

    @non_viable.setter
    def non_viable(self, violate: tuple[str, int]):
        """
        Args:
            violate (tuple[str, str]):
                violate[0] must be either "rows" or "columns" or 'sub-matrices"
        """
        if self._non_viable is None:
            self._non_viable = {"rows": [], "columns": [], "sub-matrices": []}
        if 1 <= violate[1] <= 9:
            if violate[0] in self._non_viable.keys():
                self._non_viable[violate[0]].append(violate[1])
            else:
                raise KeyError(
                    "Key must be either \"rows\" or \"columns\" or \"sub-matrices\"")
        else:
            raise ValueError("The value must be between 1 to 9")


class Sodukus(list):
    def __init__(self, soduku: list[list[list[int]]]):
        super().__init__(Soduku(s) for s in soduku)


def inp_sodukus() -> list[list[list[int]]]:
    while True:
        try:
            n = int(input())
            if not n > 0:
                raise ValueError()
            break
        except ValueError:
            print("Please enter a integer greater than 0")
            continue

    res = []
    for _ in range(n):
        soduku = []
        while True:
            try:
                tmp = [int(i) for i in input().strip().split()]
            except ValueError:
                print("All the values should be integers")
                continue

            if len(tmp) == 0:
                continue  # For the empty line
            if len(tmp) != 9:
                print("There should be exactly nine integers in each row")
                continue

            soduku.append(tmp)

            if len(soduku) == 9:
                break

        res.append(soduku)
    return res


def output(sodukus: list[Soduku]):
    for s in sodukus:
        print(f"\n{s.category}")
        if s.category == "non-viable":
            for k, v in s.non_viable.items():
                print("  {}: {}".format(k, " ".join(str(i) for i in v)))


def main():
    sodukus = Sodukus(inp_sodukus())
    output(sodukus)


if __name__ == "__main__":
    main()
