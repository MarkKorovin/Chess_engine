class King(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        if (self.color == 'White'):
            return 'K'
        else:
            if (self.color == 'Black'):
                return 'k'

            


class Board():
    Board = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     
    Board[7][4] = King('White', 7, 4)

    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.Board[y])) + "\n"
        return res


print(Board())

