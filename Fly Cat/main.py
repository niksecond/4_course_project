import pygame
from settings import WIDTH, HEIGHT
from resources import IMAGES

pygame.init()

# Инициализация окна и таймера
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Настройки окна
pygame.display.set_caption('Fly Cat')
pygame.display.set_icon(pygame.image.load(IMAGES['icon']))

# Инициализация игрока
py, sy, ay = HEIGHT // 2, 0, 0
player = pygame.Rect(WIDTH // 3, py, 34, 24)
frame = 0

# Состояния игры и другие параметры
state = 'menu'  # Изначальное состояние игры (меню)
timer = 10
fullscreen = False
paused = False
screen_button_text = 'Полноэкранный режим'  # Изначальный текст кнопки

# Инициализация списков объектов игры
pipes = []  # Список для труб, которые будут генерироваться
bges = []  # Список для фонов
pipesScores = []  # Список для отслеживания труб, которые были пройдены для получения очков
coins = []  # Список для монет, которые игрок может собирать

# Фон
bges.append(pygame.Rect(0, 0, 288, 600))

# Создаем кнопки меню
exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 1.1, 200, 50)
