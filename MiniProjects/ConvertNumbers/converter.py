one_digits_word = {
    0: ['zero'],
    1: ['one'],
    2: ['two', 'twen'],
    3: ['three', 'thir'],
    4: ['four', 'for'],
    5: ['five', 'fif'],
    6: ['six'],
    7: ['seven'],
    8: ['eight'],
    9: ['nine'],
}

two_digits_word = {'ten', 'eleven', 'twelve'}
hundred = 'hundred'
large_sum_words = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quiantillion', 'sixtillion', 'septillion', 'octallion', 'nonillion']

def convert_number_to_words(number):
    if number == 0:
        return 'zero'
    elif number < 0:
        return 'negative ' + convert_number_to_words(-number)
    else:
        return convert_positive_number_to_words(number)

def convert_positive_number_to_words(number):
    if number < 10:
        return one_digits_word[number][0]
    elif number < 20:
        return two_digits_word[number - 10]
    elif number < 100:
        return convert_two_digits_to_words(number)
    else:
        return convert_large_number_to_words(number)

def convert_two_digits_to_words(number):
    tens = number // 10
    ones = number % 10
    if ones == 0:
        return one_digits_word[tens][1]
    else:
        return one_digits_word[ones][0] + 'ty ' + convert_positive_number_to_words(ones)

def convert_large_number_to_words(number):
    for i, word in enumerate(large_sum_words):
        if number < 1000 ** (i + 2):
            break
    large_sum = 1000 ** (i + 1)
    return convert_positive_number_to_words(number // large_sum) + ' ' + word + ' ' + convert_positive_number_to_words(number % large_sum)

if __name__ == '__main__':
    print(convert_number_to_words(0))
    print(convert_number_to_words(1))
    print(convert_positive_number_to_words(34))
    print(convert_positive_number_to_words(100))
    print(convert_two_digits_to_words(12))
    print(convert_large_number_to_words(123456789))
    print(convert_number_to_words(123456789))
    print(convert_number_to_words(1000000000000))
