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
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
class King(Piece):  
    def __str__(self):
        if self.color == 1:
            return 'K'
        else:
            return 'k'

    def Get_Move(color, x, y):
        impos = Check_moves(color)
        if(0 <= x <= 7 and 0 <= y <= 7):
            if(Board[x][y] == '.'):
                if [x, y] not in impos:
                    return 1
            else:
                if(abs(Board[x][y].color - color) == 1):
                    if Pos_beat(color, x, y) == 1:
                        return 1
        
    def Moves(self):
        moves = []
        if King.Get_Move(self.color, self.x - 1, self.y - 1) == 1:
            moves.append([self.x - 1, self.y - 1])
            
        if King.Get_Move(self.color, self.x, self.y - 1) == 1:
            moves.append([self.x, self.y - 1])

        if King.Get_Move(self.color, self.x + 1, self.y - 1) == 1:
            moves.append([self.x + 1, self.y - 1])
            
        if King.Get_Move(self.color, self.x - 1, self.y) == 1:
            moves.append([self.x - 1, self.y])
                    
        if King.Get_Move(self.color, self.x + 1, self.y) == 1:
            moves.append([self.x + 1, self.y])
            
        if King.Get_Move(self.color, self.x, self.y - 1) == 1:
            moves.append([self.x, self.y - 1])
                    
        if King.Get_Move(self.color, self.x, self.y + 1) == 1:
            moves.append([self.x, self.y + 1])
                    
        if King.Get_Move(self.color, self.x + 1, self.y + 1) == 1:
                moves.append([self.x + 1, self.y + 1])

        return moves
            


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     

Board[7][4] = King(1, 7, 4)



Board[5][4] = King(0, 5, 4)


Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)
print(King(1, 7, 4).Moves())
