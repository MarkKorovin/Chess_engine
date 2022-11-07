##НЕ РЕАЛИЗОВАННЫЕ НЮАНСЫ:
#1. ШАХИ И МАТЫ
#2. ВЗЯТИЯ (В ТОМ ЧИСЛЕ ВЗЯТИЯ НА ПРОХОДЕ ДЛЯ ПЕШЕК)
#3. ПРЕВРАЩЕНИЯ ПЕШЕК В ФИГУРЫ
#4. РОКИРОВКА


class Piece(object):
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class Pawn(Piece):
    #НЕ РЕАЛИЗОВАНЫ ВЗЯТИЯ И ВЗЯТИЯ НА ПРОХОДЕ И НЕ РЕАЛИЗОВАНО ПРЕВРАЩЕНИЕ ПЕШКИ В ФЕРЗИ
    def __str__(self):
        if (self.color == 'White'):
            return 'P'
        else:
            if (self.color == 'Black'):
                return 'p'

    def Moves(self):
        moves = []
        if(self.color == 'White'):
            if(self.x - 1 > 0 and Board[self.x - 1][self.y] == '.'):
                moves.append([self.x - 1, self.y])
                
                if(self.x == 6 and Board[self.x - 2][self.y] == '.'):
                    moves.append([self.x - 2, self.y])

        if(self.color == 'Black'):
            if(self.x + 1 < 7 and Board[self.x + 1][self.y] == '.'): 
                moves.append([self.x + 1, self.y])
                
                if(self.x == 1 and Board[self.x + 2][self.y] == '.'):
                    moves.append([self.x + 2, self.y])
                    
        return moves

class Knight(Piece):
    #НЕ РЕАЛИЗОВАНЫ ВЗЯТИЯ И ШАХИ

    def __str__(self):
        if (self.color == 'White'):
            return 'N'
        else:
            if (self.color == 'Black'):
                return 'n'

    def Moves(self):
        moves = []
        if (self.color == 'Black' or self.color == 'White'):
            if (0 <= self.x - 1 <= 7 and 0 <= self.y - 2 <= 7 and Board[self.x - 1][self.y - 2] == '.'):
                moves.append([self.x - 1, self.y - 2])
                
            if (0 <= self.x - 2 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x - 2][self.y - 1] == '.'):
                moves.append([self.x - 2, self.y - 1])

            if (0 <= self.x - 2 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x - 2][self.y + 1] == '.'):
                moves.append([self.x - 2, self.y + 1])
                
            if (0 <= self.x - 1 <= 7 and 0 <= self.y + 2 <= 7 and Board[self.x - 1][self.y + 2] == '.'):
                moves.append([self.x - 1, self.y + 2])

            if (0 <= self.x + 1 <= 7 and 0 <= self.y + 2 <= 7 and Board[self.x + 1][self.y + 2] == '.'):
                moves.append([self.x + 1, self.y + 2])
                
            if (0 <= self.x + 2 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x + 2][self.y + 1] == '.'):
                moves.append([self.x + 2, self.y + 1])

            if (0 <= self.x + 2 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x + 2][self.y - 1] == '.'):
                moves.append([self.x + 2, self.y - 1])

            if (0 <= self.x + 1 <= 7 and 0 <= self.y - 2 <= 7 and Board[self.x + 1][self.y - 2] == '.'):
                moves.append([self.x + 1, self.y - 2])

        return moves

class Bishop(Piece):
    #НЕ РЕАЛИЗОВАНЫ ВЗЯТИЯ И ШАХИ

    def __str__(self):
        if self.color == 'White':
            return 'B'
        else:
            if self.color == 'Black':
                return 'b'

    def Moves(self):
        moves =[]
        if (self.color == 'White' or self.color == 'Black'):
            a = self.x - 1
            b = self.y - 1
            while a>=0 and b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b -= 1
                else:
                    break
                
            a = self.x + 1
            b = self.y + 1
            
            while a <= 7 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b += 1
                else:
                    break

            a = self.x - 1
            b = self.y + 1
            while a >= 0 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b += 1
                else:
                    break

            a = self.x + 1
            b = self.y - 1
            while a <= 7 and b >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b -= 1
                else:
                    break
                
        return moves

class Rook(Piece):
    #НЕ РЕАЛИЗОВАНЫ: ШАХИ, ВЗЯТИЯ, РОКИРОВКА
    def __str__(self):
        if (self.color == 'White'):
            return 'R'
        else:
            if (self.color == 'Black'):
                return 'r'
    def Moves(self):
        moves = []
        if (self.color == 'White' or self.color == 'Black'):
            
            a = self.x
            b = self.y - 1
            while b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b -= 1
                else:
                    break
                
            b = self.y + 1
            while b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b += 1
                else:
                    break

            a = self.x - 1
            b = self.y
            while a >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                else:
                    break

            a = self.x + 1
            while a <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                else:
                    break
                
        return moves
        
