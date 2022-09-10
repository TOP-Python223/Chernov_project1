"""Модуль с функциями ввода/вывода для игры крестики-нолики."""

# количество клеток игрового поля по горизонтали
field_size_x: int = 3
# размер окна терминала по горизонтали в символах
term_size_x: int = 80
# количество клеток игрового поля по вертикали
field_size_y: int = 3
# размер игрового поля по горизонтали в символах
field_width = (field_size_x * 2 - 1)


# ввод команды игрока и её обработка
# параметры:
#   player - игрок (0 - играющий Х, 1 - играющий О)
# возвращает введенную пользователем строку
def input_turn(players):
    # res = {'turn': 0, 'err_code': 0, 'err_mess': ''}
    # ИСПОЛЬЗОВАТЬ: приведение к bool
    if players['curr_player']:
        sign_char = 'О'
    else:
        sign_char = 'Х'
    pl_name = players['player'][players['curr_player']]['name']
    # ИСПОЛЬЗОВАТЬ: цикл для проверки пользовательского ввода
    while True:
        # строка, которую ввел пользователь в запросе хода
        input_string = input(
            f'Input turn "{pl_name}" for {sign_char} player>'
        ).strip()
        if input_string.isdecimal():
            # доп проверки при необходимости
            return input_string
        else:
            print('введите номер ячейки поля или пустую строку если хотите сохранить незавершённую партию и выйти')
    # try:
    #     input_int = int(input_string)
    # except:
    #     input_int = None
    # # if field[turn // field_size_x][turn % field_size_x] > 0:
    # #     res['err_code'] = -1
    # #     res['err_mess'] = f'Клетка с индексом {input_int} уже занята'
    # return input_int
    # return input_string


# добавление хода в структуру игрового поля
# параметры:
#   turn - номер выбранной клетки
#   field - игровое поле
def merge_turn_field(turn: int, field):
    turn_number: int = max(sum(field, [])) + 1
    field[turn // field_size_x][turn % field_size_x] = turn_number


# отображение игрового поля
#   field - игровое поле
#   player - игрок (0 - играющий Х, 1 - играющий О)
def print_playing_field(field, players):
    if players['curr_player'] == 0:
        start_char = ''
    else:
        start_char = ' '*(term_size_x - field_width)
    for i in range(field_size_y):
        print(start_char, end='')
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
            print(print_char, end=finish_char)
        print()
        if i < field_size_y - 1:
            print(start_char + '-'*field_width)

