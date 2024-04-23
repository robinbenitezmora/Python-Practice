
def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) == len(string2):
        return 0
    else:
        return 1

print(compare_by_length('patience', 'perseverance'))# -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0        