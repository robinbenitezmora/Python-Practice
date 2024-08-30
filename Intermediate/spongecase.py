import random, sys

try:
    import pyperclip
except ImportError:
    print("Please install pyperclip module: pip install pyperclip")
    print("Exiting...")
    sys.exit()

def spongecase(text):
    newText = ''
    for i, letter in enumerate(text):
        if i % 2 == 0:
            newText += letter.upper()
        else:
            newText += letter.lower()
    return newText

def main():
    print('Enter text to convert to SpongeCase:')
    text = input()
    newText = spongecase(text)
    print('SpongeCase text:')
    print(newText)
    pyperclip.copy(newText)
    print('SpongeCase text copied to clipboard.')

if __name__ == '__main__':
    main()
