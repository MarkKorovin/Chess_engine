class King(object):
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
        if (self.color == 'White'):
            if(0 <= self.x - 1 <= 7 and 0 <= self.y - 1 <= 7 and Board[self.x - 1][self.y - 1] == '.'):
                moves.append([self.x - 1, self.y - 1])
                if(97 <= ord(Board[self.x - 1][self.y - 1]) <= 122): #ПРОВЕРКА ПОПАДАНИЯ ПОД ШАХ!
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
Board[0][4] = King('Black', 7, 4)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)
print(King('White', 7, 4).Moves())
