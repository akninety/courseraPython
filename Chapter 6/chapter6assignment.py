text = "X-DSPAM-Confidence:    0.8475"

#Find 0.8475 index position
#print(text.find('0.8475'))

searching = text[23:]
print(searching)
print(type(searching))
print(float(searching))
