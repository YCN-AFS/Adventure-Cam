import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MENU GAME")

# Load hình ảnh nền
background_image = pygame.image.load(
    "./data/images/background.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Định nghĩa màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
bright_red = (255, 100, 100)
bright_green = (100, 255, 100)
bright_black = (100, 100, 100)

# Định nghĩa phông chữ
font = pygame.font.Font('RetroGaming.ttf', 60)

# Định nghĩa các hàm để hiển thị text
def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def message_display_top(text, y_displace=0, font_size='large'):
    if font_size == 'large':
        text_surface, text_rect = text_objects(text, font)
    elif font_size == 'small':
        text_surface, text_rect = text_objects(text, smallfont)
    text_rect.midtop = (screen_width / 2, y_displace)
    screen.blit(text_surface, text_rect)    

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
start_button = Button("Start", 200, 150, 300, 100, red, bright_red)
options_button = Button("Options", 200, 300, 300, 100, green, bright_green)
quit_button = Button("Quit", 200, 450, 300, 100, black, bright_black)
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
                        elif button.text == "Options":
                            print("Options button clicked")
                        elif button.text == "Quit":
                            print("Quit button clicked")
                            running = False

     # Hiển thị hình nền
        screen.blit(background_image, (0, 0))

     # Hiển thị tiêu đề game
        nav_height = 30  # Chiều cao của thanh điều hướng (navigation bar)
        message_display_top("Ninja Game", nav_height + 10, 'large') 

    for button in buttons:
        if button.clicked or button.is_hovered():
            button.current_color = button.bright_color
        else:
            button.current_color = button.color
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
