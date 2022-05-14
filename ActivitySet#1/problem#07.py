# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

def my_input():
    n = input("Enter a number: ")
    return n
    
def find_lowest_and_smallest(n, l, s):
        try:
            n  = int(n)
            if l is None or n > l:
                l = n
            elif s is None or n < s:
                s = n
        except:
            print("Invalid input")
        return l, s

def output(l, s):
    print("Maximum is", l)
    print("Maximum is", s)

def main():
    largest = None
    smallest = None
    while True:
        num = my_input()
        if num == "done":
            break
        largest, smallest = find_lowest_and_smallest(num, largest, smallest)
    
    output(largest, smallest)

if __name__ == "__main__":
    main()