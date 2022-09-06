"""Модуль с функциями ввода/вывода для игры крестики-нолики."""
field_size_x: int = 3
term_size_x: int = 80
field_size_y: int = 3
field_width = (field_size_x * 2 - 1)

# ввод команды игрока и её обработка
# параметры:
#   player - игрок (0 - играющий Х, 1 - играющий О)
def input_turn(player):
    if player == 1:
        sign_char = 'Х'
    else:
        sign_char = 'О'
    return input(f'Input turn for {sign_char} player>')

# добавление хода в структкру игрового поля
# параметры:
#   turn - номер выбранной клетки
#   field - игровое поле
def merge_turn_field(turn : int, field):
    turn_number: int = max(sum(field, [])) + 1
    field[turn // field_size_x][turn % field_size_x] = turn_number

# отображение игрового поля
#   field - игровое поле
#   player - игрок (0 - играющий Х, 1 - играющий О)
def print_playing_field(field, player):
    if player == 0:
        start_char = ' ' * (term_size_x - field_width)
    else:
        start_char = ''
    for i in range(field_size_y):
        print(start_char, end = '')
        for j in range(field_size_x):
            if j == field_size_x - 1:
                finish_char = ''
            else:
                finish_char = '|'
            if field[i][j] == 0:
                print_char = ' '
            elif field[i][j] % 2 == 1:
                print_char = 'Х'
            else:
                print_char = 'O'
            print(print_char, end = finish_char)
        print()
        if i < field_size_y - 1: print(start_char + '-' * field_width)

