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

class Rook(Piece):
    def __str__(self):
        if self.color == 1:
            return 'R'
        else:
            return 'r'

    def Moves(self):
        moves = []
        a = self.x
        b = self.y - 1
        while b>=0:
            if Board[a][b] == '.':
                moves.append([a, b])
                b -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])
                break
                
        b = self.y + 1
        while b <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                b += 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])                
                break

        a = self.x - 1
        b = self.y
        while a >= 0:
            if Board[a][b] == '.':
                moves.append([a, b])
                a -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])
                break

        a = self.x + 1
        while a <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                a += 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])
                break
                
        return moves
        


class King(Piece):  
    def __str__(self):
        if self.color == 1:
            return 'K'
        else:
            return 'k'

            
    def Moves(self):
        moves = []
        impos = Check_moves(self.color)
        if(0 <= self.x - 1 <= 7 and 0 <= self.y - 1 <= 7):
            if(Board[self.x - 1][self.y - 1] == '.'):
                if [self.x - 1, self.y - 1] not in impos:
                    moves.append([self.x - 1, self.y - 1])
            else:
                if(abs(Board[self.x - 1][self.y - 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x - 1, self.y - 1) == 1:
                        moves.append([self.x - 1, self.y - 1]) 
         
        if(0 <= self.y - 1 <= 7):
            if(Board[self.x][self.y - 1] == '.'):
                if [self.x, self.y - 1] not in impos:
                    moves.append([self.x, self.y - 1])
            else:
                if(abs(Board[self.x][self.y - 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x, self.y - 1) == 1:
                        moves.append([self.x, self.y - 1])

        if(0 <= self.x + 1 <= 7 and 0 <= self.y - 1 <= 7):
            if(Board[self.x + 1][self.y - 1] == '.'):
                if [self.x + 1, self.y - 1] not in impos:
                    moves.append([self.x + 1, self.y - 1])
            else:
                if(abs(Board[self.x + 1][self.y - 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x + 1, self.y - 1) == 1:
                        moves.append([self.x + 1, self.y - 1])
                
        if(0 <= self.x - 1 <= 7):
            if(Board[self.x - 1][self.y] == '.'):
                if [self.x - 1, self.y] not in impos:
                    moves.append([self.x - 1, self.y])
            else:
                if(abs(Board[self.x - 1][self.y].color - self.color) == 1):
                    if Pos_beat(self.color, self.x - 1, self.y) == 1:
                        moves.append([self.x - 1, self.y])
                    
        if(0 <= self.x + 1 <= 7):
            if(Board[self.x + 1][self.y] == '.'):
                if [self.x + 1, self.y] not in impos:
                    moves.append([self.x + 1, self.y])
            else:
                if(abs(Board[self.x + 1][self.y].color - self.color) == 1):
                    if Pos_beat(self.color, self.x + 1, self.y) == 1:
                        moves.append([self.x + 1, self.y])
                
        if(0 <= self.x - 1 <= 7 and 0 <= self.y + 1 <= 7):
            if(Board[self.x - 1][self.y + 1] == '.'):
                if [self.x - 1, self.y + 1] not in impos:
                    moves.append([self.x - 1, self.y + 1])
            else:
                if(abs(Board[self.x - 1][self.y + 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x - 1, self.y + 1) == 1:
                        moves.append([self.x - 1, self.y + 1])
                    
        if(0 <= self.y + 1 <= 7):
            if(Board[self.x][self.y + 1] == '.'):
                if [self.x, self.y + 1] not in impos:
                    moves.append([self.x, self.y + 1])
            else:
                if(abs(Board[self.x][self.y + 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x, self.y + 1) == 1:
                        moves.append([self.x, self.y + 1])
                    
        if(0 <= self.x + 1 <= 7 and 0 <= self.y + 1 <= 7):
            if(Board[self.x + 1][self.y + 1] == '.'):
                if [self.x + 1, self.y + 1] not in impos:
                    moves.append([self.x + 1, self.y + 1])
            else:
                if(abs(Board[self.x + 1][self.y + 1].color - self.color) == 1):
                    if Pos_beat(self.color, self.x + 1, self.y + 1) == 1:
                        moves.append([self.x + 1, self.y + 1])

        return moves
            


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     

Board[7][4] = King(1, 7, 4)
Board[6][4] = Rook(0, 6, 4)
Board[5][4] = King(0, 5, 4)


Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(King(1, 7, 4).Moves())
