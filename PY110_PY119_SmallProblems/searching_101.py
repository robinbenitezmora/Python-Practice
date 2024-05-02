

num1 = int(input('Enter the first number:\n'))
num2 = int(input('Enter the second number:\n'))
num3 = int(input('Enter the third number:\n'))
num4 = int(input('Enter the fourth number:\n'))
num5 = int(input('Enter the fifth number:\n'))
num6 = int(input('Enter the sixth number:\n'))

num_list = [num1, num2, num3, num4, num5, num6]

def search_list(num_list, num):
    if num in num_list[0:5]:
        return f'The number {num} appears in {num_list}'
    else:
        return f'The number {num} does not appear in {num_list}'

print(search_list(num_list, num6))


