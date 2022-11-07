class Pawn(object):
    def __init__(self, CL):
        self.CL = CL

    def Moves(self):
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
        if (coord == [1, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])

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

    def A3(self):
        CL = [1, 3, '', '']
        if (coord == [1, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A4(coord, changes)

    def A4(self):
        CL = [1, 4, '', '']
        if (coord == [1, 4]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A5(coord, changes)

    def A5(self):
        CL = [1, 5, '', '']
        if (coord == [1, 5]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A6(coord, changes)

    def A6(self):
        CL = [1, 6, '', '']
        if (coord == [1, 6]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A7(coord, changes)

    def A7(self):
        CL = [1, 7, 'BLACK', 'PAWN']
        if (coord == [1, 7]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.A8(coord, changes)

    def A8(self):
        CL = [1, 8, 'BLACK', 'ROOK']
        if (coord == [1, 8]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B1(coord, changes)

    def B1(self):
        CL = [2, 1, 'WHITE', 'KNIGHT']
        if (coord == [2, 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B2(coord, changes)

    def B2(self):
        CL = [2, 2, 'WHITE', 'PAWN']
        if (coord == [2, 2]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B3(coord, changes)

    def B3(self):
        CL = [2, 3, '', '']
        if (coord == [2, 3]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            return CL
        else:
            return Cell.B4(coord, changes)


changes = []
CL = [8, 7, 'BLACK', 'PAWN']
print (Pawn.Moves(CL))

