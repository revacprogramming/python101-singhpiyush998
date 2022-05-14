"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""
def my_input():
    s = float(input("Enter Score: "))
    try:
        assert not (s < 0.0 or s > 1.0), "OUT OF RANGE"
    except AssertionError as e:
        print(e)
        quit()
    return s

def calc_grade(s):
    if s >= 0.9:
        return "A"
    elif s >= 0.8:
        return "B"
    elif s >= 0.7:
        return "C"
    elif s >= 0.6:
        return "D"
    else:
        return "F"

def output(res):
    print("Grade:", res)

def main():
    score = my_input()
    grade = calc_grade(score)
    output(grade)

if __name__ == "__main__":
    main()