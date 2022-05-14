def my_input():
    h = float(input("Enter no of hrs worked::"))
    r = float(input("Enter rate per hour:"))
    return h, r

def calc_pay(h, r):
    if h <= 40.0:
        return h * r
    else:
        return (40 * r + (h - 40) * r * 1.5)

def output(p):
    print("Pay:", p)

def main():
    hrs, rate = my_input()
    pay = calc_pay(hrs, rate)
    output(pay)

if __name__ == "__main__":
    main()