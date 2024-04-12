
num = int(input("Enter a number: "))

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(f"The number {num} is {even_or_odd(num)}")
