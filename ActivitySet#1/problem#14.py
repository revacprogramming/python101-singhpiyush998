#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
# looking for a regular expression of '[0-9]+' 
# and then converting the extracted strings to integers and summing up the integers.
import re

fh = open("dataset/reg_ex.txt")
sum = 0

for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for number in numbers:
            sum += int(number)

print(sum)