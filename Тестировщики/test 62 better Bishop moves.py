class Piece(object):
    IMG = None
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    def __str__(self):
        return self.IMG[0 if self.color == 0 else 1]

class Bishop(Piece):
    IMG = ('b', 'B')
    
    def Take_Moves(color, x, y, i, j):
        lst = []
        x = x + i
        y = y + j
        while 0 <= x <= 7 and 0 <= y <= 7:
            if Board[x][y] == '.':
                lst.append([x, y])
                x += i
                y += j
            else:
                if(abs(color - Board[x][y].color) == 1):
                    lst.append([x, y])
                break
        return lst
            
    def Moves(self):
        moves = []
        moves += Bishop.Take_Moves(self.color, self.x, self.y, 1, 1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, 1, -1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, -1, 1)
        moves += Bishop.Take_Moves(self.color, self.x, self.y, -1, -1)        
        return moves
    

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']

Board[7][2] = Bishop(1, 7, 2)
Board[7][5] = Bishop(1, 7, 5)

Board[0][2] = Bishop(0, 0, 2)
Board[0][5] = Bishop(0, 0, 5)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"

print(Print_Board)
print(Bishop(1, 7, 2).Moves())
