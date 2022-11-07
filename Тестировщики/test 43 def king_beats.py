#король под шах ходить не может. поэтому функцию проверки взятия
#можно переделать в функцию проверки хода под шах
# Pos_beat - possible beating - возможные взятия.


def Pos_beat(x, y):
    old = Board[x][y]
    Board[x][y] = '.'
    moves = []
    a = 0
    b = 0
    while a < 8:
        while b < 8:
            if(Board[a][b] == '.'):
                b += 1
            else:
                if abs(Board[a][b].color - self.color) == 1:
                    moves += Board[a][b].Moves()
                b += 1
        a += 1
    if [x, y] not in moves:
        return 1
    else:
        return 0
    Board[x][y] = old

