class Cell(object):
    def __init__(self):
        self
    def A1 (changes):
        CL = ['A', '1', 'WHITE', 'ROOK']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            #del name[x:] удаляет все элементы, начиная с х
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        
    def A2 (changes):
        CL = ['A', '2', 'WHITE', 'PAWN']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        
    def A3 (changes):
        CL = ['A', '3', '', '']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        
    def A4 (changes):
        CL = ['A', '4', '', '']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

    def A5 (changes):
        CL = ['A', '5', '', '']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

    def A6 (changes):
        CL = ['A', '6', '', '']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

    def A7 (changes):
        CL = ['A', '7', 'BLACK', 'PAWN']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

    def A8 (changes):
        CL = ['A', '8', 'BLACK', 'ROOK']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info


    def B1 (changes):
        CL = ['B', '1', 'WHITE', 'KNIGHT']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

   def B2 (changes):
        CL = ['B', '2', 'WHITE', 'PAWN']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

   def B3 (changes):
        CL = ['B', '3', '', '']
        if (changes == []):
            Cell_info = [CL[2], CL[3]]
            return Cell_info
        else:
            del CL[2:]
            CL.append(changes[0])
            CL.append(changes[1])
            Cell_info = [CL[2], CL[3]]
            return Cell_info

    def B4 (changes):
            CL = ['B', '4', '', '']
            if (changes == []):
                Cell_info = [CL[2], CL[3]]
                return Cell_info
            else:
                del CL[2:]
                CL.append(changes[0])
                CL.append(changes[1])
                Cell_info = [CL[2], CL[3]]
                return Cell_info






