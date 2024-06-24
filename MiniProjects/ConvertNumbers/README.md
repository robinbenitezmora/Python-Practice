# Convert Numbers To Words

## Description

This program converts numbers to words. It takes a number as input and returns the number in words. For example, if the input is 123, the output will be "one hundred twenty three".

## Prerequisites

- Python 3.x

## How to use

1. Clone the repository

2. Run the script with the following command:

```bash
python convert_numbers_to_words.py
```

## Example

If the input is 123, the output will be:

```bash
one hundred twenty three
```

## Function Signature

```python

def convert_number_to_words(number: int) -> str:

```

## Note

- The program can convert numbers up to 999,999,999,999. If the input is greater than 999,999,999,999, the program will raise a `ValueError`.

- The program can convert negative numbers. If the input is a negative number, the output will start with the word "negative". For example, if the input is -123, the output will be "negative one hundred twenty three".

- The program can convert decimal numbers. If the input is a decimal number, the output will include the word "point". For example, if the input is 123.45, the output will be "one hundred twenty three point four five".

- The program can convert numbers with leading zeros. If the input is 00123, the output will be "one hundred twenty three".

- The program can convert numbers with trailing zeros. If the input is 123.4500, the output will be "one hundred twenty three point four five".

- The program can convert numbers with commas. If the input is 1,000,000, the output will be "one million".

- The program can convert numbers with spaces. If the input is 1 000 000, the output will be "one million".

- The program can convert numbers with underscores. If the input is 1_000_000, the output will be "one million".
