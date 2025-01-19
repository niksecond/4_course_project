from settings import *
from random import randint
from main import *
from resources import imgBG, imgCat, imgPT, imgPB, imgCoin


def handle_events():
    """
    Обрабатывает все события игры, включая нажатия клавиш, клики мыши и выход из игры.
    """
    global play, state, fullscreen, window, screen_button_text, music_volume, sound_volume
    global lives, scores, pipes, coins, pipesScores, pipeSpeed, timer, paused, click

    # Цикл обработки всех событий pygame
    for event in pygame.event.get():
        # Если событие - закрытие окна, завершить игру
        if event.type == pygame.QUIT:
            play = False

        # Если нажата кнопка мыши, обработать нажатие
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(event)

        # Если нажата клавиша, обработать нажатие клавиши
        if event.type == pygame.KEYDOWN:
            handle_key_press(event)


def handle_mouse_click(event):
    """
    Обрабатывает нажатия кнопок мыши в зависимости от текущего состояния игры (меню или игровой процесс).
     """
    global state, fullscreen, window, screen_button_text, music_volume, sound_volume, play
    global lives, scores, pipes, coins, pipesScores, pipeSpeed, timer

    # Обработка кликов в зависимости от текущего состояния игры
    if state == 'menu':
        handle_menu_click(event)
    elif state == 'play':
        handle_play_click(event)


def handle_menu_click(event):
    """
    Обрабатывает клики мыши в главном меню, определяя действия для кнопок:
    'Начать игру', 'Полноэкранный режим', 'Выйти из игры', 'Музыка', 'Звук'.
     """
    global state, fullscreen, window, screen_button_text, music_volume, sound_volume, play

    if start_button.collidepoint(event.pos):  # Кнопка для начала игры
        state = 'start'
        timer = 10
    elif screen_button.collidepoint(event.pos):  # Кнопка переключения режима экрана
        toggle_fullscreen()
    elif exit_button.collidepoint(event.pos):  # Кнопка выхода из игры
        play = False
    elif music_button.collidepoint(event.pos):  # Кнопка включения/выключения музыки
        toggle_music()
    elif sound_button.collidepoint(event.pos):  # Кнопка включения/выключения звуков
        toggle_sound()


def handle_play_click(event):
    """
    Обрабатывает клики мыши во время игры для взаимодействия с кнопками 'Меню' и 'Выход из игры'.
    """
    global state, lives, scores, pipes, coins, pipesScores, pipeSpeed, timer, play

    # Определение областей для кнопок "Выход из игры" и "Меню"
    exit_text = font1.render('Выход из игры', 1, 'black')
    exit_text_rect = pygame.Rect(WIDTH - 200, HEIGHT - 30, exit_text.get_width(), exit_text.get_height())

    menu_text = font1.render('Меню', 1, 'black')
    menu_text_rect = pygame.Rect(WIDTH - 80, 10, menu_text.get_width(), menu_text.get_height())

    # Проверка нажатия на кнопки
    if menu_text_rect.collidepoint(event.pos):  # Кнопка "Меню"
        reset_to_menu()
    elif exit_text_rect.collidepoint(event.pos):  # Кнопка "Выход из игры"
        play = False


def handle_key_press(event):
    """
    Обрабатывает нажатия клавиш во время игры:
    'Escape' для паузы, 'Пробел' для действий в зависимости от состояния игры.
    """
    global paused, state, lives, scores, pipes, coins, pipesScores, pipeSpeed

    # Обработка нажатия клавиши "Escape" для паузы или выхода
    if event.key == pygame.K_ESCAPE and state == 'play':
        paused = not paused
    # Обработка нажатия клавиши "Пробел"
    elif event.key == pygame.K_SPACE:
        handle_space_press()


def handle_space_press():
    """
    Реализует действия по нажатию клавиши 'Пробел':
    снятие паузы или сброс игры после завершения.
    """
    global paused, state, lives, scores, pipes, coins, pipesScores, pipeSpeed

    # Если игра на паузе, снять с паузы
    if paused:
        paused = False
    # Если конец игры, сбросить параметры для новой игры
    elif state == 'game over' and not timer:
        reset_game()


