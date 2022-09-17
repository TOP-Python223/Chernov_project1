"""Модуль с функциями ввода/вывода для игры крестики-нолики."""

#                       Глобальные константы
# -----------------------------------------------------------------------------
# количество клеток игрового поля по горизонтали
c_field_columns: int = 3
# количество клеток игрового поля по вертикали
c_field_rows: int = 3
# размер одной ячейки по горизонтали в символах
c_cell_width: int = 3
# размер окна терминала по горизонтали в символах
c_term_width: int = 80
# размер игрового поля по горизонтали в символах
c_field_width = c_field_columns * c_cell_width + c_field_columns - 1
# символы для обозначения ходов на игровом поле
c_marks = ('X', 'O')

#                       Функции ввода-вывода
# -----------------------------------------------------------------------------
# ввод команды игрока и её обработка
# параметры:
#   p_player - игрок (0 - играющий Х, 1 - играющий О)
# возвращает введенную пользователем строку
def input_turn(p_players):
    # ИСПОЛЬЗОВАТЬ: приведение к bool
    if p_players['curr_player']:
        sign_char = c_marks[1]
    else:
        sign_char = c_marks[0]
    pl_name = p_players['player'][p_players['curr_player']]['name']
    # ИСПОЛЬЗОВАТЬ: цикл для проверки пользовательского ввода
    while True:
        # строка, которую ввел пользователь в запросе хода
        input_string = input(
            f'Input turn "{pl_name}" for {sign_char} player>'
        ).strip()
        if input_string.isdecimal():
            # доп проверки при необходимости
            return input_string
        elif not input_string:
            return ''
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
#   p_turn - номер выбранной клетки
#   p_field - игровое поле
def merge_turn_field(p_turn: int, p_field):
    turn_number: int = max(sum(p_field, [])) + 1
    p_field[p_turn // c_field_columns][p_turn % c_field_rows] = turn_number


# отображение игрового поля
#   p_field - игровое поле
#   p_player - игрок (0 - играющий Х, 1 - играющий О)
# возврат: строка игрового поля по домашнему заданию # HW_09.04.txt
def show_field(p_field, p_players) -> str:
    result = ''
    if p_players['curr_player']:
        start_char = ' '*(c_term_width - c_field_width)
    else:
        start_char = ''
    for i in range(c_field_rows):
        result = result + start_char
        for j in range(c_field_columns):
            finish_char = '' if j == c_field_columns - 1 else '|'
            if p_field[i][j] == 0:
                print_char = ' '
            elif p_field[i][j] % 2:
                print_char = c_marks[0]
            else:
                print_char = c_marks[1]
            # print(print_char, end=finish_char)
            result = result + print_char.center(c_cell_width) + finish_char
        result = result + '\n'
        if i < c_field_rows - 1:
            # print(start_char + '-'*c_field_width)
            #
            result = result + start_char + '—' * (c_field_width) + '\n'
    return result


# Проверка выигрышного хода
#    p_field  - игровое поле
#    p_turn   - номер хода
# возврат: bool - есть ли на поле победная комбинация (столбец/строка/диагональ целиком заполненная одним символом)
# stdout: None
def check_win(p_field, p_turn: int) -> bool:
    pass