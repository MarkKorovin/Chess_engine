class PAWN(object):
    def __init__(self, color):
        self.color = color
    def __repr__(self, color):
        if (color == 'WHITE'):
            return '♙'
        if (color == 'BLACK'):
            return '♟'

    
class ROOK(object):
    def __init__(self, color, x, y):
        self.color = color
    def __repr__(self):
        return('♖', '♜')[self.color]
        
        
class BISHOP(object):
    def __init__(self, color, x, y):
        self.color = color
        
    
class KING(object):
    def __init__(self, color, x, y):
        self.color = color

class QUEEN(object):
    def __init__(self, color, x, y):
        self.color = color

class KNIGHT(object):
    def __init__(self, color, x, y):
        self.color = color



class Cell(object):
    def __init__(self):
        self
    def A1 (changes):
        CL = ['A', '1', 'WHITE', 'ROOK', '♙']
        if (changes == []):
            Cell_info = [CL[2], CL[3], CL[4]]
            return Cell_info
        else:
            del CL[2:]
            #del name[x:] удаляет все элементы, начиная с х
            CL.append(changes[0])
            CL.append(changes[1])
            CL.append(changes[2])
            Cell_info = [CL[2], A2[3], A2[4]]
            return Cell_info
        
    def A2 (changes):
        CL = ['A', '2', 'WHITE', 'PAWN', '♙']
        if (changes == []):
            Cell_info = [CL[2], CL[3], CL[4]]
            return Cell_info
        else:
            del CL[2:]
            #del name[x:] удаляет все элементы, начиная с х
            CL.append(changes[0])
            CL.append(changes[1])
            CL.append(changes[2])
            Cell_info = [CL[2], CL[3], CL[4]]
            return Cell_info

    
changes = []
print(Cell.A2(changes))
