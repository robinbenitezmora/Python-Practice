import pygame, time, random

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background-img.jpg')

# Set the title of the window
pygame.display.set_caption("Bouncing Ball")

# Set the color of the ball
ball_color = (255, 0, 0)

# Set the size of the ball
ball_radius = 20

# Set the initial position of the ball
ball_x = 400

# Set the initial velocity of the ball
ball_velocity_x = 0

# Set the initial position of the ball
ball_y = 300

# Set the initial velocity of the ball
ball_velocity_y = 0

class ball:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, velocity_x):
        self.x += velocity_x
        self.y += velocity_y

        if self.x < 0 or self.x > 768:
            self.velocity_x *= -1

        if self.y < 0 or self.y > 0:
            self.velocity_y *= -1
            self.y = 0

        if self.y > 568 and self.velocity_y > 0:
            self.velocity_y *= -1
            self.y = 568

# Create a ball object
Ball_List = [ball(), ball(), ball(), ball(), ball()]

# The main program loop
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.02)
    screen.fill((0, 0, 0))

    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()

    pygame.display.update()
