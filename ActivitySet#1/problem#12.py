name = input("Enter file:")
if len(name) < 1:
    name = "../dataset/mbox-short.txt"
handle = open(name)

email_count = dict()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        if words[1] in email_count.keys():
            email_count[words[1]] = email_count[words[1]] + 1
        else:
            email_count[words[1]] = 1

max_count = 0
max_count_email = ""
for k,v in email_count.items():
    if v > max_count:
        max_count = v
        max_count_email = k

print(max_count_email, max_count)