
def is_empty_or_blank(s):
    return len(s.strip()) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True