"""Модуль с функциями ввода/вывода для игры крестики-нолики."""
#                       Функции ввода-вывода
# -----------------------------------------------------------------------------

import g_consts as G

def input_turn(p_players):
    """Функция запроса ввода команды или хота игрока."""
    # параметры:
    #   p_player - игроки струкруры, описанной
    # возвращает введенную пользователем строку
    # ИСПОЛЬЗОВАТЬ: приведение к bool
    v_turn = None
    if p_players['curr_player']:
        sign_char = G.MARKS[1]
    else:
        sign_char = G.MARKS[0]
    pl_name = p_players['player'][p_players['curr_player']]['name']
    # ИСПОЛЬЗОВАТЬ: цикл для проверки пользовательского ввода
    while True:
        # строка, которую ввел пользователь в запросе хода
        input_string = input(
            f'Игрок "{pl_name}", играющий за "{sign_char}", введите номер хода>'
        ).strip()
        if input_string.isdecimal():
            v_turn = int(input_string)
            # доп проверки при необходимости
            if (v_turn < 0) or (v_turn > G.FIELD_ROWS * G.FIELD_COLUMNS):
                print('Номер хода должен быть от 0 до ' + (G.FIELD_ROWS * G.FIELD_COLUMNS - 1))
            if G.FIELD[v_turn // G.FIELD_COLUMNS][v_turn % G.FIELD_COLUMNS] > 0:
                print('В это поле уже произведен ход, повторите ввод')
        elif not input_string:
            return ''
        else:
            print('введите номер ячейки поля или пустую строку, если хотите сохранить незавершённую партию и выйти')
        if not(v_turn is None):
            return v_turn

def merge_turn_field(p_field, p_turn: int):
    """функция объединения очередного хода с матицей ходов"""
    # параметры:
    #   p_turn - номер выбранной клетки
    #   p_field - игровое поле
    turn_number: int = max(sum(p_field, [])) + 1
    p_field[p_turn // G.FIELD_COLUMNS][p_turn % G.FIELD_COLUMNS] = turn_number

def show_field(p_field, p_players) -> str:
    """функция возвращает строку игрового поля для отображения"""
    # отображение игрового поля
    #   p_field - игровое поле
    #   p_player - игрок (0 - играющий Х, 1 - играющий О)
    # возврат: строка игрового поля по домашнему заданию # HW_09.04.txt
    result = ''
    if p_players['curr_player']:
        start_char = ' ' * (G.TERM_WIDTH - G.FIELD_WIDTH)
    else:
        start_char = ''
    for r in range(G.FIELD_ROWS):
        result = result + start_char
        for c in range(G.FIELD_COLUMNS):
            finish_char = '' if c == G.FIELD_COLUMNS - 1 else '|'
            if p_field[r][c] == 0:
                print_char = ' '
            elif p_field[r][c] % 2:
                print_char = G.MARKS[0]
            else:
                print_char = G.MARKS[1]
            # print(print_char, end=finish_char)
            result = result + print_char.center(G.CELL_WIDTH) + finish_char
        result = result + '\n'
        if r < G.FIELD_ROWS - 1:
            # print(start_char + '-'*G_FIELD_WIDTH)
            #
            result = result + start_char + '—' * (G.FIELD_WIDTH) + '\n'
    return result


def check_win(p_field, p_turn: int) -> bool:
    """функция проверки выигрышного хода"""
    #    вход: объекты с данными о сделанных ходах
    #    p_field - игровое поле
    #    p_turn - 0 ход первого игрока, 1 - второго
    #    возврат: bool - есть ли на поле победная комбинация (столбец/строка/диагональ целиком заполненная одним символом)
    #    stdout: None
    # номер строки хода
    v_row_num = p_turn // G.FIELD_COLUMNS
    # номер колонки хода
    v_col_num = p_turn % G.FIELD_COLUMNS
    # 1 - ход игрока 1, 0 - ход игрока 2
    v_odd = p_field[v_row_num][v_col_num] % 2
    def check_row() -> bool:
        """по горионтали"""
        #    вход: None
        #    возврат: bool - есть ли на горизонтали победная комбинация
        # количество четных или нечетных должно быть равно G.COUNT_WIN
        v_count = 0
        # print(f'{p_turn=}  {v_odd=}')
        for c in p_field[v_row_num]:
            # print(f'{c=}')
            v_count += (c % 2 == v_odd) and (c != 0)
        # print(f'{v_count} | {G.COUNT_WIN}')
        return v_count == G.COUNT_WIN

    def check_column() -> bool:
        """по вертикали"""
        #    вход: None
        #    возврат: bool - есть ли на вертикале победная комбинация
        # вертикаль вычисляется как деление нацело хода на количество столбцов
        # количество четных или нечетных должно быть равно G.COUNT_WIN по условиям задания
        v_count = 0
        for v_row in p_field:
            v_count += (v_row[v_col_num] % 2 == v_odd) and (v_row[v_col_num] != 0)
        return v_count == G.COUNT_WIN

    def check_cross_0() -> bool:
        """по диагонали право-верх:лево-низ"""
        #    вход: None
        #    возврат: bool - есть ли на диагонали победная комбинация
        v_count = 1
        i_loop = 1
        while True:
            i_row_num = v_row_num - i_loop
            i_col_num = v_col_num + i_loop
            if (i_row_num >= 0) and (i_col_num < G.FIELD_COLUMNS):
                v_count += (p_field[i_row_num][i_col_num] % 2 == v_odd) and (p_field[i_row_num][i_col_num] != 0)
            i_row_num = v_row_num + i_loop
            i_col_num = v_col_num - i_loop
            if (i_row_num < G.FIELD_ROWS) and (i_col_num >= 0):
                v_count += (p_field[i_row_num][i_col_num] % 2 == v_odd) and (p_field[i_row_num][i_col_num] != 0)
            i_loop += 1
            if (v_row_num - i_loop < 0) and \
                (v_col_num - i_loop < 0) and \
                (v_row_num + i_loop >= G.FIELD_ROWS) and \
                (v_col_num + i_loop >= G.FIELD_COLUMNS):
                break
        return v_count == G.COUNT_WIN
    def check_cross_1() -> bool:
        """по диагонали лево-верх:право-низ"""
        #    вход: None
        #    возврат: bool - есть ли на обратной диагонали победная комбинация
        v_count = 1
        i_loop = 1
        while True:
            i_row_num = v_row_num - i_loop
            i_col_num = v_col_num - i_loop
            if (i_row_num >= 0) and (i_col_num >= 0):
                v_count += (p_field[i_row_num][i_col_num] % 2 == v_odd) and (p_field[i_row_num][i_col_num] != 0)
            i_row_num = v_row_num + i_loop
            i_col_num = v_col_num + i_loop
            if (i_row_num < G.FIELD_ROWS) and (i_col_num < G.FIELD_COLUMNS):
                v_count += (p_field[i_row_num][i_col_num] % 2 == v_odd) and (p_field[i_row_num][i_col_num] != 0)

            i_loop += 1
            if (v_row_num - i_loop < 0) and \
                (v_col_num - i_loop < 0) and \
                (v_row_num + i_loop >= G.FIELD_ROWS) and \
                (v_col_num + i_loop >= G.FIELD_COLUMNS):
                break
        return v_count == G.COUNT_WIN

    # результат функции check_win
    return check_row() or check_column() or check_cross_0() or check_cross_1()


# if __name__ == "__main__":
#     pass
