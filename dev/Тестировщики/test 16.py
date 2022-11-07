class Pawn(object):
    def __init__(self):
        self

    def Moves(CL):
        moves = []
        if (CL[2] == 'WHITE' and CL[3] == 'PAWN'):
            #пусть наша пешка стоит на поле A2, нам надо проверить поле A3
            coord = [CL[0], CL[1]+1]
            changes = []
            CL_NEW = Cell.A1(coord, changes)
            if (CL_NEW[3] == ''):
                moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                if (CL[1] == 2):
                    coord = [CL[0], CL[1]+2]
                    changes = []
                    CL_NEW = Cell.A1(coord, changes)
                    if (CL_NEW[3] == ''):
                        moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                        
            coord = [CL[0]+1, CL[1]+1]
            if (coord[0]<=8 and coord[1]<=8):
                CL_NEW = Cell.A1(coord, changes)
                if (CL_NEW[2] == 'BLACK'):
                    moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
            else:
                coord =[]
            
            coord = [CL[0]-1, CL[1]-1]
            if (coord[0]>=1 and coord[1]>=1):
                CL_NEW = Cell.A1(coord, changes)
                if (CL_NEW[2] == 'BLACK'):
                    moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
            else:
                coord =[]


        if (CL[2] == 'BLACK' and CL[3] == 'PAWN'):
            #пусть наша пешка стоит на поле A2, нам надо проверить поле A3
            coord = [CL[0], CL[1]+1]
            changes = []
            CL_NEW = Cell.A1(coord, changes)
            if (CL_NEW[3] == ''):
                moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                if (CL[1] == 2):
                    coord = [CL[0], CL[1]+2]
                    changes = []
                    CL_NEW = Cell.A1(coord, changes)
                    if (CL_NEW[3] == ''):
                        moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                        
            coord = [CL[0]+1, CL[1]+1]
            if (coord[0]<=8 and coord[1]<=8):
                CL_NEW = Cell.A1(coord, changes)
                if (CL_NEW[2] == 'WHITE'):
                    moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
            else:
                coord =[]
            
            coord = [CL[0]-1, CL[1]-1]
            if (coord[0]>=1 and coord[1]>=1):
                CL_NEW = Cell.A1(coord, changes)
                if (CL_NEW[2] == 'WHITE'):
                    moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
            else:
                coord =[]

        return moves


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

            return CL
        else:
            return Cell.A2(coord, changes)

    def A2(coord, changes):
        CL = ['A', 2, 'WHITE', 'PAWN']
        if (coord == ['A', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
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
            return CL
        else:
            return Cell.A4(coord, changes)

    def A4(coord, changes):
        CL = ['A', 4, '', '']
        if (coord == ['A', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A5(coord, changes)

    def A5(coord, changes):
        CL = ['A', 5, '', '']
        if (coord == ['A', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A6(coord, changes)

    def A6(coord, changes):
        CL = ['A', 6, '', '']
        if (coord == ['A', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A7(coord, changes)

    def A7(coord, changes):
        CL = ['A', 7, 'BLACK', 'PAWN']
        if (coord == ['A', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A8(coord, changes)

    def A8(coord, changes):
        CL = ['A', 8, 'BLACK', 'ROOK']
        if (coord == ['A', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B1(coord, changes)

    def B1(coord, changes):
        CL = ['B', 1, 'WHITE', 'KNIGHT']
        if (coord == ['B', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B2(coord, changes)

    def B2(coord, changes):
        CL = ['B', 2, 'WHITE', 'PAWN']
        if (coord == ['B', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B3(coord, changes)

    def B3(coord, changes):
        CL = ['B', 3, '', '']
        if (coord == ['B', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B4(coord, changes)

    def B4(coord, changes):
        CL = ['B', 4, '', '']
        if (coord == ['B', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B5(coord, changes)

    def B5(coord, changes):
        CL = ['B', 5, '', '']
        if (coord == ['B', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B6(coord, changes)

    def B6(coord, changes):
        CL = ['B', 6, '', '']
        if (coord == ['B', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B7(coord, changes)

    def B7(coord, changes):
        CL = ['B', 7, 'BLACK', 'PAWN']
        if (coord == ['B', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B8(coord, changes)

    def B8(coord, changes):
        CL = ['B', 8, 'BLACK', 'KNIGHT']
        if (coord == ['B', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C1(coord, changes)

    def C1(coord, changes):
        CL = ['C', 1, 'WHITE', 'BISHOP']
        if (coord == ['C', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C2(coord, changes)

    def C2(coord, changes):
        CL = ['C', 2, 'WHITE', 'PAWN']
        if (coord == ['C', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C3(coord, changes)

    def C3(coord, changes):
        CL = ['C', 3, '', '']
        if (coord == ['C', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C4(coord, changes)

    def C4(coord, changes):
        CL = ['C', 4, '', '']
        if (coord == ['C', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C5(coord, changes)

    def C5(coord, changes):
        CL = ['C', 5, '', '']
        if (coord == ['C', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C6(coord, changes)

    def C6(coord, changes):
        CL = ['C', 6, '', '']
        if (coord == ['C', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C7(coord, changes)

    def C7(coord, changes):
        CL = ['C', 7, 'BLACK', 'PAWN']
        if (coord == ['C', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C8(coord, changes)

    def C8(coord, changes):
        CL = ['C', 8, 'BLACK', 'BISHOP']
        if (coord == ['C', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D1(coord, changes)

    def D1(coord, changes):
        CL = ['D', 1, 'WHITE', 'QUEEN']
        if (coord == ['D', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D2(coord, changes)

    def D2(coord, changes):
        CL = ['D', 2, 'WHITE', 'PAWN']
        if (coord == ['D', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D3(coord, changes)

    def D3(coord, changes):
        CL = ['D', 3, '', '']
        if (coord == ['D', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D4(coord, changes)

    def D4(coord, changes):
        CL = ['D', 4, '', '']
        if (coord == ['D', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D5(coord, changes)

    def D5(coord, changes):
        CL = ['D', 5, '', '']
        if (coord == ['D', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D6(coord, changes)

    def D6(coord, changes):
        CL = ['D', 6, '', '']
        if (coord == ['D', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D7(coord, changes)

    def D7(coord, changes):
        CL = ['D', 7, 'BLACK', 'PAWN']
        if (coord == ['D', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D8(coord, changes)

    def D8(coord, changes):
        CL = ['D', 8, 'BLACK', 'QUEEN']
        if (coord == ['D', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E1(coord, changes)

    def E1(coord, changes):
        CL = ['E', 1, 'WHITE', 'KING']
        if (coord == ['E', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E2(coord, changes)

    def E2(coord, changes):
        CL = ['E', 2, 'WHITE', 'PAWN']
        if (coord == ['E', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E3(coord, changes)

    def E3(coord, changes):
        CL = ['E', 3, '', '']
        if (coord == ['E', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E4(coord, changes)

    def E4(coord, changes):
        CL = ['E', 4, '', '']
        if (coord == ['E', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E5(coord, changes)

    def E5(coord, changes):
        CL = ['E', 5, '', '']
        if (coord == ['E', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E6(coord, changes)

    def E6(coord, changes):
        CL = ['E', 6, '', '']
        if (coord == ['E', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E7(coord, changes)

    def E7(coord, changes):
        CL = ['E', 7, 'BLACK', 'PAWN']
        if (coord == ['E', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E8(coord, changes)

    def E8(coord, changes):
        CL = ['E', 8, 'BLACK', 'KING']
        if (coord == ['E', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F1(coord, changes)

    def F1(coord, changes):
        CL = ['F', 1, 'WHITE', 'BISHOP']
        if (coord == ['F', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F2(coord, changes)

    def F2(coord, changes):
        CL = ['F', 2, 'WHITE', 'PAWN']
        if (coord == ['F', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F3(coord, changes)

    def F3(coord, changes):
        CL = ['F', 3, '', '']
        if (coord == ['F', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F4(coord, changes)

    def F4(coord, changes):
        CL = ['F', 4, '', '']
        if (coord == ['F', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F5(coord, changes)

    def F5(coord, changes):
        CL = ['F', 5, '', '']
        if (coord == ['F', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F6(coord, changes)

    def F6(coord, changes):
        CL = ['F', 6, '', '']
        if (coord == ['F', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F7(coord, changes)

    def F7(coord, changes):
        CL = ['F', 7, 'BLACK', 'PAWN']
        if (coord == ['F', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F8(coord, changes)

    def F8(coord, changes):
        CL = ['F', 8, 'BLACK', 'BISHOP']
        if (coord == ['F', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G1(coord, changes)

    def G1(coord, changes):
        CL = ['G', 1, 'WHITE', 'KNIGHT']
        if (coord == ['G', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G2(coord, changes)

    def G2(coord, changes):
        CL = ['G', 2, 'WHITE', 'PAWN']
        if (coord == ['G', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G3(coord, changes)

    def G3(coord, changes):
        CL = ['G', 3, '', '']
        if (coord == ['G', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G4(coord, changes)

    def G4(coord, changes):
        CL = ['G', 4, '', '']
        if (coord == ['G', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G5(coord, changes)

    def G5(coord, changes):
        CL = ['G', 5, '', '']
        if (coord == ['G', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G6(coord, changes)

    def G6(coord, changes):
        CL = ['G', 6, '', '']
        if (coord == ['G', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G7(coord, changes)

    def G7(coord, changes):
        CL = ['G', 7, 'BLACK', 'PAWN']
        if (coord == ['G', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G8(coord, changes)

    def G8(coord, changes):
        CL = ['G', 8, 'BLACK', 'KNIGHT']
        if (coord == ['G', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H1(coord, changes)

    def H1(coord, changes):
        CL = ['H', 1, 'WHITE', 'ROOK']
        if (coord == ['H', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H2(coord, changes)

    def H2(coord, changes):
        CL = ['H', 2, 'WHITE', 'PAWN']
        if (coord == ['H', 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H3(coord, changes)

    def H3(coord, changes):
        CL = ['H', 3, '', '']
        if (coord == ['H', 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H4(coord, changes)

    def H4(coord, changes):
        CL = ['H', 4, '', '']
        if (coord == ['H', 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H5(coord, changes)

    def H5(coord, changes):
        CL = ['H', 5, '', '']
        if (coord == ['H', 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H6(coord, changes)

    def H6(coord, changes):
        CL = ['H', 6, '', '']
        if (coord == ['H', 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H7(coord, changes)

    def H7(coord, changes):
        CL = ['H', 7, 'BLACK', 'PAWN']
        if (coord == ['H', 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H8(coord, changes)

    def H8(coord, changes):
        CL = ['H', 8, 'BLACK', 'ROOK']
        if (coord == ['H', 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            raise Exception('TROUBLES WITH CODE!!!')



CL = [1, 2, 'WHITE', 'PAWN']
print (Pawn.Moves(CL))
