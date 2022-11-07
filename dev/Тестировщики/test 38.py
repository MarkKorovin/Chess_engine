##НЕ РЕАЛИЗОВАННЫЕ НЮАНСЫ:
#1. ШАХИ И МАТЫ
#2. ВЗЯТИЯ (В ТОМ ЧИСЛЕ ВЗЯТИЯ НА ПРОХОДЕ ДЛЯ ПЕШЕК)
#3. ПРЕВРАЩЕНИЯ ПЕШЕК В ФИГУРЫ
#4. РОКИРОВКА
# Можно сделать преобразователь координат по y в буквы, а координат по х со сдвигом на 1.


class Piece(object):
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
    def defence(self):
        return defence

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
                    
            if(self.x - 1 >= 0 and self.y - 1 >= 0 and Board[self.x - 1][self.y - 1] != '.'):
                
                if(Board[self.x - 1][self.y - 1].color == 'Black'):
                    moves.append([self.x - 1, self.y - 1])
                else:
                    Board[self.x - 1][self.y - 1].defence += 1
                    
            if(self.x - 1 >= 0 and self.y + 1 <= 7 and Board[self.x - 1][self.y + 1] != '.'):
                
                if(Board[self.x - 1][self.y + 1].color == 'Black'):
                    moves.append([self.x - 1, self.y + 1])
                else:
                    Board[self.x - 1][self.y + 1].defence += 1

        if(self.color == 'Black'):
            
            if(self.x + 1 < 7 and Board[self.x + 1][self.y] == '.'):
                moves.append([self.x + 1, self.y])
                if(self.x == 1 and Board[self.x + 2][self.y] == '.'):
                    moves.append([self.x + 2, self.y])
                    
            if(self.x + 1 <= 7 and self.y + 1 <= 7 and Board[self.x + 1][self.y + 1] != '.'):

                if Board[self.x + 1][self.y + 1] == 'White':
                    moves.append([self.x + 1, self.y + 1])
                else:
                    Board[self.x + 1][self.y + 1].defence += 1
                    
            if(self.x + 1 <= 7 and self.y - 1 >= 0 and Board[self.x + 1][self.y - 1] != '.'):
                if Board[self.x + 1][self.y - 1] == 'White':
                    moves.append([self.x + 1, self.y - 1])
                else:
                    Board[self.x + 1][self.y - 1].defence += 1
                    
                    
        return moves


Board = [[],[],[],[],[],[],[],[]]
for i in range(8):
    Board[i] = ['.', '.', '.', '.', '.', '.', '.', '.']     



Board[6][0] = Pawn('White', 6, 0)
Board[5][1] = Pawn('White', 5, 1)
Board[6][2] = Pawn('White', 6, 2)
Board[6][3] = Pawn('White', 6, 3)
Board[6][4] = Pawn('White', 6, 4)
Board[6][5] = Pawn('White', 6, 5)
Board[6][6] = Pawn('White', 6, 6)
Board[6][7] = Pawn('White', 6, 7)





Print_Board = ''
for y in range(8):
    Print_Board += ''.join(map(str, Board[y])) + "\n"



print(Print_Board)

Pawn('White', 6, 0).Moves
Pawn('White', 6, 2).Moves
Pawn('White', 5, 1).Moves

Pawn('White', 6, 0)
Pawn('White', 6, 2)
Pawn('White', 5, 1)





#Реализовать поиск ходов достаточно просто. Надо пробежать по всему массиву и в случае обнаружения не точки проверить совпадения с буквой.
# А потом вызвать функцию фигуры по заданым координатам и цвету.

