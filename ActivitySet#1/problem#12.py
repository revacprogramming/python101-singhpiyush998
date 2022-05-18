from gettext import find


def my_input():
    name = input("Enter file:")
    if len(name) < 1:
        name = "dataset/mbox-short.txt"
    fh = open(name)
    return fh

def find_max_count_email(fh):
    email_count = dict()

    for line in fh:
        if line.startswith("From") and not line.startswith("From:"):
            words = line.split()
            if words[1] in email_count.keys():
                email_count[words[1]] += 1
            else:
                email_count[words[1]] = 1

    max_count = 0
    max_count_email = ""
    for k,v in email_count.items():
        if v > max_count:
            max_count = v
            max_count_email = k

    return max_count, max_count_email

def output(max_count, max_count_email):
    print(max_count_email, max_count)

def main():
    fh = my_input()
    max_count, max_count_email = find_max_count_email(fh)
    output(max_count, max_count_email)

if __name__ == "__main__":
    main()
