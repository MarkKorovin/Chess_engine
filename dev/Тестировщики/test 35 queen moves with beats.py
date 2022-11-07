##НЕ РЕАЛИЗОВАННЫЕ НЮАНСЫ:
#1. ШАХИ И МАТЫ
#2. ВЗЯТИЯ (В ТОМ ЧИСЛЕ ВЗЯТИЯ НА ПРОХОДЕ ДЛЯ ПЕШЕК)
#3. ПРЕВРАЩЕНИЯ ПЕШЕК В ФИГУРЫ
#4. РОКИРОВКА
# Можно сделать преобразователь координат по y в буквы, а координат по х со сдвигом на 1.

Black_pieces = ['p', 'k', 'b', 'r', 'q']
White_pieces = ['P', 'K', 'B', 'R', 'Q']
class Piece(object):
    global Black_pieces
    global White_pieces
    def __init__ (self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


        
class Queen(Piece):
    #НЕ РЕАЛИЗОВАНЫ: ШАХИ, ВЗЯТИЯ
    def __str__(self):
        if (self.color == 'White'):
            return 'Q'
        else:
            if (self.color == 'Black'):
                return 'q'
    def Moves(self):
        moves = []

                
        if (self.color == 'Black'):
            a = self.x - 1
            b = self.y - 1
            while a>=0 and b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b -= 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break
                
            a = self.x + 1
            b = self.y + 1
            
            while a <= 7 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b += 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

            a = self.x - 1
            b = self.y + 1
            while a >= 0 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b += 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

            a = self.x + 1
            b = self.y - 1
            while a <= 7 and b >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b -= 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

            
            a = self.x
            b = self.y - 1
            while b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b -= 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break
                
            b = self.y + 1
            while b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b += 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

            a = self.x - 1
            b = self.y
            while a >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

            a = self.x + 1
            while a <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                else:
                    if Board[a][b].color == 'White':
                        moves.append([a, b])
                    break

                
                
        if (self.color == 'White'):
            
            a = self.x
            b = self.y - 1
            while b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b -= 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break
                
            b = self.y + 1
            while b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    b += 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break

            a = self.x - 1
            b = self.y
            while a >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break

            a = self.x + 1
            while a <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break

            a = self.x - 1
            b = self.y - 1
            while a>=0 and b>=0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b -= 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break
                
            a = self.x + 1
            b = self.y + 1
            
            while a <= 7 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b += 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break

            a = self.x - 1
            b = self.y + 1
            while a >= 0 and b <= 7:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a -= 1
                    b += 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break

            a = self.x + 1
            b = self.y - 1
            while a <= 7 and b >= 0:
                if Board[a][b] == '.':
                    moves.append([a, b])
                    a += 1
                    b -= 1
                else:
                    if Board[a][b].color == 'Black':
                        moves.append([a, b])
                    break
                
        return moves
 





Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     




Board[7][3] = Queen('White', 7, 3)
Board[0][3] = Queen('Black', 0, 3)

Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

print(Queen('White', 7, 3).Moves())

