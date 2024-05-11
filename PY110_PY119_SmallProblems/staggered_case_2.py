'''Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.'''

def staggered_case(string, start_upper=True):
    result = ''
    upper = start_upper

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

print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")