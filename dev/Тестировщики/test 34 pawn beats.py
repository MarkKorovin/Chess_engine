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
        moves = []
        if(self.color == 'White'):
            
            if(self.x - 1 > 0 and Board[self.x - 1][self.y] == '.'):
                moves.append([self.x - 1, self.y])
                if(self.x == 6 and Board[self.x - 2][self.y] == '.'):
                    moves.append([self.x - 2, self.y])
            if(self.x - 1 >= 0 and self.y - 1 >= 0 and Board[self.x - 1][self.y - 1] in Black_pieces):
                moves.append([self.x - 1, self.y - 1])

        if(self.color == 'Black'):
            
            if(self.x + 1 < 7 and Board[self.x + 1][self.y] == '.'):
                moves.append([self.x + 1, self.y])
                if(self.x == 1 and Board[self.x + 2][self.y] == '.'):
                    moves.append([self.x + 2, self.y])
                    
        return moves

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
Board[6][0] = Pawn('White', 6, 0)
Board[6][1] = Pawn('White', 6, 1)
Board[5][0] = 'b'

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"
print(Print_Board)
print(Pawn('White', 6, 0).Moves())
print(Pawn('White', 6, 1).Moves())      
