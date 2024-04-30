
bill = int(input("Enter the bill amount: "))
tip = int(input("Enter the tip percentage: "))

def tip_calculator(bill, tip):
    amount = round((1 + tip / 100) * bill, 2)
    return amount

amount = tip_calculator(bill, tip)
print(f"The total amount is {amount}.")
