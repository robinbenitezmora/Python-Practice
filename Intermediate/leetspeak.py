import random

try:
    import pyperclip
except ImportError:
    print("This program requires the pyperclip module.")
    print("You can install it by running: pip install pyperclip")
    print("Exiting...")
    pass

def leetspeak(text):
    leet = {'a': '4', 'b': '8', 'c': '(', 'e': '3', 'g': '6', 'h': '#', 'i': '!', 'l': '1', 'o': '0', 's': '$', 't': '7', 'z': '2'}
    leetspeakText = ''
    for char in text:
        leetspeakText += leet.get(char.lower(), char)
    return leetspeakText

def main():
    print("Enter the text to convert to Leetspeak:")
    text = input()
    leetspeakText = leetspeak(text)
    print(f"Leetspeak version: {leetspeakText}")
    pyperclip.copy(leetspeakText)
    print("This text has been copied to the clipboard.")

if __name__ == '__main__':
    main()
