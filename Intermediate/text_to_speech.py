import sys

try:
    import pyttsx3
except ImportError:
    print("pyttsx3 is not installed. Please install it using pip install pyttsx3")
    sys.exit(1)

tts = pyttsx3.init()
print("Enter the text to speak or QUIT to exit")
while True:
    text = input("Enter the text: ")
    if text.upper() == "QUIT":
        break
    tts.say(text)
    tts.runAndWait()

tts.stop()
tts.runAndWait()
tts.end()
