import pygame

# Загрузка изображений
IMAGES = {
    "background": 'images/background.png',  # Изображение фона
    "cat": 'images/cat.png',  # Изображение игрока (кот)
    "pipe_top": 'images/pipe_top.png',  # Изображение верхней трубы
    "pipe_bottom": 'images/pipe_bottom.png',  # Изображение нижней трубы
    "coin_cat": 'images/coin_cat.png',  # Изображение монеты
    'pausebg': 'images/pausebg.png',  # Изображение фона для паузы
    'icon': 'images/icon.png'  # Иконка игры
}

imgBG = pygame.image.load(IMAGES['background'])  # Фон игры
imgCat = pygame.image.load(IMAGES['cat'])  # Картинка с котом (игрок)
imgPT = pygame.image.load(IMAGES['pipe_top'])  # Верхняя труба
imgPB = pygame.image.load(IMAGES['pipe_bottom'])  # Нижняя труба
imgCoin = pygame.image.load(IMAGES['coin_cat'])  # Монета (с изображением кота)
