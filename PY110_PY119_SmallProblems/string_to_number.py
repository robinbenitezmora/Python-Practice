'''To compute an integer value from a string of digits, you should know that the rightmost digit is the "ones" digit; that is, it contributes its value to the overall result. If there's another digit to the left of that digit, that digit is the "tens" digit; it contributes its value times 10 to the overall result.

To convert a string like "5372" to an integer, you need to understand how our decimal numbers work. In this case, 2 is in the "ones" position, 7 is in the tens position, 3 in the hundreds position, and 5 in the thousands position:

digits	5	3	7	2
ones				2
tens			70	
hundreds	300		
thousands5000			
Thus, we can calculate the numeric value of "5372" as 5000 + 300 + 70 + 2, or 5372.'''

def string_to_integer(string):
    length = len(string)
    num = 0
    for i in range(length):
        num += (ord(string[i]) - 48) * 10 ** (length - i - 1)
    return num

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

