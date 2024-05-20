import pygame
from game_objects import Animation, Player
#from pygame.locals import *
import os

# Game constants
GAME_WIDTH = int(1920/1.2)
GAME_HEIGHT = int(1080/1.2)
ANIMATION_SPEED = 110
FPS = 60



PLAYER_SPEED = 4
JUMP_HEIGHT = 20
X_POSITION = 0
Y_POSITION = 640
# JUMPING = False
GRAVITY = 1


# Set up
pygame.init()
icon = pygame.image.load('../ninja_game/icon.ico')
pygame.display.set_icon(icon)

# os.environ['SDL_VIDEODRIVER'] = '1'
# info = pygame.display.Info()
# GAME_WIDTH, GAME_HEIGHT = info.current_w, info.current_h

screen = pygame.display.set_mode((GAME_WIDTH-10, GAME_HEIGHT-50), pygame.RESIZABLE)
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


#Create a Player object
player = Player(screen, X_POSITION, Y_POSITION)
pygame.display.set_caption("Adventure Cam")
clock = pygame.time.Clock()

#Draw the main square
rect_1 = pygame.Rect(0, 0, 25, 25)
rect_2 = pygame.Rect(300, 500, 69, 44)


# Load sounds
# jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")
# hurt_sound = pygame.mixer.Sound("assets/sound/hurt.wav")


# Game loop
running = True
while running:
    clock.tick(FPS)

    COLOR = (0, 255, 0)
    #Get mouse
    pos = pygame.mouse.get_pos()
    rect_1.center = pos





    #Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= ANIMATION_SPEED:
        frame += 1
        if frame >= len(animation_list):
             frame = 0
        last_update = current_time

    # draw_ground()
    character_position = player.update_position(player_speed=PLAYER_SPEED, jump_height=JUMP_HEIGHT, gravity=GRAVITY)
    X_POSITION, Y_POSITION = character_position
    animation.draw_background(X_POSITION)

    #Draw characters
    screen.blit(animation_list[frame], (X_POSITION,Y_POSITION))

    # draw rec
    if rect_1.colliderect(rect_2):
        COLOR = (0, 0, 255)
    pygame.draw.rect(screen, (255, 0, 0), rect_1)
    pygame.draw.rect(screen, COLOR, rect_2)






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()



pygame.quit()