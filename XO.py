"""Основной модудуль запуска игры."""
import game
import g_consts as G

# для тестирования
G.PLAYERS['player'][0] = {'name': 'Паша', 'age': 11}
G.PLAYERS['player'][1] = {'name': 'Сева', 'age': 14}

while True:
    # отображаем игровое поле
    str_field = game.show_field()
    print(str_field)
    # запрашиваем ход или команду игрока
    turn = game.input_turn()
    # выход при пустом вводе (пока)
    if turn == '':
        break
    # заносим ход во внутреннее представление
    game.merge_turn_field(int(turn))
    # проверяем на победу
    if game.check_win(turn):
        pl_name = G.PLAYERS['player'][G.PLAYERS['curr_player']]['name']
        print(f"Celebration! {pl_name}, YRW!!!")
    G.PLAYERS['curr_player'] = (G.PLAYERS['curr_player'] + 1) % 2
