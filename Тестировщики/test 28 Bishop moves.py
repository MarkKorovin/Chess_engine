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
        return moves


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
    
Board[3][5] = Bishop('Black', 3, 5)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"


print(Print_Board)

print(Bishop('Black', 3, 5).Moves())
