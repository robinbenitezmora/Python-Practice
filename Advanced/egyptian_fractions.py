'''Write two functions: one that takes a Rational number as an argument, and returns a list of the denominators that are part of an Egyptian Fraction representation of the number, and another that takes a list of numbers in the same format, and calculates the resulting Rational number. You will need to use the Fraction class provided by the fractions module.'''

from fractions import Fraction

def egyptian(rational):
    result = []
    while rational > 0:
        n = 1
        while Fraction(1, n) > rational:
            n += 1
        result.append(n)
        rational -= Fraction(1, n)
    return result

def unegyptian(egyptian):
    return sum(Fraction(1, n) for n in egyptian)

from fractions import Fraction

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
