fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

emails = list()
addressbook = list()

count = 0

fh = open(fname)
for items in fh :
    items.rstrip()
    if items.startswith('From ') :
        emails.append(items.split())

for addresses in emails :
    print(addresses[1])
    addressbook.append(addresses[1])

print("There were", len(addressbook), "lines in the file with From as well as the first word")