class Pawn(Piece):
    IMG = ('p', 'P')
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
            if self.x + 1 < 7 and self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] != '.':
                if Board[self.x + 1][self.y + 1].color == 1:
                    moves.append([self.x + 1, self.y + 1])   
            if self.x + 1 < 7 and self.y - 1 >= 0 and Board[self.x + 1][self.y - 1] != '.':
                if Board[self.x + 1][self.y - 1].color == 1:
                    moves.append([self.x + 1, self.y - 1])
        return moves
    
class Pawn(Piece):
    IMG = ('p', 'P')
    def Moves(self):
        moves = []
        cells = [1, -1]]
        a = (-self.color)*2 + 1
        if 0 < self.x < 7 and Board[self.x + a][self.y] == '.':
            moves.append([self.x + a, self.y])
            if (self.color == 0 and self.x == 1) or (self.color == 1 and self.x == 6):
                moves.append([self.x + a*2, self.y])
        for i in range(len(cells)):
            if 0 < self.x + a < 7 and 0 < self.y + cells[i] < 7:
                if Board[self.x + a][self.y + cells[i]] != '.':
                    if abs(self.color - Board[self.x + a][self.y + cells[i]].color) == 1:
                        moves.append([self.x + a, self.y + cells[i]]
    return moves







