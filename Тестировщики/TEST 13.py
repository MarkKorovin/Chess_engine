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
        return Cell_info

    def A2(coord, changes):
        CL = ['A', 2, 'WHITE', 'PAWN']
        if (coord == ['A', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A3(coord, changes):
        CL = ['A', 3, '', '']
        if (coord == ['A', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A4(coord, changes):
        CL = ['A', 4, '', '']
        if (coord == ['A', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A5(coord, changes):
        CL = ['A', 5, '', '']
        if (coord == ['A', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A6(coord, changes):
        CL = ['A', 6, '', '']
        if (coord == ['A', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A7(coord, changes):
        CL = ['A', 7, 'BLACK', 'PAWN']
        if (coord == ['A', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def A8(coord, changes):
        CL = ['A', 8, 'BLACK', 'ROOK']
        if (coord == ['A', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info


    

    def H1(coord, changes):
        CL = ['H', 1, 'WHITE', 'ROOK']
        if (coord == ['H', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H2(coord, changes):
        CL = ['H', 2, 'WHITE', 'PAWN']
        if (coord == ['H', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H3(coord, changes):
        CL = ['H', 3, '', '']
        if (coord == ['H', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H4(coord, changes):
        CL = ['H', 4, '', '']
        if (coord == ['H', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H5(coord, changes):
        CL = ['H', 5, '', '']
        if (coord == ['H', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H6(coord, changes):
        CL = ['H', 6, '', '']
        if (coord == ['H', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H7(coord, changes):
        CL = ['H', 7, 'BLACK', 'PAWN']
        if (coord == ['H', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info

    def H8(coord, changes):
        CL = ['H', 8, 'BLACK', 'ROOK']
        if (coord == ['H', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
        Cell_info = [CL[2], CL[3]] 
        return Cell_info
