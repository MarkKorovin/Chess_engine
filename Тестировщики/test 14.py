class Cell(object):
    def __init__(self, coord, Cellinfo):
        self.coord = coord
        self.Cellinfo = Cellinfo

    def __str__(self):
        return self.Cellinfo

    def A1(self, changes, coord, Cellinfo):
        CL = ['A', 1, 'WHITE', 'ROOK']
        if (coord == ['A', 1]):
            if (changes != []):
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
            Cellinfo = [CL[2], CL[3]]
            return Cellinfo
        else:
            Cell.A2

changes = []
Cellinfor = []
coordinates = ['A', 1]
print(Cell.A1(changes, coordinates, Cellinfor))

