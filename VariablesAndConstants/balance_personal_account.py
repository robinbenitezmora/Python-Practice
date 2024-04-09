
amount = int(input('Write the amount to deposit: '))
interest = float(input('Please define the interest to pay: '))
months = int(input('How many months would you like to calculate your money?: '))

amount *= round((1 + (interest / 100))**(months), 5)
print(amount)

