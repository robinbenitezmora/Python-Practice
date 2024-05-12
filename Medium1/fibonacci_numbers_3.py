'''Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed. In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

An image representing the computation of the 7th Fibonacci number is shown below. It is the same image that was shown in the previous exercise, except this one highlights the values that have previously been computed.

Fibonacci Memoization

Hint: One approach to memoization is to use a lookup table, such as an object, for storing and accessing previously computed values.'''

def fibonacci_memoization(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    return fibonacci_memoization(number - 1) + fibonacci_memoization(number - 2)

print(fibonacci_memoization(1) == 1)         # True
print(fibonacci_memoization(2) == 1)         # True
print(fibonacci_memoization(3) == 2)         # True
print(fibonacci_memoization(4) == 3)         # True
print(fibonacci_memoization(5) == 5)         # True
print(fibonacci_memoization(6) == 8)         # True
print(fibonacci_memoization(12) == 144)      # True
print(fibonacci_memoization(20) == 6765)     # True
print(fibonacci_memoization(50) == 12586269025) # True
