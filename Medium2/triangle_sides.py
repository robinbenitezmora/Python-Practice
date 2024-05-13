'''A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.'''

def triangle(dim1, dim2, dim3):
    if dim1 + dim2 > dim3 and dim1 + dim3 > dim2 and dim2 + dim3 > dim1:
        if dim1 == dim2 == dim3:
            return "Equilateral"
        elif dim1 == dim2 or dim1 == dim3 or dim2 == dim3:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Invalid"

print(triangle(3, 3, 3) == "Equilateral")  # True
print(triangle(3, 3, 1.5) == "Isosceles")  # True
print(triangle(3, 4, 5) == "Scalene")      # True
print(triangle(0, 3, 3) == "Invalid")      # True
print(triangle(3, 1, 1) == "Invalid")      # True
