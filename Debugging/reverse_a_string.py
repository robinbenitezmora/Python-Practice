# You have a function that should reverse a given string. However, it's not producing the expected output.

def reverse_string(s):
    for char in s:
        return s[::-1]

print(reverse_string('hello')) # Expected output: 'olleh
print(reverse_string('world')) # Expected output: 'dlrow'
print(reverse_string('')) # Expected output: ''
print(reverse_string('12345')) # Expected output: '54321'
print(reverse_string('l')) # Expected output: 'l'
print(reverse_string('hi')) # Expected output: 'ih'
print(reverse_string('123456789')) # Expected output: '987654321'
print(reverse_string('a')) # Expected output: 'a'

