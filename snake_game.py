# Проект "Змейка"
# Импорты
from random import seed, randint

# Переменные
INPUT_TABLE_SIZE_TEXT = "Введите размер поля: "
INPUT_MOVE_TEXT = "Введите направление (w, a, s или d)"
INPUT_BREAKERS_COUNT_TEXT = "Введите количество препятствий:"
INPUT_APPLES_COUNT_TEXT = "Введите количество яблок:"
MIN_TABLE_SIZE = 2
SIZE_OR_COUNT_ERROR = "Так нельзя!"
TABLE_SYMBOL = ' '
SNAKE_SYMBOL = '※'
APPLE_SYMBOL = 'ò'
BREAKER_SYMBOL = '▩'
WIN_TEXT = "Вы выиграли!"
LOOSE_TEXT = "Вы проиграли("
SNAKE_HEAD_EATING = '◈'
SNAKE_HEAD_UP = '▲'
SNAKE_HEAD_DOWN = '▼'
SNAKE_HEAD_LEFT = '◀'
SNAKE_HEAD_RIGHT = '▶'
win = False
loose = False
snake_head_symbol = SNAKE_HEAD_UP
score = 0
step_count = 0

# Стабилизация рандома
seed(10)

# Генерация поля
print(INPUT_TABLE_SIZE_TEXT, end=' ')
table_size = int(input())
while table_size < MIN_TABLE_SIZE:
    print(SIZE_OR_COUNT_ERROR)
    table_size = int(input())
table = list()
for _ in range(table_size):
    table.append(tuple([TABLE_SYMBOL for _ in range(table_size)]))

# Создание змейки
snake = [(table_size // 2, table_size // 2)]

# Создание списка пустых клеток
free_space = list()
for y in range(table_size):
    for x in range(table_size):
        if (y, x) not in snake:
            free_space.append((y,x))

# Генерация препятствий
print(INPUT_BREAKERS_COUNT_TEXT, end=' ')
breakers_count = int(input())
while breakers_count > table_size ** 2 - 1:
    print(MIN_TABLE_SIZE)
    breakers_count = int(input())
breakers = list()
for _ in range(breakers_count):
    breaker_place = free_space[randint(0, len(free_space) - 1)]
    breakers.append(breaker_place)
    free_space.remove(breaker_place)

# Генерация первого яблока
print(INPUT_APPLES_COUNT_TEXT, end=' ')
apples_count = int(input())
while apples_count > table_size ** 2 - 1 - breakers_count:
    print(SIZE_OR_COUNT_ERROR)
    apples_count = int(input())
apples = list()
for _ in range(apples_count):
    apple_place = free_space[randint(0, len(free_space) - 1)]
    apples.append(apple_place)
    free_space.remove(apple_place)

while not win and not loose:
    # Отрисовка поля
    table_copy = [list(row) for row in table]
    table_copy[snake[0][0]][snake[0][1]] = snake_head_symbol
    for snake_part in snake[1:]:
        table_copy[snake_part[0]][snake_part[1]] = SNAKE_SYMBOL
    for breaker in breakers:
        table_copy[breaker[0]][breaker[1]] = BREAKER_SYMBOL
    for apple in apples:
        table_copy[apple[0]][apple[1]] = APPLE_SYMBOL
    print()
    print(f'Score -- {score}\nStep count -- {step_count}')
    print(' _' + '__' * table_size + ' ')
    for row in table_copy:
        print('|', *row, '|')
    print(' -' + '--' * table_size + ' ')
    print()

    # Ввод следующего шага
    print(INPUT_MOVE_TEXT, end=' ')
    snake_move_letter = input()

    # Передвижение змейки
    snake_head_y, snake_head_x = snake[0]
    if snake_move_letter == 'w':  # Движение вверх
        snake_head_y -= 1
        snake_head_symbol = SNAKE_HEAD_UP
    elif snake_move_letter == 's':  # Движение вниз
        snake_head_y += 1
        snake_head_symbol = SNAKE_HEAD_DOWN
    elif snake_move_letter == 'a':  # Движение влево
        snake_head_x -= 1
        snake_head_symbol = SNAKE_HEAD_LEFT
    elif snake_move_letter == 'd':  # Движение вправо
        snake_head_x += 1
        snake_head_symbol = SNAKE_HEAD_RIGHT

    if snake_head_y < 0:
        snake_head_y = table_size
    elif snake_head_y >= table_size:
        snake_head_y = 0
    if snake_head_x < 0:
        snake_head_x = table_size
    elif snake_head_x >= table_size:
        snake_head_x = 0
    snake.insert(0, (snake_head_y, snake_head_x))

    step_count += 1

    # Коллизии
    if snake[0] in snake[1:] or snake[0] in breakers:
        loose = True
    elif snake[0] in apples:
        snake_head_symbol = SNAKE_HEAD_EATING
        apples.remove(snake[0])
        score += 1

        free_space = list()
        for y in range(table_size):
            for x in range(table_size):
                if (y, x) not in snake and (y, x) not in breakers and (y, x) not in apples:
                    free_space.append((y, x))
        if len(free_space) == 0 and len(apples) == 0:
            win = True
        elif len(free_space) != 0:
            apples.append(free_space[randint(0, len(free_space) - 1)])
    else:
        snake.pop()

if win:
    print(WIN_TEXT)
elif loose:
    print(LOOSE_TEXT)