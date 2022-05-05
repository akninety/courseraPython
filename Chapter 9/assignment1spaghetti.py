fname = input("Enter file name: ")
fh = open(fname)

lst = list()
poem = list()
final = list()
sorted = list()

for line in fh :
    lst.append(line.rstrip())

for words in lst :
    poem.append(words.split())

for items in poem[0] :
    final.append(items)

for items in poem[1] :
    final.append(items)

for items in poem[2] :
    final.append(items)

for items in poem[3] :
    final.append(items)

for i in final :
    if i not in sorted:
        sorted.append(i)

sorted.sort()
print(sorted)