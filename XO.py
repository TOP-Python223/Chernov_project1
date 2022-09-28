"""Основной модудуль запуска игры."""
#                       Глобальные константы

import game
import g_cont as G

# номер текущего игрока (0 - играющий Х, 1 - играющий О)
g_players = {'curr_player': 0,
             'player': [
                 {'name': '', 'age': 0},
                 {'name': '', 'age': 0}
             ]
             }

# field = [[0, 5, 1],[0, 2, 3],[0, 0, 4]]
g_players['player'][0] = {'name': 'Паша', 'age': 11}
g_players['player'][1] = {'name': 'Сева', 'age': 14}

while True:
    # отображаем игровое поле
    str_field = game.show_field(G.FIELD, g_players)
    print(str_field)
    # запрашиваем ход или команду игрока
    turn = game.input_turn(g_players)
    # выход при пустом вводе (пока)
    if turn == '':
        break
    # заносим ход во внутреннее представление
    game.merge_turn_field(G.FIELD, int(turn))
    if game.check_win(G.FIELD, turn):
        pl_name = g_players['player'][g_players['curr_player']]['name']
        print(f"Celebration! {pl_name}, YRW!!!")
        str_field = game.show_field(G.FIELD, g_players)
        print(str_field)
        break
    g_players['curr_player'] = (g_players['curr_player'] + 1) % 2
