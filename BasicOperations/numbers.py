
number = '4936'

for i in range(len(number), 0, -1):
    print('One place value of the number is: ' + number[i-1])
    print('Tens place value of the number is: ' + number[i-2])
    print('Hundreds place value of the number is: ' + number[i-3])
    print('Thousands place value of the number is: ' + number[i-4])
    break