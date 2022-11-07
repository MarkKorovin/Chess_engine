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
    def Moves(self):
        moves = []
        if (self.color == 'White' and Board[self.x-1][self.y] == '.'):
            moves.append([self.x-1, self.y])
        return moves
            


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     

Board[7][4] = King('White', 7, 4)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)
print(King('White', 7, 4).Moves())
