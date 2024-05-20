import pygame
from time import sleep
from random import randint

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elastic Bounce")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 200, 200)

# Define ball properties
ball_radius = 20
ball_x = randint(0, width-1)
ball_y = randint(0, height-1)
ball_speed_x = 5
ball_speed_y = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x  # Reverse horizontal speed
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y  # Reverse vertical speed

    # Clear the screen
    # screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()
    sleep(0.04)

# Quit Pygame
pygame.quit()