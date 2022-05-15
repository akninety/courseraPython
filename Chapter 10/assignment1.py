name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

counts = dict()
emails = list()

for line in handle:
    line.rstrip()
    if line.startswith("From "):
        emails.append(line.split()[1])

for email in emails:
    counts[email] = counts.get(email,0) + 1

bigkey = None
bigvalue = None

for key,value in counts.items():
    if bigkey is None or value > bigvalue:
        bigkey = key
        bigvalue = value

print(bigkey,bigvalue)