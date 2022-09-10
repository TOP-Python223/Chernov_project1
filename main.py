"""Модуль верхнего уровня для учебного проекта."""

import func_io
# import func_io
# print_playing_field, merge_turn_field, input_turn


# структура игрового поля
field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
# номер текущего игрока (0 - играющий Х, 1 - играющий О)
players = {'curr_player': 0,
           'player': [
               {'name': '', 'age': 0},
               {'name': '','age': 0}
            ]
           }
# field = [[0, 5, 1],[0, 2, 3],[0, 0, 4]]
players['player'][0] = {'name': 'Паша', 'age': 11}
players['player'][1] = {'name': 'Сева', 'age': 14}


while True:
    # отображаем игровое поле
    func_io.print_playing_field(field, players)

    # запрашиваем ход или команду игрока
    turn = func_io.input_turn(players)
    # выход при пустом вводе (пока)
    if turn == '':
        break
    # заносим ход во внутреннее представление
    func_io.merge_turn_field(int(turn), field)
    players['curr_player'] = (players['curr_player'] + 1) % 2
