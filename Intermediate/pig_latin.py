'''
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Convert the word from English to Pig Latin.
4. Display the translation result.
'''

try:
    import pyperclip
except ImportError:
    print('pyperclip module is not installed. Install it using pip install pyperclip')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def pig_latin(word):
    if word[0].lower() in VOWELS:
        return word + 'yay'
    return word[1:] + word[0] + 'ay'

def main():
    print('Pig Latin Translator')
    print('Enter a word in English to translate to Pig Latin')
    word = input()
    if word.isalpha():
        translation = pig_latin(word)
        print(f'The Pig Latin translation of {word} is {translation}')
        pyperclip.copy(translation)
        print('The translation has been copied to the clipboard')
    else:
        print('Invalid word. Please enter a valid word')

if __name__ == '__main__':
    main()
    