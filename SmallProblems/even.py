num = int(input("Enter a number: "))

def is_even(num):
    for number in range(0, num, 2):
        print(number)

is_even(num)