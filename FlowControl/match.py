value = int(input('Enter a value between 1 to 6: '))

match value:
    case 1 | 2 | 3 | 4:
        print('Value is < 5')
    case 5 | 6:
        print('Value is 5 or 6')
    case _:
        print('Value is not 1, 2, 3, 4, 5 or 6')

