'''Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.'''

def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char

    return result

print(staggered_case('I Love Launch School!'))        # "I LoVe lAuNcH ScHoOl!"
print(staggered_case('ALL_CAPS'))                     # "AlL_CaPs"
print(staggered_case('ignore 77 the 4444 numbers'))   # "IgNoRe 77 ThE 4444 nUmBeRs"
