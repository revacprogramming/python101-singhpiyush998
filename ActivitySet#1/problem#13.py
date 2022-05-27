"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""


def my_input():
    name = input("Enter file:")
    if len(name) < 1:
        name = "../dataset/mbox-short.txt"
    fh = open(name)
    return fh

def find_hour_count(fh):
    hour_list = list()

    for line in fh:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.split()
            time = words[5]
            hour = time[0:2]
                        
            hour_list.append(hour)


    hour_list.sort()

    hour_count = list()

    i = 0
    while i < len(hour_list):
        j = i
        count = 0
        while j < len(hour_list) and hour_list[i] == hour_list[j]:
            j += 1
        count = j - i
        hour_count.append((hour_list[i], count))
        
        i += count

    return hour_count;

def output(hour_count):
    for i, j in hour_count:
        print(i, j)

def main():
    fh = my_input()
    hour_count = find_hour_count(fh)
    output(hour_count)

if __name__ == "__main__":
    main()