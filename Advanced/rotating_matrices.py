'''Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. The function should not mutate the original matrix.'''

def rotate_90(matrix):
    return [[row[i] for row in matrix][::-1] for i in range(len(matrix[0]))]

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate_90(matrix1)
new_matrix2 = rotate_90(matrix2)
new_matrix3 = rotate_90(rotate_90(rotate_90(rotate_90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
print(matrix1 == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])
print(matrix2 == [[3, 7, 4, 2], [5, 1, 0, 8]])
print(rotate_90([[1, 2, 3, 4]]))            # [[4], [3], [2], [1]]