class Queen(Piece):
    #НЕ РЕАЛИЗОВАНЫ: ШАХИ, ВЗЯТИЯ
    def __str__(self):
        if (self.color == 'White'):
            return 'Q'
        else:
            if (self.color == 'Black'):
                return 'q'
    def Moves(self):
        moves = []
        if (self.color == 'White' or self.color == 'Black'):
            a = self.x
            b = self.y - 1
            while b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b -= 1
                else:
                    break
                
            b = self.y + 1
            while b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b += 1
                else:
                    break

            a = self.x - 1
            b = self.y
            while a >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                else:
                    break

            a = self.x + 1
            while a <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                else:
                    break
                
        
            a = self.x - 1
            b = self.y - 1
            while a>=0 and b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b -= 1
                else:
                    break
                
            a = self.x + 1
            b = self.y + 1
            
            while a <= 7 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b += 1
                else:
                    break

            a = self.x - 1
            b = self.y + 1
            while a >= 0 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b += 1
                else:
                    break

            a = self.x + 1
            b = self.y - 1
            while a <= 7 and b >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b -= 1
                else:
                    break
                
        return moves


class King(Piece):
    #НЕ РЕАЛИЗОВАНЫ: ШАХИ, ВЗЯТИЯ ЧУЖИХ ФИГУР КОРОЛЁМ И РОКИРОВКА
    
    def __str__(self):
        if (self.color == 'White'):
            return 'K'
        else:
            if (self.color == 'Black'):
                return 'k'
            
    def Moves(self):
        moves = []
        if (self.color == 'White' or self.color == 'Black'):
            if(0 <= self.x - 1 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x - 1][self.y - 1] == '.'):
                moves.append([self.x - 1, self.y - 1])
                
            if(0 <= self.y - 1 <= 7 and Board[self.x][self.y - 1] == '.'):
                moves.append([self.x, self.y - 1])

            if(0 <= self.x + 1 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x + 1][self.y - 1] == '.'):
                moves.append([self.x + 1, self.y - 1])
            
            if(0 <= self.x - 1 <= 7 and Board[self.x - 1][self.y] == '.'):
                moves.append([self.x - 1, self.y])
                
            if(0 <= self.x + 1 <= 7 and Board[self.x + 1][self.y] == '.'):
                moves.append([self.x + 1, self.y])
            
            if(0 <= self.x - 1 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x - 1][self.y + 1] == '.'):
                moves.append([self.x - 1, self.y + 1])
                
            if(0 <= self.y + 1 <= 7 and Board[self.x][self.y + 1] == '.'):
                moves.append([self.x, self.y + 1])
                
            if(0 <= self.x + 1 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] == '.'):
                moves.append([self.x + 1, self.y + 1])

        return moves
            



Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     

Board[7][4] = King('White', 7, 4)


Board[6][0] = Pawn('White', 6, 0)
Board[6][1] = Pawn('White', 6, 1)
Board[6][2] = Pawn('White', 6, 2)
Board[6][3] = Pawn('White', 6, 3)
Board[6][4] = Pawn('White', 6, 4)
Board[6][5] = Pawn('White', 6, 5)
Board[6][6] = Pawn('White', 6, 6)
Board[6][7] = Pawn('White', 6, 7)

Board[7][1] = Knight('White', 7, 1)
Board[7][6] = Knight('White', 7, 6)

Board[7][2] = Bishop('White', 7, 2)
Board[7][5] = Bishop('White', 7, 5)

Board[7][0] = Rook('White', 7, 0)
Board[7][7] = Rook('White', 7, 7)


Board[7][3] = Queen('White', 7, 3)


Board[0][4] = King('Black', 0, 4)

Board[1][0] = Pawn('Black', 1, 0)
Board[1][1] = Pawn('Black', 1, 1)
Board[1][2] = Pawn('Black', 1, 2)
Board[1][3] = Pawn('Black', 1, 3)
Board[1][4] = Pawn('Black', 1, 4)
Board[1][5] = Pawn('Black', 1, 5)
Board[1][6] = Pawn('Black', 1, 6)
Board[1][7] = Pawn('Black', 1, 7)

Board[0][1] = Knight('Black', 0, 1)
Board[0][6] = Knight('Black', 0, 6)

Board[0][2] = Bishop('Black', 0, 2)
Board[0][5] = Bishop('Black', 0, 5)

Board[0][0] = Rook('Black', 0, 0)
Board[0][7] = Rook('Black', 0, 7)

Board[0][3] = Queen('Black', 0, 3)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(King('White', 7, 4).Moves())

print(King('Black', 0, 4).Moves())

print(Pawn('White', 6, 3).Moves())

print(Pawn('Black', 1, 7).Moves())

print(Knight('Black', 0, 1).Moves())

print(Knight('White', 7, 6).Moves())
