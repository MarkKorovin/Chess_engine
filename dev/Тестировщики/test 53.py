#CРАЗУ ДОГОВОРИМСЯ, ЧТО БЕЛЫЕ - ЭТО ЦВЕТ 1, А ЧЁРНЫЕ - ЦВЕТ 0

##НЕ РЕАЛИЗОВАННЫЕ НЮАНСЫ:
#1. ШАХИ И МАТЫ
#2. ВЗЯТИЕ НА ПРОХОДЕ
#3. ПРЕВРАЩЕНИЯ ПЕШЕК В ФИГУРЫ
#4. РОКИРОВКА

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


class Pawn(Piece):
    def __str__(self):
        if self.color == 1:
            return 'P'
        else:
            return 'p'

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
    def __str__(self):
        if (self.color == 1):
            return 'N'
        else:
            return 'n'

    def Moves(self):
        moves = []
        
    
        if 0 <= self.x - 1 <= 7 and 0 <= self.y - 2 <= 7:
            if Board[self.x - 1][self.y - 2] == '.':
                moves.append([self.x - 1, self.y - 2])
            else:
                if abs(self.color - Board[self.x - 1][self.y - 2].color) == 1:
                    moves.append([self.x - 1, self.y - 2])
                    
                
        if 0 <= self.x - 2 <= 7 and 0 <= self.y - 1 <= 7:
             if Board[self.x - 2, self.y - 1] == '.':
                moves.append([self.x - 2, self.y - 1])
                
             else:
                if abs(self.color - Board[self.x - 2, self.y - 1].color) == 1:
                    moves.append([self.x - 2, self.y - 1])


        if 0 <= self.x - 2 <= 7 and 0 <= self.y + 1 <= 7:
            
             if Board[self.x - 2, self.y + 1] == '.':
                moves.append([self.x - 2, self.y + 1])
                
             else:
                if abs(self.color - Board[self.x - 2, self.y + 1].color) == 1:
                    moves.append([self.x - 2, self.y + 1])

                
        if 0 <= self.x - 1 <= 7 and 0 <= self.y + 2 <= 7:
            
             if Board[self.x - 1, self.y + 2] == '.':
                moves.append([self.x - 1, self.y + 2])
                
             else:
                if abs(self.color - Board[self.x - 1, self.y + 2].color) == 1:
                    moves.append([self.x - 1, self.y + 2])


        if 0 <= self.x + 1 <= 7 and 0 <= self.y + 2 <= 7:
            
             if Board[self.x + 1, self.y + 2] == '.':
                moves.append([self.x + 1, self.y + 2])
                
             else:
                if abs(self.color - Board[self.x + 1, self.y + 2].color) == 1:
                    moves.append([self.x + 1, self.y + 2])
                
        if 0 <= self.x + 2 <= 7 and 0 <= self.y + 1 <= 7:
            
             if Board[self.x + 2, self.y + 1] == '.':
                moves.append([self.x + 2, self.y + 1])
                
             else:
                if abs(self.color - Board[self.x + 2, self.y + 1].color) == 1:
                    moves.append([self.x + 2, self.y + 1])


        if 0 <= self.x + 2 <= 7 and 0 <= self.y - 1 <= 7:
            
             if Board[self.x + 2, self.y - 1] == '.':
                moves.append([self.x + 2, self.y - 1])
                
             else:
                if abs(self.color - Board[self.x + 2, self.y - 1].color) == 1:
                    moves.append([self.x + 2, self.y - 1])


        if 0 <= self.x + 1 <= 7 and 0 <= self.y - 2 <= 7:
            
             if Board[self.x + 1, self.y - 2] == '.':
                moves.append([self.x + 1, self.y - 2])
                
             else:
                if abs(self.color - Board[self.x + 1, self.y - 2].color) == 1:
                    moves.append([self.x + 1, self.y - 2])


        return moves

class Bishop(Piece):
    def __str__(self):
        if self.color == 1:
            return 'B'
        else:
            return 'b'

    def Moves(self):
        
        moves =[]
        a = self.x - 1
        b = self.y - 1
        while a>=0 and b>=0:
            if Board[a][b] == '.':
                moves.append([a, b])
                a -= 1
                b -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])
                break
             
        a = self.x + 1
        b = self.y + 1
            
        while a <= 7 and b <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                a += 1
                b += 1          
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])               
                break

        a = self.x - 1
        b = self.y + 1
        while a >= 0 and b <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                a -= 1
                b += 1           
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                     moves.append([a, b])               
                break

        a = self.x + 1
        b = self.y - 1
        while a <= 7 and b >= 0:
            if Board[a][b] == '.':
                moves.append([a, b])
                a += 1
                b -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                     moves.append([a, b])               
                break
                
        return moves

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
        
class Queen(Piece):
    def __str__(self):
        if self.color == 1:
            return 'Q'
        else:
            return 'q'
        
    def Moves(self):
        moves = []
        a = self.x - 1
        b = self.y - 1
        while a>=0 and b>=0:
            if Board[a][b] == '.':
                moves.append([a, b])
                a -= 1
                b -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])
                break
             
        a = self.x + 1
        b = self.y + 1
            
        while a <= 7 and b <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                a += 1
                b += 1          
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                    moves.append([a, b])                 
                break

        a = self.x - 1
        b = self.y + 1
        while a >= 0 and b <= 7:
            if Board[a][b] == '.':
                moves.append([a, b])
                a -= 1
                b += 1           
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                     moves.append([a, b])                
                break

        a = self.x + 1
        b = self.y - 1
        while a <= 7 and b >= 0:
            if Board[a][b] == '.':
                moves.append([a, b])
                a += 1
                b -= 1
            else:
                if(abs(self.color - Board[a][b].color) == 1):
                     moves.append([a, b])                
                break

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

