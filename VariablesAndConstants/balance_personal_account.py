
amount = int(input('Write the amount to deposit: '))
interest = float(input('Please define the interest to pay: '))
years = int(input('How many years would you like to calculate your money?: '))

amount *= round((1 + (interest / 100))**(years), 8)
print(amount)

