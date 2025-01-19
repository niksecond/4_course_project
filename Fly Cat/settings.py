import pygame

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Инициализация Pygame
pygame.init()

# Шрифты
font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 80)

# Настройки громкости
music_volume = 0.1
sound_volume = 0.5

# Загрузка музыки и звуков
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)

# Настройки громкости для музыки и звуков в игре
sndFall = pygame.mixer.Sound('sounds/fall.wav')
sndFall.set_volume(sound_volume)

# Настройки игры
pipeSpeed = 3  # Скорость движения труб
pipeGateSize = 200  # Размер отверстия между верхней и нижней трубой
pipeGatePos = HEIGHT // 2  # Позиция отверстия по вертикали (по умолчанию в центре экрана)

# Игровые параметры
lives = 3  # Начальное количество жизней у игрока
scores = 0  # Начальный счет
