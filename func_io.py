"""Модуль с функциями ввода/вывода для игры крестики-нолики."""
field_size_x: int = 3
term_size_x: int = 80
field_size_y: int = 3
field_width = (field_size_x * 2 - 1)

# ввод команды игрока и её обработка
# параметры:
#   player - игрок (0 - играющий Х, 1 - играющий О)
def input_turn(player):
    pass

# добавление хода в структкру игрового поля
# параметры:
#   turn - номер выбранной клетки
#   field - игровое поле
def merge_turn_field(turn : int, field):
    pass

# отображение игрового поля
#   field - игровое поле
#   player - игрок (0 - играющий Х, 1 - играющий О)
def print_playing_field(field, player):
    pass

