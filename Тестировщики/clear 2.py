def Pos_beat(color, x, y):
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
                if Board[a][b].__str__() != 'k':
                    if Board[a][b].__str__() != 'K':
                        if abs(Board[a][b].color - color) == 1:
                            moves += Board[a][b].Moves()

                    else:
                        if color == 0:
                            king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b], [a - 1, b]
                            moves += king_moves
                else:
                    if color == 1:
                        king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b], [a - 1, b]
                        moves += king_moves
                b += 1
        b = 0
        a += 1
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
                            king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b], [a - 1, b]
                            moves += king_moves
                else:
                    if color == 1:
                        king_moves = [a - 1, b - 1], [a, b - 1], [a + 1, b - 1], [a + 1, b], [a + 1, b + 1], [a, b + 1], [a - 1, b], [a - 1, b]
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
class Pawn(Piece):
    IMG = ('p', 'P')
    def Moves(self):
        moves = []
        if self.color == 1:
            if self.x - 1 > 0 and Board[self.x - 1][self.y] == '.':
                moves.append([self.x - 1, self.y])
                if self.x == 6 and Board[self.x - 2][self.y] == '.':
                    moves.append([self.x - 2, self.y])
            if self.x - 1 >= 0 and self.y - 1 >= 0 and Board[self.x - 1][self.y - 1] != '.':
                if Board[self.x - 1][self.y - 1].color == 0:
                    moves.append([self.x - 1, self.y - 1])
            if self.x - 1 >= 0 and self.y + 1 <= 7 and Board[self.x - 1][self.y + 1] != '.':
                if Board[self.x - 1][self.y + 1].color == 0:
                    moves.append([self.x - 1, self.y + 1])
        if self.color == 0:
            if self.x + 1 < 7 and Board[self.x + 1][self.y] == '.':
                moves.append([self.x + 1, self.y])
                if self.x == 1 and Board[self.x + 2][self.y] == '.':
                    moves.append([self.x + 2, self.y]) 
            if self.x + 1 <= 7 and self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] != '.':
                if Board[self.x + 1][self.y + 1].color == 1:
                    moves.append([self.x + 1, self.y + 1])   
            if self.x + 1 <= 7 and self.y - 1 >= 0 and Board[self.x + 1][self.y - 1] != '.':
                if Board[self.x + 1][self.y - 1].color == 1:
                    moves.append([self.x + 1, self.y - 1])
        return moves
class Knight(Piece):
    IMG = ('n', 'N')
    def Take_Move(color, x, y):
        lst = []
        if 0 <= x <= 7 and 0 <= y <= 7:
            if Board[x][y] == '.':
                lst.append([x, y])
            else:
                if abs(color - Board[x][y].color) == 1:
                    lst.append([x, y])
        return lst
    def Moves(self):
        moves = []
        moves += Knight.Take_Move(self.color, self.x - 1, self.y - 2)
        moves += Knight.Take_Move(self.color, self.x - 2, self.y - 1)
        moves += Knight.Take_Move(self.color, self.x - 2, self.y + 1)
        moves += Knight.Take_Move(self.color, self.x - 1, self.y + 2)
        moves += Knight.Take_Move(self.color, self.x + 1, self.y + 2)                
        moves += Knight.Take_Move(self.color, self.x + 2, self.y + 1) 
        moves += Knight.Take_Move(self.color, self.x + 2, self.y - 1)
        moves += Knight.Take_Move(self.color, self.x + 1, self.y - 2) 
        return moves
class Bishop(Piece):
    IMG = ('b', 'B')
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
        moves += Bishop.Take_Moves(self.color, self.x, self.y, 1, 1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, 1, -1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, -1, 1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, -1, -1)        
        return moves
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
class Queen(Piece):
    IMG = ('q', 'Q')
    def Moves(self):
        moves = []
        moves += Rook(self.color, self.x, self.y).Moves()
        moves += Bishop(self.color, self.x, self.y).Moves()
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
    def Moves(self):
        moves = []
        moves += King.Take_Move(self.color, self.x - 1, self.y - 1) 
        moves += King.Take_Move(self.color, self.x, self.y - 1)
        moves += King.Take_Move(self.color, self.x + 1, self.y - 1)   
        moves += King.Take_Move(self.color, self.x - 1, self.y)   
        moves += King.Take_Move(self.color, self.x + 1, self.y)
        moves += King.Take_Move(self.color, self.x, self.y - 1)                    
        moves += King.Take_Move(self.color, self.x, self.y + 1)                   
        moves += King.Take_Move(self.color, self.x + 1, self.y + 1) 
Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
Board[7][4] = King(1, 7, 4)
Board[6][0] = Pawn(1, 6, 0)
Board[6][1] = Pawn(1, 6, 1)
Board[6][2] = Pawn(1, 6, 2)
Board[6][3] = Pawn(1, 6, 3)
Board[6][4] = Pawn(1, 6, 4)
Board[6][5] = Pawn(1, 6, 5)
Board[6][6] = Pawn(1, 6, 6)
Board[6][7] = Pawn(1, 6, 7)
Board[7][1] = Knight(1, 7, 1)
Board[7][6] = Knight(1, 7, 6)
Board[7][2] = Bishop(1, 7, 2)
Board[7][5] = Bishop(1, 7, 5)
Board[7][0] = Rook(1, 7, 0)
Board[7][7] = Rook(1, 7, 7)
Board[7][3] = Queen(1, 7, 3)
Board[0][4] = King(0, 0, 4)
Board[1][0] = Pawn(0, 1, 0)
Board[1][1] = Pawn(0, 1, 1)
Board[1][2] = Pawn(0, 1, 2)
Board[1][3] = Pawn(0, 1, 3)
Board[1][4] = Pawn(0, 1, 4)
Board[1][5] = Pawn(0, 1, 5)
Board[1][6] = Pawn(0, 1, 6)
Board[1][7] = Pawn(0, 1, 7)
Board[0][1] = Knight(0, 0, 1)
Board[0][6] = Knight(0, 0, 6)
Board[0][2] = Bishop(0, 0, 2)
Board[0][5] = Bishop(0, 0, 5)
Board[0][0] = Rook(0, 0, 0)
Board[0][7] = Rook(0, 0, 7)
Board[0][3] = Queen(0, 0, 3)
Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"

print(Print_Board)
print(Knight(1, 7, 1).Moves())
