
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

num = int(input('Enter how many stars you want in the triangle: '))

def tringle(n):
    for i in range(1, n+1):
        print(' '* (n-i) + '*'*i)

tringle(num)