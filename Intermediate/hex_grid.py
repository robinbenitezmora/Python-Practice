import pyautogui
import math

X_REPEAT = 19
Y_REPEAT = 14

def drawHexagon(x, y, size):
    for i in range(6):
        x2 = x + math.cos(i * 2 * math.pi / 6) * size
        y2 = y + math.sin(i * 2 * math.pi / 6) * size
        pyautogui.moveTo(x, y)
        pyautogui.dragTo(x2, y2, duration=0.25)

def drawHexGrid():
    for y in range(Y_REPEAT):
        for x in range(X_REPEAT):
            size = 20
            if y % 2 == 0:
                drawHexagon(100 + x * size * 2, 100 + y * size * math.sqrt(3), size)
            else:
                drawHexagon(100 + x * size * 2 + size, 100 + y * size * math.sqrt(3), size)

if __name__ == '__main__':
    drawHexGrid()
# Compare this snippet from Intermediate/hex_grid.py:
#