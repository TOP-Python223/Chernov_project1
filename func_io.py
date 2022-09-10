"""Модуль с функциями ввода/вывода для игры крестики-нолики."""
# количество клеток игрового поля по горизонтали
field_size_x: int = 3
# размер окна терминала по гризонтали в символах
term_size_x: int = 80
# количество клеток игрового поля по вертикали
field_size_y: int = 3
# размер игрового поля по горизонтали в символах
field_width = (field_size_x * 2 - 1)

# ввод команды игрока и её обработка
# параметры:
#   player - игрок (0 - играющий Х, 1 - играющий О)
# возвращает словарь структурой:
# {'turn': 1, 'err_code': 0, 'err_mess': ''}
# где:
# turn номер хода при правильном выборе,
# err_code - код ошибки, 0 ошибки нет,
# err_mess - текст ошибки, '' ошибки нет
def input_turn(players):
    res = {'turn': 0, 'err_code': 0, 'err_mess': ''}
    if players['curr_player'] == 1:
        sign_char = 'Х'
    else:
        sign_char = 'О'
    # строка, которую ввел пользователь в запросе хода
    input_string = input(f'Input turn for {sign_char} player>')
    try:
        input_int = int(input_string)
    except:
        input_int = None
    # if field[turn // field_size_x][turn % field_size_x] > 0:
    #     res['err_code'] = -1
    #     res['err_mess'] = f'Клетка с индексом {input_int} уже занята'
    return input_int

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
def print_playing_field(field, players):
    if players['curr_player'] == 0:
        start_char = ''
    else:
        start_char = ' ' * (term_size_x - field_width)
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
        if i < field_size_y - 1:
            print(start_char + '-' * field_width)

