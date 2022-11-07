class Pawn(object):
    #НЕ РЕАЛИЗОВАНЫ ВЗЯТИЯ И ВЗЯТИЯ НА ПРОХОДЕ И НЕ РЕАЛИЗОВАНО ПРЕВРАЩЕНИЕ ПЕШКИ В ФЕРЗИ
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

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
            if(self.x + 1 < 7 and Board[self.x - 1][self.y] == '.'): 
                moves.append([self.x + 1, self.y])
                if(self.x == 1 and Board[self.x + 2][self.y] == '.'):
                    moves.append([self.x + 2, self.y])
        return moves

class Knight(object):
    #НЕ РЕАЛИЗОВАНЫ ВЗЯТИЯ
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

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

class Bishop(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        if self.color == 'White':
            return 'B'
        else:
            if self.color == 'Black':
                return 'b'

    def Moves(self):
        moves =[]
        if (self.color == 'White' or self.color == 'Black'):
            if(0 <= self.x - 1 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x - 1][self.y - 1] == '.'):
                moves.append([self.x - 1, self.y - 1])
                
                if(0 <= self.x - 2 <= 7 and 0 <= self.y - 2 <= 7 and Board[self.x - 2][self.y - 2] == '.'):
                    moves.append([self.x - 2, self.y - 2])
                    
                    if(0 <= self.x - 3 <= 7 and 0 <= self.y - 3 <= 7 and Board[self.x - 3][self.y - 3] == '.'):
                        moves.append([self.x - 3, self.y - 3])

                        if(0 <= self.x - 4 <= 7 and 0 <= self.y - 4 <= 7 and Board[self.x - 4][self.y - 4] == '.'):
                            moves.append([self.x - 4, self.y - 4])
                            
                            if(0 <= self.x - 5 <= 7 and 0 <= self.y - 5 <= 7 and Board[self.x - 5][self.y - 5] == '.'):
                                moves.append([self.x - 5, self.y - 5])
                                
                                if(0 <= self.x - 6 <= 7 and 0 <= self.y - 6 <= 7 and Board[self.x - 6][self.y - 6] == '.'):
                                    moves.append([self.x - 6, self.y - 6])
                                    
                                    if(0 <= self.x - 7 <= 7 and 0 <= self.y - 7 <= 7 and Board[self.x - 7][self.y - 7] == '.'):
                                        moves.append([self.x - 7, self.y - 7])
                                        
        if (self.color == 'White' or self.color == 'Black'):
            if(0 <= self.x + 1 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] == '.'):
                moves.append([self.x + 1, self.y + 1])
                
                if(0 <= self.x + 2 <= 7 and 0 <= self.y + 2 <= 7 and Board[self.x + 2][self.y + 2] == '.'):
                    moves.append([self.x + 2, self.y + 2])
                    
                    if(0 <= self.x + 3 <= 7 and 0 <= self.y + 3 <= 7 and Board[self.x + 3][self.y + 3] == '.'):
                        moves.append([self.x + 3, self.y + 3])

                        if(0 <= self.x + 4 <= 7 and 0 <= self.y + 4 <= 7 and Board[self.x + 4][self.y + 4] == '.'):
                            moves.append([self.x + 4, self.y + 4])
                            
                            if(0 <= self.x + 5 <= 7 and 0 <= self.y + 5 <= 7 and Board[self.x + 5][self.y + 5] == '.'):
                                moves.append([self.x + 5, self.y + 5])
                                
                                if(0 <= self.x + 6 <= 7 and 0 <= self.y + 6 <= 7 and Board[self.x + 6][self.y + 6] == '.'):
                                    moves.append([self.x + 6, self.y + 6])
                                    
                                    if(0 <= self.x + 7 <= 7 and 0 <= self.y + 7 <= 7 and Board[self.x + 7][self.y + 7] == '.'):
                                        moves.append([self.x + 7, self.y + 7])
                                        
        if (self.color == 'White' or self.color == 'Black'):
            if(0 <= self.x - 1 <= 7 and 0 <= self.y + 1 <= 7 and Board[self.x - 1][self.y + 1] == '.'):
                moves.append([self.x - 1, self.y + 1])
                
                if(0 <= self.x - 2 <= 7 and 0 <= self.y + 2 <= 7 and Board[self.x - 2][self.y + 2] == '.'):
                    moves.append([self.x - 2, self.y + 2])
                    
                    if(0 <= self.x - 3 <= 7 and 0 <= self.y + 3 <= 7 and Board[self.x - 3][self.y + 3] == '.'):
                        moves.append([self.x - 3, self.y + 3])

                        if(0 <= self.x - 4 <= 7 and 0 <= self.y + 4 <= 7 and Board[self.x - 4][self.y + 4] == '.'):
                            moves.append([self.x - 4, self.y + 4])
                            
                            if(0 <= self.x - 5 <= 7 and 0 <= self.y + 5 <= 7 and Board[self.x - 5][self.y + 5] == '.'):
                                moves.append([self.x - 5, self.y + 5])
                                
                                if(0 <= self.x - 6 <= 7 and 0 <= self.y + 6 <= 7 and Board[self.x - 6][self.y + 6] == '.'):
                                    moves.append([self.x - 6, self.y + 6])
                                    
                                    if(0 <= self.x - 7 <= 7 and 0 <= self.y + 7 <= 7 and Board[self.x - 7][self.y + 7] == '.'):
                                        moves.append([self.x - 7, self.y + 7])

        if (self.color == 'White' or self.color == 'Black'):
            if(0 <= self.x + 1 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x + 1][self.y - 1] == '.'):
                moves.append([self.x + 1, self.y - 1])
                
                if(0 <= self.x + 2 <= 7 and 0 <= self.y - 2 <= 7 and Board[self.x + 2][self.y - 2] == '.'):
                    moves.append([self.x + 2, self.y - 2])
                    
                    if(0 <= self.x + 3 <= 7 and 0 <= self.y - 3 <= 7 and Board[self.x + 3][self.y - 3] == '.'):
                        moves.append([self.x + 3, self.y - 3])

                        if(0 <= self.x + 4 <= 7 and 0 <= self.y - 4 <= 7 and Board[self.x + 4][self.y - 4] == '.'):
                            moves.append([self.x + 4, self.y - 4])
                            
                            if(0 <= self.x + 5 <= 7 and 0 <= self.y - 5 <= 7 and Board[self.x + 5][self.y - 5] == '.'):
                                moves.append([self.x + 5, self.y - 5])
                                
                                if(0 <= self.x + 6 <= 7 and 0 <= self.y - 6 <= 7 and Board[self.x + 6][self.y - 6] == '.'):
                                    moves.append([self.x + 6, self.y - 6])
                                    
                                    if(0 <= self.x + 7 <= 7 and 0 <= self.y - 7 <= 7 and Board[self.x + 7][self.y - 7] == '.'):
                                        moves.append([self.x + 7, self.y - 7])


            

class King(object):
    #НЕ РЕАЛИЗОВАНЫ: ШАХИ, ВЗЯТИЯ ЧУЖИХ ФИГУР КОРОЛЁМБ РОКИРОВКА
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



Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(King('White', 7, 4).Moves())

print(King('White', 7, 4).Moves())

print(Pawn('White', 6, 3).Moves())

print(Pawn('Black', 1, 7).Moves())

print(Knight('Black', 0, 1).Moves())

print(Knight('White', 7, 6).Moves())

