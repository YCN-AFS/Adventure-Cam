import pygame
import sys
import os


# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
os.environ['SDL_VIDEODRIVER'] = '1'
info = pygame.display.Info()

GAME_WIDTH, GAME_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((GAME_WIDTH-10, GAME_HEIGHT-50), pygame.RESIZABLE)

pygame.display.set_caption("Advan")

# Định nghĩa màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
bright_red = (255, 100, 100)
bright_green = (100, 255, 100)
bright_black = (100, 100, 100)

# Định nghĩa phông chữ
font = pygame.font.Font('../ninja_game/RetroGaming.ttf', 60)

# Tạo các nút
class Button:
    def __init__(self, text, x, y, width, height, color, bright_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.bright_color = bright_color
        self.current_color = color
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self):
        return self.clicked

# Tạo các nút
# rectangle =  pygame.Rect(0, GAME_WIDTH, )
start_button = Button("Start", GAME_WIDTH/2.3, 150, 300, 100, red, bright_red)
options_button = Button("Options", GAME_WIDTH/2.3, 300, 300, 100, green, bright_green)
quit_button = Button("Quit", GAME_WIDTH/2.3, 450, 300, 100, black, bright_black)
buttons = [start_button, options_button, quit_button]


# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_hovered():
                    button.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for button in buttons:
                if button.clicked:
                    button.clicked = False
                    if button.is_hovered():
                        if button.text == "Start":
                            print("Start button clicked")
                            Game.run()
                            break
                        elif button.text == "Options":
                            print("Options button clicked")
                        elif button.text == "Quit":
                            print("Quit button clicked")
                            running = False

    screen.fill(white)

    for button in buttons:
        if button.clicked or button.is_hovered():
            button.current_color = button.bright_color
        else:
            button.current_color = button.color
        button.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
