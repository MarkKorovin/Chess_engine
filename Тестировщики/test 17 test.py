class Pawn(object):
    def __init__(self):
        self

    def Moves(self, CL):
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
            
            coord = [CL[0]-1, CL[1]+1]
            if (coord[0]>=1 and coord[1]>=1):
                CL_NEW = Cell.A1(coord, changes)
                if (CL_NEW[2] == 'BLACK'):
                    moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
            else:
                coord =[]



        if (CL[2] == 'BLACK' and CL[3] == 'PAWN'):
            #пусть наша пешка стоит на поле A2, нам надо проверить поле A3
            coord = [CL[0], CL[1]-1]
            changes = []
            CL_NEW = Cell.A1(coord, changes)
            if (CL_NEW[3] == ''):
                moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                if (CL[1] == 7):
                    coord = [CL[0], CL[1]-2]
                    changes = []
                    CL_NEW = Cell.A1(coord, changes)
                    if (CL_NEW[3] == ''):
                        moves.append([CL[0], CL[1], CL_NEW[0], CL_NEW[1]])
                        
            coord = [CL[0]+1, CL[1]-1]
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
    def __init__(self, coord, changes):
        self.coord = coord
        self.changes = changes

    def A1(self):
        CL = [1, 1, 'WHITE', 'ROOK']
        if (self.coord == [1, 1]):
            if (self.changes != []):
                del CL[2:]
                CL.append(self.changes[0])
                CL.append(self.changes[1])

            return CL
        else:
            return Cell.A2(coord, changes)

    def A2(self):
        CL = [1, 2, 'WHITE', 'PAWN']
        if (coord == [1, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A3(coord, changes)

    def A3(self, coord, changes):
        CL = [1, 3, '', '']
        if (coord == [1, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A4(coord, changes)

    def A4(self, coord, changes):
        CL = [1, 4, '', '']
        if (coord == [1, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A5(coord, changes)

    def A5(self, coord, changes):
        CL = [1, 5, '', '']
        if (coord == [1, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A6(coord, changes)

    def A6(self, coord, changes):
        CL = [1, 6, '', '']
        if (coord == [1, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A7(coord, changes)

    def A7(self, coord, changes):
        CL = [1, 7, 'BLACK', 'PAWN']
        if (coord == [1, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A8(coord, changes)

    def A8(self, coord, changes):
        CL = [1, 8, 'BLACK', 'ROOK']
        if (coord == [1, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B1(coord, changes)

    def B1(self, coord, changes):
        CL = [2, 1, 'WHITE', 'KNIGHT']
        if (coord == [2, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B2(coord, changes)

    def B2(self, coord, changes):
        CL = [2, 2, 'WHITE', 'PAWN']
        if (coord == [2, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B3(coord, changes)

    def B3(self, coord, changes):
        CL = [2, 3, '', '']
        if (coord == [2, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B4(coord, changes)

    def B4(self, coord, changes):
        CL = [2, 4, '', '']
        if (coord == [2, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B5(coord, changes)

    def B5(self, coord, changes):
        CL = [2, 5, '', '']
        if (coord == [2, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B6(coord, changes)

    def B6(self, coord, changes):
        CL = [2, 6, '', '']
        if (coord == [2, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B7(coord, changes)

    def B7(self, coord, changes):
        CL = [2, 7, 'BLACK', 'PAWN']
        if (coord == [2, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B8(coord, changes)

    def B8(self, coord, changes):
        CL = [2, 8, 'BLACK', 'KNIGHT']
        if (coord == [2, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C1(coord, changes)

    def C1(self, coord, changes):
        CL = [3, 1, 'WHITE', 'BISHOP']
        if (coord == [3, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C2(coord, changes)

    def C2(self, coord, changes):
        CL = [3, 2, 'WHITE', 'PAWN']
        if (coord == [3, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C3(coord, changes)

    def C3(self, coord, changes):
        CL = [3, 3, '', '']
        if (coord == [3, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C4(coord, changes)

    def C4(self, coord, changes):
        CL = [3, 4, '', '']
        if (coord == [3, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C5(coord, changes)

    def C5(self, coord, changes):
        CL = [3, 5, '', '']
        if (coord == [3, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C6(coord, changes)

    def C6(self, coord, changes):
        CL = [3, 6, '', '']
        if (coord == [3, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C7(coord, changes)

    def C7(self, coord, changes):
        CL = [3, 7, 'BLACK', 'PAWN']
        if (coord == [3, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.C8(coord, changes)

    def C8(self, coord, changes):
        CL = [3, 8, 'BLACK', 'BISHOP']
        if (coord == [3, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D1(coord, changes)

    def D1(self, coord, changes):
        CL = [4, 1, 'WHITE', 'QUEEN']
        if (coord == [4, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D2(coord, changes)

    def D2(self, coord, changes):
        CL = [4, 2, 'WHITE', 'PAWN']
        if (coord == [4, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D3(coord, changes)

    def D3(self, coord, changes):
        CL = [4, 3, '', '']
        if (coord == [4, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D4(coord, changes)

    def D4(self, coord, changes):
        CL = [4, 4, '', '']
        if (coord == [4, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D5(coord, changes)

    def D5(self, coord, changes):
        CL = [4, 5, '', '']
        if (coord == [4, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D6(coord, changes)

    def D6(self, coord, changes):
        CL = [4, 6, '', '']
        if (coord == [4, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D7(coord, changes)

    def D7(self, coord, changes):
        CL = [4, 7, 'BLACK', 'PAWN']
        if (coord == [4, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.D8(coord, changes)

    def D8(self, coord, changes):
        CL = [4, 8, 'BLACK', 'QUEEN']
        if (coord == [4, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E1(coord, changes)

    def E1(self, coord, changes):
        CL = [5, 1, 'WHITE', 'KING']
        if (coord == [5, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E2(coord, changes)

    def E2(self, coord, changes):
        CL = [5, 2, 'WHITE', 'PAWN']
        if (coord == [5, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E3(coord, changes)

    def E3(self, coord, changes):
        CL = [5, 3, '', '']
        if (coord == [5, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E4(coord, changes)

    def E4(self, coord, changes):
        CL = [5, 4, '', '']
        if (coord == [5, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E5(coord, changes)

    def E5(self, coord, changes):
        CL = [5, 5, '', '']
        if (coord == [5, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E6(coord, changes)

    def E6(self, coord, changes):
        CL = [5, 6, '', '']
        if (coord == [5, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E7(coord, changes)

    def E7(self, coord, changes):
        CL = [5, 7, 'BLACK', 'PAWN']
        if (coord == [5, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.E8(coord, changes)

    def E8(self, coord, changes):
        CL = [5, 8, 'BLACK', 'KING']
        if (coord == [5, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F1(coord, changes)

    def F1(self, coord, changes):
        CL = [6, 1, 'WHITE', 'BISHOP']
        if (coord == [6, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F2(coord, changes)

    def F2(self, coord, changes):
        CL = [6, 2, 'WHITE', 'PAWN']
        if (coord == [6, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F3(coord, changes)

    def F3(self, coord, changes):
        CL = [6, 3, '', '']
        if (coord == [6, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F4(coord, changes)

    def F4(self, coord, changes):
        CL = [6, 4, '', '']
        if (coord == [6, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F5(coord, changes)

    def F5(self, coord, changes):
        CL = [6, 5, '', '']
        if (coord == [6, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F6(coord, changes)

    def F6(self, coord, changes):
        CL = [6, 6, '', '']
        if (coord == [6, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F7(coord, changes)

    def F7(self, coord, changes):
        CL = [6, 7, 'BLACK', 'PAWN']
        if (coord == [6, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.F8(coord, changes)

    def F8(self, coord, changes):
        CL = [6, 8, 'BLACK', 'BISHOP']
        if (coord == [6, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G1(coord, changes)

    def G1(self, coord, changes):
        CL = [7, 1, 'WHITE', 'KNIGHT']
        if (coord == [7, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G2(coord, changes)

    def G2(self, coord, changes):
        CL = [7, 2, 'WHITE', 'PAWN']
        if (coord == [7, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G3(coord, changes)

    def G3(self, coord, changes):
        CL = [7, 3, '', '']
        if (coord == [7, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G4(coord, changes)

    def G4(self, coord, changes):
        CL = [7, 4, '', '']
        if (coord == [7, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G5(coord, changes)

    def G5(self, coord, changes):
        CL = [7, 5, '', '']
        if (coord == [7, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G6(coord, changes)

    def G6(self, coord, changes):
        CL = [7, 6, '', '']
        if (coord == [7, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G7(coord, changes)

    def G7(self, coord, changes):
        CL = [7, 7, 'BLACK', 'PAWN']
        if (coord == [7, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.G8(coord, changes)

    def G8(self, coord, changes):
        CL = [7, 8, 'BLACK', 'KNIGHT']
        if (coord == [7, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H1(coord, changes)

    def H1(self, coord, changes):
        CL = [8, 1, 'WHITE', 'ROOK']
        if (coord == [8, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H2(coord, changes)

    def H2(self, coord, changes):
        CL = [8, 2, 'WHITE', 'PAWN']
        if (coord == [8, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H3(coord, changes)

    def H3(self, coord, changes):
        CL = [8, 3, '', '']
        if (coord == [8, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H4(coord, changes)

    def H4(self, coord, changes):
        CL = [8, 4, '', '']
        if (coord == [8, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H5(coord, changes)

    def H5(self, coord, changes):
        CL = [8, 5, '', '']
        if (coord == [8, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H6(coord, changes)

    def H6(self, coord, changes):
        CL = [8, 6, '', '']
        if (coord == [8, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H7(coord, changes)

    def H7(self, coord, changes):
        CL = [8, 7, 'BLACK', 'PAWN']
        if (coord == [8, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.H8(coord, changes)

    def H8(self, coord, changes):
        CL = [8, 8, 'BLACK', 'ROOK']
        if (coord == [8, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            raise Exception('TROUBLES WITH CODE!!!')

changes = []
CL = [8, 7, 'BLACK', 'PAWN']
print (Pawn.Moves(CL, CL))

