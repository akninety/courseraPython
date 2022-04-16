# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

#Set counter variable for loop
count = 0
nums = 0
total = 0
average = 0

for line in fh:
    #Strip newline whitespace
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #Define counter variable to obtain line count
    count = count + 1
    #Slice last 6 characters of a string
    nums = line[-6:]
    total = total + float(nums)
    average = total / count
   
print("Done")
print(count)
print(average)