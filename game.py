import pygame
from game_objects import Animation, Player
#from pygame.locals import *
# import os
# import re


# Game constants


GAME_WIDTH = int(1920/1.2)
GAME_HEIGHT = int(1080/1.2)
PLAYER_SPEED = 4
# JUMP_HEIGHT = -170
# GRAVITY = 10
FPS = 60
ANIMATION_SPEED = 110


# Set up
pygame.init()
icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
last_update = pygame.time.get_ticks()


#Animation
Warrior_Sheet_image = pygame.image.load('assets/characters/Warrior/Warrior_Sheet-Effect.png').convert_alpha()
animation = Animation(Warrior_Sheet_image, screen)
animation.load_image("assets/background/map_0")


#create list animations
animation_list = []
animmation_steps = 6
frame = 0
for i in range(animmation_steps):
     animation_list.append(animation.get_image((i, 1), 69, 44))


#Player obj
player = Player(screen)
pygame.display.set_caption("Adventure Cam")
clock = pygame.time.Clock()

# Load sounds
# jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")
# hurt_sound = pygame.mixer.Sound("assets/sound/hurt.wav")


# Game loop
running = True
while running:
    clock.tick(FPS)

    # draw_ground()
    character_position = player.character_action(player_speed=PLAYER_SPEED)
    animation.draw_background(character_position)
    #Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= ANIMATION_SPEED:
        frame += 1
        if frame >= len(animation_list):
            frame = 0
        last_update = current_time

    screen.blit(animation_list[frame], (0,640))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    # screen.blit(background, (0, 0))
    #screen.blit(middleground, (0, 80))
    # player.draw(screen)
    # pygame.display.update()

pygame.quit()