def toggle_fullscreen():
    """
    Переключает полноэкранный режим игры на оконный и обратно.
    """
    global fullscreen, window, screen_button_text

    fullscreen = not fullscreen
    if fullscreen:
        # Переключение на полноэкранный режим
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        screen_button_text = 'Оконный режим'
    else:
        # Переключение на оконный режим
        window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        screen_button_text = 'Полноэкранный режим'


def toggle_music():
    """
    Включает или выключает музыку, изменяя громкость.
    """
    global music_volume

    # Если музыка включена, выключить, и наоборот
    music_volume = 0 if music_volume > 0 else 0.1
    pygame.mixer.music.set_volume(music_volume)


def toggle_sound():
    """
    Включает или выключает звуковые эффекты, изменяя громкость.
    """
    global sound_volume

    # Если звук включен, выключить, и наоборот
    sound_volume = 0 if sound_volume > 0 else 0.5
    sndFall.set_volume(sound_volume)


def reset_to_menu():
    """
    Сбрасывает состояние игры и возвращает пользователя в главное меню.
    """
    global state, lives, scores, pipes, coins, pipesScores, pipeSpeed, timer

    state = 'menu'  # Устанавливаем состояние меню
    lives = 3  # Восстанавливаем количество жизней
    scores = 0  # Сбрасываем счет
    pipes.clear()  # Очищаем список труб
    coins.clear()  # Очищаем список монет
    pipesScores.clear()  # Очищаем список труб для подсчета очков
    pipeSpeed = 3  # Устанавливаем начальную скорость труб
    timer = 180  # Обновляем таймер


def reset_game():
    """
    Полностью сбрасывает игру, включая счет, жизни и препятствия.
    """
    global state, lives, scores, pipes, coins, pipesScores, pipeSpeed

    lives = 3  # Восстанавливаем жизни
    scores = 0  # Обнуляем счет
    pipes.clear()  # Удаляем все трубы
    coins.clear()  # Удаляем все монеты
    pipesScores.clear()  # Очищаем список труб для подсчета очков
    pipeSpeed = 3  # Устанавливаем начальную скорость
    state = 'menu'  # Возвращаем в главное меню


def update_background():
    """
    Обновляет фон, перемещая его влево с учетом скорости движения.
    Если фон уходит за экран, он удаляется и добавляется новый.
    """
    for i in range(len(bges) - 1, -1, -1):  # Проходим по списку фонов с конца
        bg = bges[i]
        bg.x -= pipeSpeed // 2  # Перемещаем фон влево

        # Удаляем фон, если он вышел за пределы экрана
        if bg.right < 0:
            bges.remove(bg)

        # Если последний фон достигает края экрана, добавляем новый
        if bges[len(bges) - 1].right <= WIDTH:
            bges.append(pygame.Rect(bges[len(bges) - 1].right, 0, 288, 600))


def update_pipes():
    """
    Обновляет положение труб, перемещая их влево.
    Удаляет трубы, вышедшие за пределы экрана.
    """
    for i in range(len(pipes) - 1, -1, -1):  # Проходим по списку труб с конца
        pipe = pipes[i]
        pipe.x -= pipeSpeed  # Перемещаем трубу влево

        if pipe.right < 0:  # Удаляем трубу, если она вышла за пределы экрана
            pipes.remove(pipe)
            if pipe in pipesScores:  # Удаляем трубу из списка подсчета очков
                pipesScores.remove(pipe)


# Функция обновления монет в игре
def update_coins():
    """
    Обновляет положение монет, перемещая их влево.
    Удаляет монеты, вышедшие за пределы экрана, или собранные игроком.
    """
    global scores

    for i in range(len(coins) - 1, -1, -1):  # Проходим по монетам с конца списка
        coin = coins[i]
        coin.x -= pipeSpeed  # Перемещаем монету влево

        if coin.right < 0:  # Удаляем монету, если она вышла за пределы экрана
            coins.remove(coin)

        # Проверяем, собрал ли игрок монету
        if state == 'play' and lives > 0 and player.colliderect(coin):
            coins.remove(coin)  # Удаляем монету
            scores += 5  # Увеличиваем счет


