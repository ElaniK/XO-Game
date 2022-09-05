desk = list(range(1, 10))

wins_combo = [(1, 2, 3),
              (4, 5, 6),
              (7, 8, 9),
              (1, 4, 7),
              (2, 5, 8),
              (3, 6, 9),
              (1, 5, 9),
              (3, 5, 7)]


def draw_desk():
    print("-------------")
    for i in range(3):
        print("|", desk[0 + i * 3], '|', desk[1 + i * 3], '|', desk[2 + i * 3], '|')
    print("-------------")



def gamer_step(player_token):
    while True:
        value = input('Сделайте ход' + ' ' + player_token + ' ')
        if not (value in '123456789'):
            print('Ошибка, выберите свободную клетку')
            continue
        value = int(value)
        if str(desk[value - 1]) in 'xo':
            print('Клетка уже занята')
            continue
        desk[value - 1] = player_token
        break


def ckeck_win():
    for each in wins_combo:
        if (desk[each[0] - 1]) == (desk[each[1] - 1]) == (desk[each[2] - 1]):
            return desk[each[1] - 1]
    else:
            return False


def main():
    counter = 0
    while True:
        draw_desk()
        if counter % 2 == 0:
            gamer_step('x')
        else:
            gamer_step('0')
        if counter > 3:
            winner = ckeck_win()
            if winner:
                draw_desk()
                print(winner, 'Победа!')
                break
        counter += 1
        if counter > 8:
            draw_desk()
            print('Ничья!')

main()
