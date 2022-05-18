""" Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

def my_input():
    fname = input("Enter file name: ")
    fh = open(fname)
    return fh

def find_avg(fh):
    total = 0
    count = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        total += float(line[line.find('0'):])
        count += 1
    return total / count

def output(avg):
    print("Average spam confidence:", avg)

def main():
    fh = my_input()
    avg = find_avg(fh)
    output(avg)

if __name__ == "__main__":
    main()