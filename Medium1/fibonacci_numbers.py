'''he Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2) where n > 2
This simple sequence can be computed using a recursive function. Write a recursive function that computes the nth Fibonacci number, where nth is an argument passed to the function.'''

def fibonacci(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
print(fibonacci(100) == 354224848179261915075) # True
print(fibonacci(1000) == 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501) # True
print(fibonacci(10000) == 20793608237133498072112648988642836825087036094015903119682945866528501423455686648927456034305226515591757343297190158010624794267250973176133810179902738038231789748346235556483191431591924532394420028067810320408724414693462849062668387083308048366) # True
print(fibonacci(100000) == 25974069347221724166155034021275915414880485386517696584724770703952534543511273686265556772836716744754637587223074432111638399473875091030965697382188304493052287638531334921353026792789567010512765782716356080730505322002432331143839865151) # True  