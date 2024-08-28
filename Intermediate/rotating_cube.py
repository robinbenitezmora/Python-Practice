'''
Rotating Cube is a simple example of a 3D object rotating in space.
The program uses the colorama library to print colored text on the terminal.
The program prints a rotating cube on the terminal by printing colored text in a loop.
The program uses the colorama library to print colored text on the terminal.
'''

import math, time, sys, os

PAUSE_AMOUNT = 0.1
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8

SCALEY += 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

LINE_CHAR = chr(9608)

X_ROTATE_SPEED = 0.07
Y_ROTATE_SPEED = 0.13
Z_ROTATE_SPEED = 0.2

X = 0
Y = 1
Z = 2

def line(x1, y1, x2, y2):
    points = []
    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2)
    ystep = 1 if y1 < y2 else -1
    y = y1
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        points.reverse()
    return points

def rotate2d(x, y, radians):
    cos = math.cos(radians)
    sin = math.sin(radians)
    nx = x * cos + y * sin
    ny = y * cos - x * sin
    return nx, ny

def render(screen, points):
    screen.clear()
    for p in points:
        x, y = p[X] * SCALEX + TRANSLATEX, p[Y] * SCALEY + TRANSLATEY
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            screen[int(x)][int(y)] = LINE_CHAR
    for i in range(len(screen)):
        print(''.join(screen[i]))

def main():
    screen = [[' ' for _ in range(HEIGHT)] for _ in range(WIDTH)]
    angle_x, angle_y, angle_z = 0, 0, 0
    while True:
        t = time.time()
        points = []
        for i in range(8):
            x = i & 1
            y = i & 2
            z = i & 4
            if x:
                y, z = rotate2d(y, z, angle_x)
            if y:
                x, z = rotate2d(x, z, angle_y)
            if z:
                x, y = rotate2d(x, y, angle_z)
            points.append((x, y, z))
        render(screen, points)
        angle_x += X_ROTATE_SPEED
        angle_y += Y_ROTATE_SPEED
        angle_z += Z_ROTATE_SPEED
        time_to_sleep = PAUSE_AMOUNT - (time.time() - t)
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
