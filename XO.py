"""Основной модудуль запуска игры."""
#                       Глобальные константы

import game
import g_consts as G

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
    # проверяем на победу
    if game.check_win(G.FIELD, turn):
        pl_name = g_players['player'][g_players['curr_player']]['name']
        print(f"Celebration! {pl_name}, YRW!!!")
    g_players['curr_player'] = (g_players['curr_player'] + 1) % 2
