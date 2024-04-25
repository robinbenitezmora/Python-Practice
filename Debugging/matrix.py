
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())
x = int(input("Enter a value between 0 and 2: "))
y = int(input("Enter another value between 0 and 2: "))
matrix[x][y] = "X"

#matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]