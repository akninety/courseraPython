largest = None
smallest = None

while True:
    num = input()
    if num == 'done':
        break
 
    try :
        num = int(num)
    except :
        print('Invalid input')
        continue
    
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = int(num)
    
    if largest is None :
        largest = num
    elif num > largest :
        largest = int(num)
    
print('Maximum is', largest)
print('Minimum is', smallest)