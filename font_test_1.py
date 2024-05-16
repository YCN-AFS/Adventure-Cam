import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font từ tệp tin .ttf
font_path = "game/RetroGaming.ttf"
font_size = 40
custom_font = pygame.font.Font(font_path, font_size)

# Tải hình cái loa
speaker_image_path = "loa.png"
speaker_image = pygame.image.load(speaker_image_path)
speaker_image = pygame.transform.scale(speaker_image, (
30, 30))  # số liệu chị k biết cân chưa, chị k biết bỏ vào khúc nào trong code để chạy thử kt :((

# Khởi tạo cửa sổ (Khúc này em coi lại giúp chị xem có cần tạo lại sửa sổ không nha, chị thấy nó là sửa sổ menu nên nghĩ có mà không chắc nữa)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Main Menu", custom_font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

        mx, my = pygame.mouse.get_pos()

        # Nút Bắt đầu
        start_button = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)  # đoạn này em coi số liệu giúp chị xem cân chưa nha
        pygame.draw.rect(screen, BLACK, start_button)
        draw_text("Bắt đầu", custom_font, WHITE, screen, WIDTH // 2, 175)
        if start_button.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                game_loop()

        # Nút Chơi tiếp
        continue_button = pygame.Rect(WIDTH // 2 - 100, 225, 200, 50)
        pygame.draw.rect(screen, BLACK, continue_button)
        draw_text("Chơi tiếp", custom_font, WHITE, screen, WIDTH // 2, 250)
        if continue_button.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                print("Chơi tiếp")

        # Nút Kỉ lục
        highscore_button = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, highscore_button)
        draw_text("Kỉ lục", custom_font, WHITE, screen, WIDTH // 2, 325)
        if highscore_button.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                print("Xem kỉ lục")

        # Nút Âm thanh
        sound_button = pygame.Rect(WIDTH // 2 - 100, 375, 200, 50)
        pygame.draw.rect(screen, BLACK, sound_button)
        draw_text("Âm thanh", custom_font, WHITE, screen, WIDTH // 2, 400)
        if sound_button.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                print("âm thanh")
                # Vẽ cái loa
        screen.blit(speaker_image, (30, 30))
        # khúc liên quan âm thanh chị không biết đúng không do trên có nói cái hình cái loa. với cái âm thanh là cái file âm thanh của game, c k biết lấy chỗ nào

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":  # để bảo vệ và chắc chắn khối lệnh chỉ chạy trên tệp trực tiếp. Khi chạy trên tệp trực tiếp thì hàm main_menu sẽ được gọi
    main_menu()