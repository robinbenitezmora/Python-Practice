
number = input("Enter a number: ")

def is_odd(number):
    if int(number) % 2 == 0:
        return False
    else:
        return True

print(is_odd(number))
