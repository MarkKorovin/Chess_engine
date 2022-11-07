class Cell(object):
    def __init__(self):
        self

    def A1(coord, changes):
        CL = ['A', 1, 'WHITE', 'ROOK']
        if (coord == ['A', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                СL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

changes = ['BLACK', 'BISHOP']
coord = ['A', 1]
print (Cell.A1(coord, changes))
