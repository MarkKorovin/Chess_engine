class Cell(object):
    CL = None
    
    def __init__(self, changes):
        self.changes = changes
        
    def info (self, changes):
        if (changes == []):
            Cell_info = [CL[2], CL[3], CL[4]]
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            CL.append(changes[2])
            Cell_info = [CL[2], A2[3], A2[4]]
            return Cell_info
class A1(Cell):
    CL = ['A', '1', 'WHITE', 'PAWN', '♙']

changes = ['BLACK', 'ROOK', '♜']
print(A1(changes))
