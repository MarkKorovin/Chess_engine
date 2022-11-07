def A2 (changes):
    A2 = ['A', '2', 'WHITE', 'PAWN', '♙']
    if (changes == []):
        Cell_info = [A2[2], A2[3], A2[4]]
        return Cell_info
    else:
        del A2[2:]
        #del name[x:] удаляет все элементы, начиная с х
        A2.append(changes[0])
        A2.append(changes[1])
        A2.append(changes[2])
        Cell_info = [A2[2], A2[3], A2[4]]
        return Cell_info

changes = ['BLACK', 'ROOK', '♜']
print (A2(changes))
