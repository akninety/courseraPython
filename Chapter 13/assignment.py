import re

hand = open('regex.txt')

numlist = list()
sum = 0

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for items in stuff:
        sum = sum + float(items)

print(sum)
