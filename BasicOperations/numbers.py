
'''number = '4936'

for i in range(len(number), 0, -1):
    print('One place value of the number is: ' + number[i-1])
    print('Tens place value of the number is: ' + number[i-2])
    print('Hundreds place value of the number is: ' + number[i-3])
    print('Thousands place value of the number is: ' + number[i-4])
    break'''

number = 4936

print('One place value of the number is: ' + str(number % 10))
print('Tens place value of the number is: ' + str((number % 100) // 10))
print('Hundreds place value of the number is: ' + str((number % 1000) // 100))
print('Thousands place value of the number is: ' + str((number % 10000) // 1000))
