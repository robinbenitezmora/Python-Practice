print('Multiplication Table')
print(' | 0 1  2  3  4  5  6  7  8  9 10 11 12')
print('-----------------------------------------------------')

for i in range(13):
    print(i, end='|')
    for j in range(13):
        print(f'{i * j:3}', end=' ')
    print()
