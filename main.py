import pygame
import random # Не забудьте импортировать random

pygame.init()

# --- НАЧАЛО НОВОГО КОДА ---
# 1. Константы и создание окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 2. Заголовок и иконка
pygame.display.set_caption("Игра Тир")
# Создайте папку 'images' и положите туда ваши файлы
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# 3. Настройка цели
target_img = pygame.image.load("images/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# 4. Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# --- КОНЕЦ НОВОГО КОДА ---

running = True
while running:
    # --- НАЧАЛО НОВОГО КОДА ВНУТРИ ЦИКЛА ---
    screen.fill(color) # Заливаем экран цветом

    # Обработка событий
    for event in pygame.event.get():
        # Событие: закрытие окна
        if event.type == pygame.QUIT:
            running = False

        # Событие: клик мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверка попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Если попал, генерируем новые координаты
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

pygame.quit()