hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

overtime = 0
grosspay = 0

if h < 40 :
    grosspay = h * r
    print('Gross Pay:', grosspay)
elif h >= 40 :
    overtime = h - 40
    grosspay = (40 * r) + (overtime * 1.5 * r)
    print('Gross Pay: ', grosspay)
else :
    print('Check your input!')

