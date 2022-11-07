from random import randint
result = '*'
half_move = 1
move_turn = 1
def Color_moves(color):
    moves = []
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
def Check(color):
    CHECK = 0
    for a in range (8):
        for b in range (8):
            if(Board[a][b] != '.'):
                if Board[a][b].__str__() == chr(ord('K') + 32 * (1 - color)):
                    king_coord = [a, b]
                    break 
    moves = Color_moves(abs(color - 1))
    for i in range(len(moves)):
        j = 2
        while j < len(moves[i]):
            mas = [moves[i][j], moves[i][j + 1]]
            if mas == king_coord:
                CHECK = 1
                break
            j += 2
    if CHECK == 1:
        return 1
    else:
        return 0    
def Possible_move(color):
    moves = []
    massiv = Color_moves(color)
    for i in range(len(massiv)):
        j = 2
        while j < (len(massiv[i])):
            move = [massiv[i][0], massiv[i][1], massiv[i][j], massiv[i][j + 1]]
            piece = Board[move[0]][move[1]]
            Board[move[2]][move[3]] = Board[move[0]][move[1]]
            Board[move[0]][move[1]] = '.'
            Board[move[2]][move[3]].x = move[2]
            Board[move[2]][move[3]].y = move[3]
            if Check(color) == 0:
                moves.append(move)
            j += 2
            Board[move[0]][move[1]] = Board[move[2]][move[3]]
            #Board[move[2]][move[3]] = piece
            #Но здесь возникает проблема. Компьютер просто считает эта фигурой противника. То есть нужно чуть более сложное условие.
            Board[move[2]][move[3]] = '.'
            Board[move[0]][move[1]].x = move[0]
            Board[move[0]][move[1]].y = move[1]
            Print_Board()
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
        cells = [1, -1]
        a = (-self.color)*2 + 1
        if 0 < self.x < 7 and Board[self.x + a][self.y] == '.':
            moves.append([self.x + a, self.y])
            if ((self.color == 0 and self.x == 1) or (self.color == 1 and self.x == 6)) and Board[self.x + a*2][self.y] == '.':
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
        if(0 <= x <= 7 and 0 <= y <= 7):
            if(Board[x][y] == '.'):
                lst.append([x, y])
            else:
                if(abs(Board[x][y].color - color) == 1):
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
def FEN_get():
    FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
    i = 0
    x = 0
    y = 0
    while i < len(FEN):
        if 49 <= ord(FEN[i]) <= 56:
            y += int(FEN[i])
        if FEN[i] == 'r':
            Board[x][y] = Rook(0, x, y)
            y += 1
        if FEN[i] == 'R':
            Board[x][y] = Rook(1, x, y)
            y += 1
        if FEN[i] == 'k':
            Board[x][y] = King(0, x, y)
            y += 1
        if FEN[i] == 'K':
            Board[x][y] = King(1, x, y)
            y += 1
        if FEN[i] == 'b':
            Board[x][y] = Bishop(0, x, y)
            y += 1
        if FEN[i] == 'B':
            Board[x][y] = Bishop(1, x, y)
            y += 1
        if FEN[i] == 'p':
            Board[x][y] = Pawn(0, x, y)
            y += 1
        if FEN[i] == 'P':
            Board[x][y] = Pawn(1, x, y)
            y += 1
        if FEN[i] == 'q':
            Board[x][y] = Queen(0, x, y)
            y += 1
        if FEN[i] == 'Q':
            Board[x][y] = Queen(1, x, y)
            y += 1
        if FEN[i] == 'n':
            Board[x][y] = Knight(0, x, y)
            y += 1
        if FEN[i] == 'N':
            Board[x][y] = Knight(1, x, y)
            y += 1
        if FEN[i] == '/':
            x += 1
            y = 0
        i += 1
def Print_Board():
    Print_Board = ''
    for y in range(8):
        Print_Board += ''.join(map(str, Board[y])) + "\n"
        #FEN += ''.join(map(str, Board[y])) + "/"
    return Print_Board
def Print_move(moven):
    printing = ''
    x_coord = moven[2]
    y_coord = moven[3]
    letter = Board[moven[2]][moven[3]].__str__()
    x_coord = 8 - x_coord
    y_coord = chr(ord('a') + y_coord)   
    match letter:
        case 'p'|'P':
            letter = ''
        case 'k'|'K':
            letter = 'K'
        case 'n'|'N':
            letter = 'N'
        case 'b'|'B':
            letter = 'B'
        case 'q'|'Q':
            letter = 'Q'
        case 'r'|'R':
            letter = 'R'
    printing = str(letter) + str(y_coord) + str(x_coord)
    return printing


FEN_get()
print(Print_Board())

def Print_coord(cur_moves):
    printing = ''
    for i in range (len(cur_moves)):
        x_coord = cur_moves[i][2]
        y_coord = cur_moves[i][3]
        letter = Board[cur_moves[i][0]][cur_moves[i][1]].__str__()
        x_coord = 8 - x_coord
        y_coord = chr(ord('a') + y_coord)
        x_old = 8 - cur_moves[i][0]
        y_old = chr(ord('a') + cur_moves[i][1])
        match letter:
            case 'p'|'P':
                letter = ''
            case 'k'|'K':
                letter = 'K'
            case 'n'|'N':
                letter = 'N'
            case 'b'|'B':
                letter = 'B'
            case 'q'|'Q':
                letter = 'Q'
            case 'r'|'R':
                letter = 'R'
        printing += str(letter) + str(y_old) + str(x_old) +'-'+ str(y_coord) + str(x_coord) + ' '
    return printing

def Do_Move(move):
    Board[move[2]][move[3]] = Board[move[0]][move[1]]
    Board[move[2]][move[3]].x = move[2] 
    Board[move[2]][move[3]].y = move[3]
    Board[move[0]][move[1]] = '.'
while half_move <= 25:
    cur_moves = Possible_move(move_turn)
    number = randint(0, (len(cur_moves) - 1))
    move = [cur_moves[number][0], cur_moves[number][1], cur_moves[number][2], cur_moves[number][3]]
    print('\n', Print_coord(cur_moves))
    print('\n')
    Do_Move(move)
    if move_turn == 1:
        print(half_move//2 + 1, end= '')
        print('.', end= ' ')
        print(Print_move(move), end='')
    else:
        print(' ', Print_move(move))
    move_turn = abs(1 - move_turn)
    half_move += 1

print('\n', Print_Board())
