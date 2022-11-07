class Piece(object):
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
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

Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     



Board[7][0] = Rook('White', 7, 0)
Board[7][7] = Rook('White', 7, 7)


Board[0][0] = Rook('Black', 0, 0)
Board[0][7] = Rook('Black', 0, 7)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(Rook('White', 7, 0).Moves())

print(Rook('White', 7, 7).Moves())

print(Rook('Black', 0, 0).Moves())

print(Rook('Black', 0, 7).Moves())


