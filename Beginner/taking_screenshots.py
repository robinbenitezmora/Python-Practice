'''
How to play taking screenshots game:
1. Enter the number of screenshots to take
2. The screenshots will be saved in the current directory
3. The game ends after taking the specified number of screenshots
'''

import pyautogui
import time

def take_screenshots(num_screenshots):
    for i in range(num_screenshots):
        screenshot = pyautogui.screenshot()
        screenshot.save(f'screenshot_{i + 1}.png')
        time.sleep(1)

def main():
    num_screenshots = int(input('Enter the number of screenshots to take:\n'))
    take_screenshots(num_screenshots)
    print(f'\n{num_screenshots} screenshots taken successfully!')

if __name__ == '__main__':
    main()