# Функция для отрисовки кнопок меню
def draw_button(window, button, mouse_pos, color_default, color_hover):
    """
    Отрисовывает кнопку, изменяя её цвет при наведении мыши.

    :param window: объект окна Pygame, где рисуется кнопка
    :param button: прямоугольник, представляющий кнопку
    :param mouse_pos: позиция курсора мыши
    :param color_default: стандартный цвет кнопки
    :param color_hover: цвет кнопки при наведении
    """

    # Проверяем, наведена ли мышь на кнопку
    if button.collidepoint(mouse_pos):
        pygame.draw.rect(window, color_hover, button)  # Цвет при наведении
    else:
        pygame.draw.rect(window, color_default, button)  # Стандартный цвет

# Функция для отрисовки текста внутри кнопок
def draw_text(window, text, button):
    """
    Отрисовывает текст в центре кнопки.

    :param window: объект окна Pygame, где рисуется текст
    :param text: объект текста Pygame
    :param button: прямоугольник кнопки, внутри которого отрисовывается текст
    """
    window.blit(text, (button.x + (button.width - text.get_width()) // 2,
                       button.y + (button.height - text.get_height()) // 2))


def draw_centered_text(window, text, y_position):
    """
    Отрисовывает текст в центре экрана по горизонтали.

    :param window: объект окна Pygame, где рисуется текст
    :param text: объект текста Pygame
    :param y_position: координата Y для отрисовки текста
    """
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, y_position))


