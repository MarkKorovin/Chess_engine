FEN = ''
def Check_moves(color):
    moves = []
    a = 0
    b = 0
    while a < 8:
        while b < 8:
            if Board[a][b] != '.':
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
def Color_moves(color):
    moves = []
    lst = []
    oxt = []
    a = 0
    b = 0
    while a < 8:
        while b < 8:
            if Board[a][b] != '.':
                if Board[a][b].color == color:
                    if Board[a][b].Moves() != []:
                        oxt = [a, b]
                        lst = Board[a][b].Moves()
                        for i in range(len(lst)):
                            oxt += (lst[i][0], lst[i][1])
                        moves.append(oxt)
                        oxt = []
            b += 1
        b = 0
        a += 1
    return moves

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
def Check(color):
    a = 0
    b = 0
    king_coord = []
    CHECK = 0
    while a < 8:
        while b < 8:
            if(Board[a][b] != '.'):
                if Board[a][b].__str__() == chr(ord('K') + 32 * (1 - color)):
                    king_coord = [a, b]
                    break
            b += 1
        b = 0
        a += 1
        
    mas = []
    j = 0
    k = abs(color - 1)
    moves = Color_moves(k)
    for i in range(len(moves)):
        while j < len(moves[i]):
            mas = [moves[i][j], moves[i][j + 1]]
            if mas == king_coord:
                CHECK = 1
                ATTACKER_POS = [moves[i][0], moves[i][1]]
                break
            j += 2
    if CHECK == 1:
        return ATTACKER_POS
    else:
        return 0

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
        cells = [1, -1]
        a = (-self.color)*2 + 1
        if 0 < self.x < 7 and Board[self.x + a][self.y] == '.':
            moves.append([self.x + a, self.y])
            if (self.color == 0 and self.x == 1) or (self.color == 1 and self.x == 6) and Board[self.x + a*2][self.y] == '.':
                moves.append([self.x + a*2, self.y])
        for i in range(len(cells)):
            if 0 < self.x + a < 7 and 0 < self.y + cells[i] < 7:
                if Board[self.x + a][self.y + cells[i]] != '.':
                    if abs(self.color - Board[self.x + a][self.y + cells[i]].color) == 1:
                        moves.append([self.x + a, self.y + cells[i]])
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
        cells = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
        for i in range(len(cells)):
            moves += Knight.Take_Move(self.color, (self.x + cells[i][0]), (self.y + cells[i][1]))
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
        cells = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for i in range(len(cells)):
            moves += Bishop.Take_Moves(self.color, self.x, self.y, cells[i][0], cells[i][1])        
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
        cells = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(cells)):
            moves += Rook.Take_Moves(self.color, self.x, self.y, cells[i][0], cells[i][1])
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
        return lst
    def Moves(self):
        king_cells = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
        moves = []
        for i in range(len(king_cells)):
            moves += King.Take_Move(self.color, self.x + king_cells[i][0], self.y + king_cells[i][1])
        return moves

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']

def FEN_take():
    FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    i = 0
    x = 0
    y = 0
    while i < len(FEN):
        if 49 <= ord(FEN[i]) <= 56:
             y += (ord(FEN[i]) - ord('0'))
        if FEN[i] == 'r':
            Board[x][y] = Rook(0, x, y)
        if FEN[i] == 'R':
            Board[x][y] = Rook(1, x, y)
        if FEN[i] == 'k':
            Board[x][y] = King(0, x, y)
        if FEN[i] == 'K':
            Board[x][y] = King(1, x, y)
        if FEN[i] == 'n':
            Board[x][y] = Knight(0, x, y)
        if FEN[i] == 'N':
            Board[x][y] = Knight(1, x, y)
        if FEN[i] == 'p':
            Board[x][y] = Pawn(0, x, y)
        if FEN[i] == 'P':
            Board[x][y] = Pawn(1, x, y)
        if FEN[i] == 'q':
            Board[x][y] = Queen(0, x, y)
        if FEN[i] == 'Q':
            Board[x][y] = Queen(1, x, y)
        if FEN[i] == 'b':
            Board[x][y] = Bishop(0, x, y)
        if FEN[i] == 'B':
            Board[x][y] = Bishop(1, x, y)
        if FEN[i] == '/':
            x += 1
            y = 0
        i += 1
        
def Print_Board():
    FEN_take()
    Print_Board = ''
    for y in range(8):
        Print_Board += ''.join(map(str, Board[y])) + "\n"
    return Print_Board
print(Print_Board())

