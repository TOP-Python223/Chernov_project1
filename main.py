"""Модуль верхнего уровня для учебного проекта."""

from func_io import *
# import func_io
# print_playing_field, merge_turn_field, input_turn

# структура игрового поля
field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# номер текущего игрока (0 - играющий Х, 1 - играющий О)
players = {'curr_player': 0, 'playerХ': {'name': ''}, 'playerO': {'name': ''}}
# field = [[0, 5, 1],[0, 2, 3],[0, 0, 4]]


while True:
    # отображаем игровое поле
    print_playing_field(field, players)
    # запрашиваем ход или командbpу игрока
    turn = input_turn(players)
    # выход при пустом вводе (пока)
    if turn == '':
        break
    # заносим ход во внутреннее представление
    merge_turn_field(int(turn), field)
    players['curr_player'] = (players['curr_player'] + 1) % 2
