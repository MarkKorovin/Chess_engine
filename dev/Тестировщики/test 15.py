class Cell(object):
    def __init__(self):
        self

    def A1(coord, changes):
        CL = ['A', 1, 'WHITE', 'ROOK']
        if (coord == ['A', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            Cell_info = [CL[2], CL[3]] 
            return CL
        else:
            return Cell.A2(coord, changes)

    def A2(coord, changes):
        CL = ['A', 2, 'WHITE', 'ROOK']
        if (coord == ['A', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            Cell_info = [CL[2], CL[3]] 
            return CL
        else:
            return Cell.A3(coord, changes)
        
    def A3(coord, changes):
        CL = ['A', 3, '', '']
        if (coord == ['A', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            Cell_info = [CL[2], CL[3]] 
            return CL
        else:
            return Cell.A4(coord, changes)


            
changes = ['BLACK', 'BISHOP']
coord = ['A', 3]
print (Cell.A1(coord, changes))
