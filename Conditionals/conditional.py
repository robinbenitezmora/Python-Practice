
value = int(input("Enter a number: "))

if value == 3:
    print('Value is 3')
    print('Value is and odd number')
    print('Value is a prime number')
elif value == 4:
    print('Value is 4')
    print('Value is an even number')
    print('Value is not a prime number')
elif value == 9:
    pass # We can use pass to do nothing
elif value == 10:
    print('Value is 10')
    print('Value is an even number')
    print('Value is not a prime number')
else:
    print('Value is not 3, 4, 9 or 10')