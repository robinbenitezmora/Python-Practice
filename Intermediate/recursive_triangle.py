def triangle(n):
    return recursive_triangle(n, n)

def recursive_triangle(x, n):
    if type(x) != int or type(n) != int:
        return "Invalid input"
    
    if x > n:
        x = n
    if x == 0 or n == 0:
        return ''
    
    start_print = n
    line_number = x

    difference = start_print - line_number
    
    if difference != 0:
        print(' ' * difference, end='')

    print('*' * line_number)
    return recursive_triangle(x-1, n)

triangle(12)
