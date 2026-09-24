
# описание функция
def draw_board(game_field):
   print("-" * 13)
   for i in range(3):
      print("|", game_field[0+i*3], "|", game_field[1+i*3], "|", game_field[2+i*3], "|")
      print("-" * 13)

def gamers_name():
    name_1 = str(input ("введите имя игрока 1 "))
    name_2 = str(input ("введите имя игрока 2 "))
    return name_1, name_2

def step_gamer_1(name, game_field):
    flag = 0
    print (f"ход игрока {name}")
    cell = int(input("укажите клетку для хода "))-1
    while flag==0:
        if any([game_field [cell] == 'x', game_field [cell] == 'o' ]):
            print("данная клетка уже занята")
            cell = int(input("укажите клетку для ход "))-1
        else:
            game_field[cell] = 'x'
            flag=1
    return game_field, 'x'
def step_gamer_2(name, game_field):
    flag=0
    print(f"ход игрока {name}")
    cell = int(input("укажите клетку для хода "))-1
    while flag == 0:
        if any([game_field[cell] == 'x', game_field[cell] == 'o']):
            print("данная клетка уже занята")
            cell = int(input("укажите клетку для хода "))-1
        else:
            game_field[cell] = 'o'
            flag = 1
    return game_field, 'o'

def game_end (game_field, symbol):
    counter = 0
    for cell in game_field:
        if cell == 'x'or cell == 'o':
            counter = counter + 1
        if counter == 9:
            return 2
    win_list = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for cell in win_list:
        if game_field[cell[0]]==game_field[cell[1]]==game_field[cell[2]]:
            return 1
    return 0

# основной код
current_board = list(range(1,10))
end_game_flag = 0
name1, name2 = gamers_name()
draw_board(current_board)
while end_game_flag == 0:
    current_board, gamer_symbol = step_gamer_1(name1, current_board)
    end_game_flag = game_end (current_board, gamer_symbol)
    draw_board(current_board)
    if end_game_flag == 1:
        print(f"{name1} победил")
        break
    if end_game_flag == 2:
        print("ничья")
        break
    current_board, gamer_symbol = step_gamer_2(name2, current_board)
    end_game_flag = game_end(current_board, gamer_symbol)
    draw_board(current_board)
    if end_game_flag == 1:
        print(f"{name2} победил")
        break
    if end_game_flag == 2:
        print("ничья")
        break
input("нажмите любую клавишу для выхода из игры")
