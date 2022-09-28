"""Модуль с функциями ввода/вывода для игры крестики-нолики."""
#                       Функции ввода-вывода
# -----------------------------------------------------------------------------

# from contstants import G_CELL_WIDTH, G_FIELD_COLUMNS, G_FIELD_ROWS, G_FIELD_WIDTH, G_TERM_WIDTH, G_MARKS
import g_cont as G

def input_turn(p_players):
    """Функция запроса ввода команды или хота игрока."""
    # параметры:
    #   p_player - игроки струкруры, описанной
    # возвращает введенную пользователем строку
    # ИСПОЛЬЗОВАТЬ: приведение к bool
    if p_players['curr_player']:
        sign_char = G.MARKS[1]
    else:
        sign_char = G.MARKS[0]
    pl_name = p_players['player'][p_players['curr_player']]['name']
    # ИСПОЛЬЗОВАТЬ: цикл для проверки пользовательского ввода
    while True:
        # строка, которую ввел пользователь в запросе хода
        input_string = input(
            f'Input turn "{pl_name}" for {sign_char} player>'
        ).strip()
        if input_string.isdecimal():
            # доп проверки при необходимости
            return int(input_string)
        elif not input_string:
            return ''
        else:
            print('введите номер ячейки поля или пустую строку если хотите сохранить незавершённую партию и выйти')

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
    def check_row() -> bool:
        """по горионтали"""
        #    вход: None
        #    возврат: bool - есть ли на горизонтали победная комбинация
        # горизонталь вычисляется как деление нацело хода на количество столбцов
        # количество четных или нечетных должно быть равно 3 по условиям задания
        count = 0
        for c in range(G.FIELD_COLUMNS):
            count += (p_field[p_turn // G.FIELD_COLUMNS][c] % 2 == p_turn % 2) \
                     and (p_field[p_turn // G.FIELD_COLUMNS][c] != 0)
        return count == G.COUNT_WIN

    def check_column() -> bool:
        """по вертикали"""
        #    вход: None
        #    возврат: bool - есть ли на вертикале победная комбинация
        # вертикаль вычисляется как деление нацело хода на количество столбцов
        # количество четных или нечетных должно быть равно 3 по условиям задания
        count = 0
        for v_row in p_field:
            count += (v_row[p_turn % G.FIELD_COLUMNS] % 2 == p_turn % 2) \
                     and (v_row[p_turn % G.FIELD_COLUMNS] != 0)
        return count == G.COUNT_WIN

    def check_cross() -> bool:
        """по диагонале"""
        #    вход: None
        #    возврат: bool - есть ли на  победная комбинация
        # Проверка текущего хода по диагоналям на выигрыш
        return False

    # результат функции check_win
    return check_row() or check_column() or check_cross()


if __name__ == "__main__":
    pass
