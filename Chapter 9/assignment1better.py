fname = input("Enter file name: ")
fh = open(fname)

lst = list()
lst2 = list()

for line in fh :
    words = line.split()
    for word in words :
        lst2.append(word)
        if word not in lst :
            lst.append(word)
            lst.sort()

print(lst)
