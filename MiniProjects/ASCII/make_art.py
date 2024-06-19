import cv2
import numpy as np
import sys

symbol_list = ["#", "-", "*", ".", "+", "o"]
threshold_list = [0, 50, 100, 150, 200]

def print_ascii(array):
    '''prints the coded image with symbols'''

    for row in array:
        for pixel in row:
            sys.stdout.write(symbol_list[pixel//50])
        sys.stdout.write('\n')

def convert_to_ascii(image):
    '''converts the image to a coded image'''

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ascii_image = np.zeros_like(gray, dtype=int)

    for i, threshold in enumerate(threshold_list):
        ascii_image[np.where(gray > threshold)] = i

    return ascii_image

def main():
    '''main function'''

    image = cv2.imread('image.jpg')
    ascii_image = convert_to_ascii(image)
    print_ascii(ascii_image)

if __name__ == '__main__':
    main()
