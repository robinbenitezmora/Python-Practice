


def crunch(string):
    result = ''
    for i in string:
        print(result[-1:])
        if i == result[-1:]:
            continue
        else:
            result += i
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')