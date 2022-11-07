#x - ЦИФРА, y - БУКВА (Attencion!!! началo в левом ВЕРХНЕМ углу!!!)
            
class Pawn(object):
    def __init__(self, color):
        self.color = color
        
    def __repr__(self):
        return('♙', '♟')[self.color]
    #self.color = 0 БЕЛЫЕ ФИГУРЫ
        
    def get_moves(self, board, x, y):
        moves = []
        if self.color == 0 and x<7:
        # and Board(x+1, y) == '.':
            moves.append([x+1, y])
        if self.color == 0 and x==1:
        #Проверка, что пусто!!!
            moves.append([x+2, y])
        if self.color == 1 and x>0:
        #Проверка, что пусто!!!
            moves.append([x-1, y])
        if self.color == 1 and x==6:
        #Проверка, что пусто!!!
            moves.append([x-2, y])
        return moves
        #ДЛЯ 0 РАССМОТРЕТЬ ОТДЕЛЬНЫЙ СЛУЧАЙ ПРЕВРАЩЕНИЯ В ФЕРЗЯ!#

class Board(object):
    def __init__(self):
        self.board = [['.']*8 for y in range(8)]
        self.board[6][0] = Pawn(1)
        self.board[6][1] = Pawn(1)
        self.board[6][2] = Pawn(1)
        self.board[6][3] = Pawn(1)
        self.board[6][4] = Pawn(1)
        self.board[6][5] = Pawn(1)
        self.board[6][6] = Pawn(1)
        self.board[6][7] = Pawn(1)
        
    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)
        
    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.board[y])) + "\n"
        return res
print (Board())
print(Pawn(1).get_moves(1, 6, 2))
"""

if self.color == 0 and x>0 and 
        #ДЛЯ 0 РАССМОТРЕТЬ ОТДЕЛЬНЫЙ СЛУЧАЙ ПРЕВРАЩЕНИЯ В ФЕРЗЯ!#
        
"""
