def greet():
    print("Правила игры")
    print(" Стиваишь: x или y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()
#show()
#while цикл
#def ask():
#    x,y=map(int,input("           ваш ход:").split())
#    while x<0 or x>2 or y<0 or y>2:
#        x, y = map(int, input("           ваш ход:").split())
#        return x,y
#ask()

def ask():
    while True:
        #        x, y = map(int, input("           ваш ход:").split())
        #        if 0<=x<=2 and 0<=y<=2 :
        #            if field[x][y]==" ":   #если эта точка пуста возвращаем х, у
        #                return x,y
        #            else: print(" Клетка занята! ") #если в точке не пробел, пишем клетка занята и заново спрашиваем
        #        else:
        #            print(" Координаты вне диапазона! ")
        # ask()
        #        if 0>x or x>2 or 0>y or y>2 :
        #            print("Координаты вне диапазона!")
        #            continue
        #
        #        if field[x][y] != " ":
        #            print("Клетка занята! ")
        #            continue
        #        return x, y
        # ask()
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите две координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
#ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break