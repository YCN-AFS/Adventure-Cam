import pygame
import os
import re

class Animation():
    def __init__(self,  image, screen):
        self.sheet = image
        self.pose_x = 0
        self.pose_y = 640
        self.screen = screen
        self.bg_width = self.sheet.get_width()
        self.bg_height = self.sheet.get_height()
        self.bg_image = []


    def get_image(self, frame, width, height, scale=2):
        """Load character movement frames and process them"""
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame[0] * width, frame[1] * height, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))
        return image


    def load_image(self, directory_path):
        """Load frames from the dictionary"""
        frame_list = os.listdir(directory_path)
        frame_list = sorted(frame_list, key=lambda x: int(re.search(r'\d+', x).group()))
        # bg_image = []
        for i in frame_list:
            self.bg_image.append(pygame.image.load(directory_path + "/" + i).convert_alpha())
        # return bg_image

    def draw_background(self, x_position, map_length = 30):
        """Draw background on the screen"""
        for x in range(map_length):
            speed = 1
            for i in self.bg_image:
                self.screen.blit(i, (x * self.bg_width - x_position * speed, 0))
                speed += 0.2
    def draw_rec(self):
        pass

    # def  load_images(self, url):
    #     bg_image = []
    #     for i in range(9):
    #         bg_image.append(pygame.image.load(f"assets/background/map_0/Layer_{i}.png").convert_alpha())

    # def draw_background(self):
    #     for x in range(5):
    #         speed = 1
    #         for i in bg_image:
    #             self.screen.blit(i, (x * bg_width - scroll * speed, 0))
    #             speed += 0.2




class Player(pygame.sprite.Sprite, Animation):
    def __init__(self, screen, pose_x, pose_y):
        super().__init__()
        self.sprites = []
        self.pose_x = pose_x
        self.pose_y = pose_y
        self.y_velocity = 0
        # self.screen = screen
        # self.image = pygame.Surface([20,20])
        # self.image.fill((255,255,255))
        # self.rect = self.image
        # self.rect.topleft = [pose_y,pose_y]

    def update_position(self, player_speed, jump_height, gravity):
        # super().__init__()
        """ Update the position of the player"""
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.pose_x > 0:
            self.pose_x -= player_speed
        elif key[pygame.K_d] and self.pose_x < 6000:
            self.pose_x += player_speed


        #Kiểm tra nhân vật đã tiếp đất hay chưa
        #640 là nền đất được gán cứng, int(1080/1.2) là chiều cao màn hình
        #https://youtu.be/s53T6eRdZpw?si=1xCXmzOSXbBH-uCt
        if self.pose_y < 640:
            # Create gravity
            self.y_velocity += gravity
            self.pose_y += self.y_velocity

        if key[pygame.K_SPACE]:
            self.pose_y -= jump_height
            print("Jumping")
        return self.pose_x, self.pose_y

    # def draw_background(self, screen):
    #     for x in range(5):
    #         speed = 1
    #         for i in bg_image:
    #             screen.blit(i, (x * bg_width - scroll * speed, 0))
    #             speed += 0.2

    # def update(self):
    #     keys = pygame.key.get_pressed()
    #     self.velocity_x = 0
    #
    #     if keys[pygame.K_LEFT]:
    #         self.velocity_x = -PLAYER_SPEED
    #         self.direction = "left"
    #     if keys[pygame.K_RIGHT]:
    #         self.velocity_x = PLAYER_SPEED
    #         self.direction = "right"
    #     if keys[pygame.K_SPACE] and self.on_ground:
    #         self.velocity_y = JUMP_HEIGHT
    #         #jump_sound.play()
    #
    #     self.velocity_y += GRAVITY
    #     self.rect.x += self.velocity_x
    #     self.rect.y += self.velocity_y
    #
    #     if self.rect.top > GAME_HEIGHT:
    #         self.rect.bottom = 0
    #
    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)


# class Background():
#     def __init__(self, image):
#         self.layer = image
#     pass
class Sound(pygame.sprite.Sprite):
    pass