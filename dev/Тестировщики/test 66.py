def Pos_beat(color, x, y):
    old = Board[x][y]
    Board[x][y] = '.'
    moves = []
    moves += Check_moves(color)
    Board[x][y] = old
    if [x, y] not in moves:
        return 1
    else:
        return 0

def Check_moves(color):
    moves = []
    a = 0
    b = 0
    while a < 8:
        while b < 8:
            if(Board[a][b] == '.'):
                b += 1
            else:
                if Board[a][b].__str__() != 'k':
                    if Board[a][b].__str__() != 'K':
                        if abs(Board[a][b].color - color) == 1:
                            moves += Board[a][b].Moves()
                    else:
                        if color == 0:
                            king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b + 1], [a - 1, b]
                            moves += king_moves
                else:
                    if color == 1:
                        king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b + 1], [a - 1, b]
                        moves += king_moves
                b += 1
        b = 0
        a += 1
    return moves
class Piece(object):
    IMG = None
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    def __str__(self):
        return self.IMG[0 if self.color == 0 else 1] 

class Rook(Piece):
    IMG = ('r', 'R')  
    def Take_Moves(color, x, y, i, j):
        lst = []
        x = x + i
        y = y + j
        while 0 <= x <= 7 and 0 <= y <= 7:
            if Board[x][y] == '.':
                lst.append([x, y])
                x += i
                y += j
            else:
                if(abs(color - Board[x][y].color) == 1):
                    lst.append([x, y])
                break
        return lst
    def Moves(self):
        moves = []
        moves += Rook.Take_Moves(self.color, self.x, self.y, 1, 0)
        moves += Rook.Take_Moves(self.color, self.x, self.y, -1, 0)
        moves += Rook.Take_Moves(self.color, self.x, self.y, 0, 1)
        moves += Rook.Take_Moves(self.color, self.x, self.y, 0, -1)
        return moves 

class King(Piece):
    IMG = ('k', 'K')
    def Take_Move(color, x, y):
        lst =[]
        impos = Check_moves(color)
        if(0 <= x <= 7 and 0 <= y <= 7):
            if(Board[x][y] == '.'):
                if [x, y] not in impos:
                    lst.append([x, y])
            else:
                if(abs(Board[x][y].color - color) == 1):
                    if Pos_beat(color, x, y) == 1:
                        lst.append([x, y])
        return lst
    def Moves(self):
        moves = []
        moves += King.Take_Move(self.color, self.x - 1, self.y - 1) 
        moves += King.Take_Move(self.color, self.x, self.y - 1)
        moves += King.Take_Move(self.color, self.x + 1, self.y - 1)   
        moves += King.Take_Move(self.color, self.x + 1, self.y)   
        moves += King.Take_Move(self.color, self.x + 1, self.y + 1)
        moves += King.Take_Move(self.color, self.x, self.y + 1)                    
        moves += King.Take_Move(self.color, self.x - 1, self.y + 1)                   
        moves += King.Take_Move(self.color, self.x - 1, self.y)
        return moves

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
Board[7][4] = King(1, 7, 4)
Board[2][3] = Rook(0, 2, 3)
Board[5][5] = King(0, 5, 5)
Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"

print(Print_Board)
print(King(1, 7, 4).Moves())

