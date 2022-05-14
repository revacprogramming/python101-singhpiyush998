# This first line is provided for you



# print("Pay: " + str(hrs * rate))


def my_input():
    h = float(input("Enter Hours:"))
    r = float(input("Enter rate:"))
    return h, r

def calc_pay(h, r):
    return h * r

def output(p):
    print("Pay:", p)

def main():
    hrs, rate = my_input()
    pay = calc_pay(hrs, rate)
    output(pay)

if __name__ == "__main__":
    main()