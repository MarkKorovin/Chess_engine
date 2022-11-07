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


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']
    
Board[3][5] = Bishop('Black', 3, 5)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"


print(Print_Board)

print(Bishop('Black', 3, 5).Moves())
