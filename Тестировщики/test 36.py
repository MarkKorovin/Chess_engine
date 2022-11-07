Black_pieces = ['p', 'k', 'b', 'r', 'q']
White_pieces = ['P', 'K', 'B', 'R', 'Q']
class Piece(object):
    global Black_pieces
    global White_pieces
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class Pawn(Piece):
    
    def __str__(self):
        if (self.color == 'White'):
            return 'P'
        else:
            if (self.color == 'Black'):
                return 'p'

    def Moves(self):
        #Чтобы понимать, о какой фигуре идёт речь, можно в массив добавить информацию о фигуре,
        #а если никаких ходов в нём не будет, то возвращать пустой массив.
        #Иначе же возвращать массив с первым элементом в виде информации о фигуре
        moves = []
        if(self.color == 'White'):
            
            if(self.x - 1 > 0 and Board[self.x - 1][self.y] == '.'):
                moves.append([self.x - 1, self.y])
                if(self.x == 6 and Board[self.x - 2][self.y] == '.'):
                    moves.append([self.x - 2, self.y])
            if(self.x - 1 >= 0 and self.y - 1 >= 0 and Print_Board[self.x - 1][self.y - 1] in Black_pieces):
                moves.append([self.x - 1, self.y - 1])
            if(self.x - 1 >= 0 and self.y + 1 <= 7 and Board[self.x - 1][self.y + 1] == 'p'):
                moves.append([self.x - 1, self.y + 1])

        if(self.color == 'Black'):
            
            if(self.x + 1 < 7 and Board[self.x + 1][self.y] == '.'):
                moves.append([self.x + 1, self.y])
                if(self.x == 1 and Board[self.x + 2][self.y] == '.'):
                    moves.append([self.x + 2, self.y])
                    
            if(self.x + 1 <= 7 and self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] in White_pieces):
                moves.append([self.x + 1, self.y + 1])   
            if(self.x + 1 <= 7 and self.y - 1 >= 0 and Board[self.x + 1][self.y - 1] in White_pieces):
                moves.append([self.x + 1, self.y - 1])
                    
        return moves





Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     


Board[4][4] = Pawn('White', 4, 4)

Board[3][3] = Pawn('Black', 3, 3)


Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(Board[3][3])
print(Pawn('White', 4, 4).Moves())

