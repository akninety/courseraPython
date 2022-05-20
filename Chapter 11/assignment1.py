name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
emails = list()

for line in handle:
    line.rstrip()
    if line.startswith("From "):
        emails.append(line[-14:-12])

for email in emails:
    counts[email] = counts.get(email,0) + 1

lst = list()

for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst, reverse=False)

for key, val in lst:
    print(key, val)