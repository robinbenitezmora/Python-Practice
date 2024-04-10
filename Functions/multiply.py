
def multiply(num1, num2):
    return num1 * num2

def get_input(prompt):
    entry = float(input(prompt))
    return entry

first_num = get_input("Enter the first number:\n")
second_num = get_input("Enter the second number:\n")

result = multiply(first_num, second_num)
print(f'{first_num} * {second_num} = {result}')
