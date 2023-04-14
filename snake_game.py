# Проект "Змейка"
# Импорты
from random import seed, randint

# Переменные меню
menu_move = """8. Вверх
2. Вниз
6. Вправо
4. Влево"""

# Стабилизация рандома
seed(10)

# Генерация поля
# 1. Узнаем размер поля
print("Введите размер поля:")
table_size = int(input())
# 2. Создаём двумерный список
table = list()  # Пустой список
for _ in range(table_size):  # Цикл сработает table_size раз
    row = ['.' for _ in range(table_size)]  # Создаём список
    table.append(row)  # Добавляем его в основной список

# Создание змейки
# 1. Вычисление стартовой позиции змейки
snake_start_y = table_size // 2

snake_start_x = table_size // 2
# 2. Само создание змейки
snake = [[snake_start_y, snake_start_x]]

# Генерация яблока
# 1. Генерируем координаты
apple_y = randint(0, table_size - 1)
apple_x = randint(0, table_size - 1)
# 2. Добавление яблока на карту
table[apple_y][apple_x] = '+'

# Вывод поля на экран
# 1. Создание копии поля
table_copy = [row.copy() for row in table]
# 2. Добавляем змейку на копию поля
for snake_part in snake:
    table_copy[snake_part[0]][snake_part[1]] = '*'
# 3. Вывод поля на экран
for row in table_copy:
    print(*row)

# Основной игровой цикл
# Ввод первого шага
print(menu_move)
snake_move_num = int(input())
# Запуск игрового цикла
while snake_move_num != 0:
    # Движение змейки
    # 1. Добавляем в начало змейки новый кусочек
    if snake_move_num == 8:  # Движение вверх
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif snake_move_num == 2:  # Движение вниз
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif snake_move_num == 4:  # Движение влево
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    elif snake_move_num == 6:  # Движение вправо
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
    else:
        print("Нет такого направления!")
    # 2. Если новый кусочек находится на еде
    if table[snake[0][0]][snake[0][1]] == '+':
        # Удаляем старую еду
        table[snake[0][0]][snake[0][1]] = '.'
        # Добавляем новую еду
        apple_y = randint(0, table_size - 1)
        apple_x = randint(0, table_size - 1)
        table[apple_y][apple_x] = '+'
    else:
        # Если еды нет -- удаляем хвост змейки
        snake.pop()
    # Вывод поля
    table_copy = [row.copy() for row in table]
    for snake_part in snake:
        table_copy[snake_part[0]][snake_part[1]] = '*'
    for row in table_copy:
        print(*row)
    # Ввод последующих шагов
    print(menu_move)
    snake_move_num = int(input())
