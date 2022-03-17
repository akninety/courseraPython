def computepay(h, r):
    overtime = 0
    grosspay = 0

    if h < 40 :
        return h * r
    elif h > 40:
        overtime = h - 40
        grosspay = (40 * r) + (overtime * 1.5 * r)
        return grosspay
    elif h < 0 :
        return "Enter a valid hour and rate"

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate"))
p = computepay(hrs, rate)
print("Pay", p)