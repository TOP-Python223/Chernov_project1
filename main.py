"""Модуль верхнего уровня для учебного проекта."""

from func_io import print_playing_field, merge_turn_field, input_turn

# структура игрового поля
field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# номер текущего игрока (0 - играющий Х, 1 - играющий О)
player = 0
# field = [[0, 5, 1],[0, 2, 3],[0, 0, 4]]


while True:
    player = (player + 1) % 2
    print_playing_field(field, player)
    turn = input_turn(player)
    if turn == '':
        break
    merge_turn_field(int(turn), field)