def draw_menu_buttons(window, mouse_pos):
    """
    Отображает кнопки меню с изменением цвета при наведении мыши.

    :param window: объект окна Pygame для отображения кнопок
    :param mouse_pos: текущая позиция курсора мыши
    """
    global start_button, screen_button, music_button, sound_button, exit_button

    # Создаем прямоугольники для кнопок
    start_button = pygame.Rect(WIDTH // 2 - 145, HEIGHT // 3, 290, 50)
    screen_button = pygame.Rect(WIDTH // 2 - 145, HEIGHT // 3 + 70, 290, 50)
    music_button = pygame.Rect(WIDTH // 2 - 145, HEIGHT // 3 + 140, 290, 50)
    sound_button = pygame.Rect(WIDTH // 2 - 145, HEIGHT // 3 + 210, 290, 50)
    exit_button = pygame.Rect(WIDTH // 2 - 145, HEIGHT // 3 + 280, 290, 50)

    # Отрисовка кнопок с соответствующими цветами
    draw_button(window, start_button, mouse_pos, (255, 69, 0), (139, 0, 0))
    draw_button(window, screen_button, mouse_pos, (70, 130, 180), (0, 191, 255))
    draw_button(window, music_button, mouse_pos, (255, 165, 0), (255, 223, 0))
    draw_button(window, sound_button, mouse_pos, (255, 165, 0), (255, 223, 0))
    draw_button(window, exit_button, mouse_pos, (139, 0, 0), (255, 0, 0))

    # Подготовка текста для кнопок
    start_text = font1.render('Начать игру', True, 'white')
    screen_text = font1.render(screen_button_text, True, 'white')
    music_text = font1.render(f'Музыка: {"ВКЛ" if music_volume > 0 else "ВЫКЛ"}', True, 'white')
    sound_text = font1.render(f'Звуки: {"ВКЛ" if sound_volume > 0 else "ВЫКЛ"}', True, 'white')
    exit_text = font1.render('Выйти из игры', True, 'white')

    # Отображение текста на кнопках
    draw_text(window, start_text, start_button)
    draw_text(window, screen_text, screen_button)
    draw_text(window, music_text, music_button)
    draw_text(window, sound_text, sound_button)
    draw_text(window, exit_text, exit_button)


def draw_game_elements(window, bges, pipes, coins, player, frame, sy):
    """
    Отображает основные элементы игры: фон, трубы, монеты и игрока.

    :param window: объект окна Pygame для отображения
    :param bges: список фоновых изображений
    :param pipes: список труб
    :param coins: список монет
    :param player: объект игрока (прямоугольник)
    :param frame: текущий кадр анимации игрока
    :param sy: скорость игрока для управления углом поворота
    """

    # Отрисовка фона
    for bg in bges:
        window.blit(imgBG, bg)  # Отображаем фоны

    # Отрисовка труб
    for pipe in pipes:
        if not pipe.y:  # Верхняя труба
            rect = imgPT.get_rect(bottomleft=pipe.bottomleft)
            window.blit(imgPT, rect)
        else:  # Нижняя труба
            rect = imgPB.get_rect(topleft=pipe.topleft)
            window.blit(imgPB, rect)

    # Отрисовка монет
    for coin in coins:
        window.blit(imgCoin, coin)  # Отображаем монеты

    # Отрисовка игрока с анимацией и поворотом
    image = imgCat.subsurface(68 * int(frame), 0, 68, 48)
    image = pygame.transform.rotate(image, -sy * 2)
    window.blit(image, player)


def draw_score_and_lives(window, scores, lives):
    """
    Отображает текущие очки и количество жизней игрока.

    :param window: объект окна Pygame для отображения
    :param scores: текущий счет игрока
    :param lives: оставшееся количество жизней
    """
    text_scores = font1.render('Очки: ' + str(scores), 1, 'black')
    window.blit(text_scores, (10, 10))  # Отображение очков в левом верхнем углу

    text_lives = font1.render('Жизни: ' + str(lives), 1, 'black')
    window.blit(text_lives, (10, 45))  # Отображение жизней чуть ниже очков


def draw_pause_screen():
    """
    Отображает экран паузы с текстом и затемнением фона.
    """

    # Создаем полупрозрачный черный фон
    pause_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pause_overlay.fill((0, 0, 0, 150))  # Прозрачный черный фон
    window.blit(pause_overlay, (0, 0))

    # Текст на экране паузы
    pause_text = font2.render('Пауза', True, 'white')
    resume_text = font1.render('Нажмите ПРОБЕЛ для продолжения', True, 'white')

    # Центрируем текст на экране
    window.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 3))
    window.blit(resume_text, (WIDTH // 2 - resume_text.get_width() // 2, HEIGHT // 2))


def update_player_position():
    """
    Обновляет положение игрока, включая его вертикальное перемещение и инерцию.
    """
    global py, sy, ay
    if click:
        ay = -2  # Устанавливаем ускорение вверх при клике
    else:
        ay = 0  # Без клика ускорение отсутствует

    py += sy  # Обновляем вертикальное положение игрока
    sy = (sy + ay + 1) * 0.95  # Обновляем скорость с учетом инерции
    player.y = py  # Применяем новое положение игрока


def update_pipes_and_coins():
    """
    Обновляет положение труб и монет. Добавляет новые трубы и монеты в зависимости от состояния игры.
    """
    global pipeGatePos, pipes, coins

    # Добавление новых труб, если последняя труба ушла за определенный предел
    if not len(pipes) or pipes[len(pipes) - 1].x < WIDTH - 200:
        # Создание верхней и нижней трубы
        pipes.append(pygame.Rect(WIDTH, 0, 52, pipeGatePos - pipeGateSize // 2))
        pipes.append(
            pygame.Rect(WIDTH, pipeGatePos + pipeGateSize // 2, 52, HEIGHT - pipeGatePos + pipeGateSize // 2)
        )

        # Смещение центрального прохода для труб
        pipeGatePos += randint(-100, 100)
        pipeGatePos = max(pipeGateSize, min(pipeGatePos, HEIGHT - pipeGateSize))

        # Генерация монет с вероятностью 25%
        if randint(0, 3) == 0:
            coin_x = pipes[-1].x + pipes[-1].width + 10
            coin_y = randint(pipeGatePos - pipeGateSize // 2 + 10, pipeGatePos + pipeGateSize // 2 - 10)
            coins.append(pygame.Rect(coin_x, coin_y, 32, 32))


def check_collisions():
    """
    Проверяет столкновения игрока с трубами и границами экрана. Обновляет очки и состояние игры.
    """
    global state, pipes, scores, pipesScores, pipeSpeed

    # Проверка на выход игрока за границы экрана
    if player.top < 0 or player.bottom > HEIGHT:
        state = 'fall'

    # Проверка столкновения игрока с трубой
    for pipe in pipes:
        if player.colliderect(pipe) or player.top < 0 or player.bottom > HEIGHT:
            state = 'fall'

        # Увеличение очков, если игрок прошел трубу
        if pipe.right < player.left and pipe not in pipesScores:
            pipesScores.append(pipe)
            scores += 5
            pipeSpeed = min(3 + scores // 100, 8)


def draw_game_over_screen(window, scores, click, timer):
    """
    Отображает экран окончания игры с информацией об очках и предложением перезапуска.

    :param window: объект окна Pygame для отображения
    :param scores: итоговый счет игрока
    :param click: состояние клика для перезапуска
    :param timer: таймер для предотвращения мгновенного перезапуска
    """
    # Черный фон
    window.fill((0, 0, 0))

    # Текст завершения игры
    game_over_text = font2.render('Игра окончена', True, 'red')
    score_text = font1.render(f'Ваш результат: {scores}', True, 'white')
    restart_text = font1.render('Нажмите ПРОБЕЛ для перезапуска', True, 'white')

    # Располагаем текст в центре экрана
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    window.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 1.5))

    # Перезапуск игры при нажатии ПРОБЕЛ
    if click and not timer:
        reset_game()


def draw_background(window, bges, imgBG):
    """
    Отображает фоновое изображение.

    :param window: объект окна Pygame для отображения
    :param bges: список координат для фоновых изображений
    :param imgBG: изображение фона
    """
    for bg in bges:
        window.blit(imgBG, bg)  # Отображаем фоны


def draw_pipes(window, pipes, imgPT, imgPB):
    """
    Отображает трубы на экране.

    :param window: объект окна Pygame для отображения
    :param pipes: список труб
    :param imgPT: изображение верхней трубы
    :param imgPB: изображение нижней трубы
    """
    for pipe in pipes:
        if not pipe.y:  # Верхняя труба
            rect = imgPT.get_rect(bottomleft=pipe.bottomleft)
            window.blit(imgPT, rect)
        else:  # Нижняя труба
            rect = imgPB.get_rect(topleft=pipe.topleft)
            window.blit(imgPB, rect)


def draw_coins(window, coins, imgCoin):
    """
    Отображает монеты на экране.

    :param window: объект окна Pygame для отображения
    :param coins: список монет
    :param imgCoin: изображение монеты
    """
    for coin in coins:
        window.blit(imgCoin, coin)


def draw_player(window, player, imgCat, frame, sy):
    """
    Отображает игрока с анимацией и вращением.

    :param window: объект окна Pygame для отображения
    :param player: объект игрока (прямоугольник)
    :param imgCat: изображение спрайтов игрока
    :param frame: текущий кадр анимации
    :param sy: вертикальная скорость для управления углом вращения
    """
    image = imgCat.subsurface(68 * int(frame), 0, 68, 48)  # Выбираем кадр анимации
    image = pygame.transform.rotate(image, -sy * 2)  # Поворачиваем в зависимости от скорости
    window.blit(image, player)


def draw_menu_and_exit(window):
    """
    Отображает текст меню и выхода из игры.

    :param window: объект окна Pygame для отображения
    """
    text = font1.render('Меню', 1, 'black')
    window.blit(text, (WIDTH - 80, 10))

    text = font1.render('Выход из игры', 1, 'black')
    window.blit(text, (WIDTH - 200, HEIGHT - 30))


def generate_coins(pipes, pipeGatePos, pipeGateSize, coins, imgCoin):
    """
    Генерирует монеты рядом с трубами с определенной вероятностью.

    :param pipes: список труб
    :param pipeGatePos: вертикальная позиция центрального прохода
    :param pipeGateSize: размер прохода между трубами
    :param coins: список монет
    :param imgCoin: изображение монеты
    """
    for pipe in pipes:
        if pipe.bottom == pipeGatePos + pipeGateSize // 2:  # Проверка нижней трубы
            if randint(0, 3) == 0:
                coin_x = pipe.x + pipe.width + 10
                coin_y = randint(pipeGatePos - pipeGateSize // 2 + 10, pipeGatePos + pipeGateSize // 2 - 10)
                coin_rect = pygame.Rect(coin_x, coin_y, imgCoin.get_width(), imgCoin.get_height())
                coins.append(coin_rect)


def main_loop():
    """
    Главная игровая петля, которая обрабатывает события, обновляет состояние игры и отрисовывает объекты.
    """
    global play, timer, frame, paused, click, py, sy, ay, state, pipeGatePos, scores, menu_text_rect
    global pipes, coins, pipesScores, pipeSpeed, lives, fullscreen, window, screen_button_text, exit_text_rect
    global music_volume, sound_volume, player, start_button, screen_button, music_button, sound_button, exit_button

    play = True  # Игра активна
    while play:
        handle_events()  # Обработка всех событий (клики, нажатия клавиш)

        press = pygame.mouse.get_pressed()  # Проверка нажатий кнопок мыши
        keys = pygame.key.get_pressed()  # Проверка нажатий клавиш на клавиатуре
        click = press[0] or keys[pygame.K_SPACE]  # Состояние нажатой кнопки мыши или пробела

        if timer:
            timer -= 1  # Уменьшаем таймер, если он активен

        frame = (frame + 0.2) % 4  # Анимация (переключение кадров)

        if not paused:
            update_background()  # Обновление фона
            update_pipes()  # Обновление труб
            update_coins()  # Обновление монет

        # Меню игры
        if state == 'menu':
            window.fill((135, 206, 250))  # Заливаем экран цветом
            title = font2.render('Fly Cat', True, 'white')  # Заголовок игры
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 6))  # Увеличиваем отступ сверху

            mouse_pos = pygame.mouse.get_pos()  # Получаем позицию мыши
            draw_menu_buttons(window, mouse_pos)  # Отрисовка кнопок меню

        # Переход в игру
        if state == 'start':
            if click and not timer and not len(pipes):
                state = 'play'  # Начало игры
            py += (HEIGHT // 2 - py) * 0.1  # Плавное перемещение игрока в центре экрана
            player.y = py

        # Основной игровой процесс
        elif state == 'play':
            if paused:
                draw_pause_screen()  # Экран паузы
            else:
                update_player_position()  # Обновление позиции игрока
                update_pipes_and_coins()  # Обновление труб и монет
                check_collisions()  # Проверка на столкновения

        # Падение игрока (состояние проигрыша)
        elif state == 'fall':
            if sound_volume > 0:
                sndFall.play()  # Воспроизведение звука падения

            sy, ay = 0, 0  # Обнуляем скорость и ускорение
            pipeGatePos = HEIGHT // 2  # Сброс позиции центрального прохода
            coins.clear()  # Удаляем все монеты
            lives -= 1  # Уменьшаем количество жизней

            # Если жизни остались, начинаем заново
            if lives:
                state = 'start'
                timer = 60  # Таймер ожидания перед перезапуском

            # Если жизни закончились, переходим на экран окончания игры
            else:
                state = 'game over'
                timer = 60  # Таймер ожидания перед перезапуском

        # Экран окончания игры
        if state == 'game over':
            draw_game_over_screen(window, scores, click, timer)

        # Отрисовка игры (фоны, трубы, монеты и игрок)
        if state in ['start', 'play', 'fall']:
            draw_background(window, bges, imgBG)  # Отрисовка фонов
            draw_pipes(window, pipes, imgPT, imgPB)  # Отрисовка труб
            draw_coins(window, coins, imgCoin)  # Отрисовка монет
            draw_player(window, player, imgCat, frame, sy)  # Отрисовка игрока
            draw_score_and_lives(window, scores, lives)  # Отображение очков и жизней
            draw_menu_and_exit(window)  # Отображение кнопок меню и выхода

        # Генерация монет в игре
        if state == 'play':
            generate_coins(pipes, pipeGatePos, pipeGateSize, coins, imgCoin)  # Генерация монет

        pygame.display.update()  # Обновляем экран
        clock.tick(FPS)  # Контроль частоты кадров

    pygame.quit()  # Завершение работы Pygame


if __name__ == "__main__":
    main_loop()  # Запуск главной игровой петли
