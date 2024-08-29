'''
Seven Segment Display
'''

def getSevSegStr(number, minWidth=0):
    '''
    Returns the seven segment display representation of the number
    '''
    number = str(number).zfill(minWidth)

    rows = ['', '', '', '']

    for i, numeral in enumerate(number):
        if numeral == '0':
            rows[0] += ' _ '
            rows[1] += '| |'
            rows[2] += '|_|'
        elif numeral == '1':
            rows[0] += '   '
            rows[1] += '  |'
            rows[2] += '  |'
        elif numeral == '2':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += '|_ '
        elif numeral == '3':
            rows[0] += ' _ '
            rows[1] += ' _|'
            rows[2] += ' _|'
        elif numeral == '4':
            rows[0] += '   '
            rows[1] += '|_|'
            rows[2] += '  |'
        elif numeral == '5':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += ' _|'
        elif numeral == '6':
            rows[0] += ' _ '
            rows[1] += '|_ '
            rows[2] += '|_|'
        elif numeral == '7':
            rows[0] += ' _ '
            rows[1] += '  |'
            rows[2] += '  |'
        elif numeral == '8':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += '|_|'
        elif numeral == '9':
            rows[0] += ' _ '
            rows[1] += '|_|'
            rows[2] += '  |'

        if i < len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
            rows[3] += ' '

    return '\n'.join(rows)

if __name__ == '__main__':
    print(getSevSegStr(1234567890, 10))
    print(getSevSegStr(1234567890))
    print(getSevSegStr(1234567890, 5))
    print(getSevSegStr(1234567890, 2))
    print(getSevSegStr(1234567890, 1))
    print(getSevSegStr(1234567890, 0))
    print(getSevSegStr(0))
    print(getSevSegStr(1))
    print(getSevSegStr(2))
    print(getSevSegStr(3))
    print(getSevSegStr(4))
    print(getSevSegStr(5))
    print(getSevSegStr(6))
    print(getSevSegStr(7))
    print(getSevSegStr(8))
    print(getSevSegStr(9)) 
