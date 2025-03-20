import re

fname = input("Enter file name: ")

if len(fname) < 1 : fname = "regex_sum_42.txt"

print(open(fname).read())
numbers = re.findall('[0-9]+', open(fname).read())
print(sum([int(num) for num in numbers]))
#print(len(numbers))