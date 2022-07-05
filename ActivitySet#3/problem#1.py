

class Rectangle:
    def __init__(self, veritces: list[tuple[float, float]]):
        self.v1, self.v2, self.v3 = veritces
        self.l, self.b = self.get_l_b()

    def get_l_b(self):
        x = ((self.v2[0] - self.v1[0]) ** 2 + (self.v2[1] - self.v1[1]) ** 2) ** 0.5
        y = ((self.v3[0] - self.v2[0]) ** 2 + (self.v3[1] - self.v2[1]) ** 2) ** 0.5
        z = ((self.v1[0] - self.v3[0]) ** 2 + (self.v1[1] - self.v3[1]) ** 2) ** 0.5

        if x >= y and x >= z:
            return y, z
        elif y >= z:
            return x, z
        else:
            return x, y

    def find_area(self):
        return self.l * self.b


class Rectangles(list):
    def __init__(self, count: int, rects: list):        
        super().__init__(Rectangle(r) for r in rects)


def inp_rects():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Enter a valid number of rectangles.")
            continue
 
    i = 0
    lst = []
    while True:
        try:
            nums = [float(_) for _ in input().strip().split()]
        except:
            print("Enter valid cartesian coordinates.")
            continue
        
        if (len(nums) != 6):
            print("There should only be 3 vertices with 6 total points.")
            continue
        lst.append([(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])
        i += 1
        if i == n:
            break
        
    return n, lst
    
    
def output(rects):
    for rect in rects:
        print(f"Area of rectangle with vertices {rect.v1},{rect.v2},{rect.v3} is {round(rect.find_area(), 1)}")


def main():
    r = Rectangles(*inp_rects())
    output(r)

if __name__ == "__main__":
    main()
