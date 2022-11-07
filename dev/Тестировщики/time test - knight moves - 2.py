import time
start_time = time.time()

class Piece(object):
    IMG = None
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    def __str__(self):
        return self.IMG[0 if self.color == 0 else 1] 
class Knight(Piece):
    IMG = ('n', 'N')
    def Take_Move(color, x, y):
        lst = []
        if 0 <= x <= 7 and 0 <= y <= 7:
            if Board[x][y] == '.':
                lst.append([x, y])
            else:
                if abs(color - Board[x][y].color) == 1:
                    lst.append([x, y])
        return lst
    
    def Moves(self):
        moves = []
        moves += Knight.Take_Move(self.color, self.x - 1, self.y - 2)
        moves += Knight.Take_Move(self.color, self.x - 2, self.y - 1)
        moves += Knight.Take_Move(self.color, self.x - 2, self.y + 1)
        moves += Knight.Take_Move(self.color, self.x - 1, self.y + 2)
        moves += Knight.Take_Move(self.color, self.x + 1, self.y + 2)                
        moves += Knight.Take_Move(self.color, self.x + 2, self.y + 1) 
        moves += Knight.Take_Move(self.color, self.x + 2, self.y - 1)
        moves += Knight.Take_Move(self.color, self.x + 1, self.y - 2) 
        return moves

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
Board[1][3] = Knight(1, 1, 3)
Board[4][6] = Knight(1, 4, 6)
Board[3][2] = Knight(1, 3, 2)
Board[7][1] = Knight(1, 7, 1)
Board[5][2] = Knight(1, 5, 2)
Board[0][1] = Knight(1, 0, 1)
Board[1][5] = Knight(1, 1, 5)
Board[7][3] = Knight(1, 7, 3)
Board[4][3] = Knight(1, 4, 3)
Board[2][0] = Knight(1, 2, 0)
Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"
print(Print_Board)
print(Knight(1, 1, 3).Moves())
print(Knight(1, 4, 6).Moves())
print(Knight(1, 3, 2).Moves())
print(Knight(1, 7, 1).Moves())
print(Knight(1, 5, 2).Moves())
print(Knight(1, 0, 1).Moves())
print(Knight(1, 1, 5).Moves())
print(Knight(1, 7, 3).Moves())
print(Knight(1, 4, 3).Moves())
print(Knight(1, 2, 0).Moves())
print("-— %s seconds —-" % (time.time() - start_time))
