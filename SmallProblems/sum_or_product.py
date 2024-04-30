
num = int(input("Enter a greater than 0 number: "))
operation = input('Enter \'s\' to compute the sum, or \'p\' to compute the product: ')

def sum_or_product(num, operation):
    if operation == 's':
        sum = 0
        for number in range(num + 1):
            sum += number
        return sum
    elif operation == 'p':
        product = 1
        for number in range(1, num + 1):
            product *= number
        return product
    else:
        return 'Invalid operation'

print(sum_or_product(num, operation))
