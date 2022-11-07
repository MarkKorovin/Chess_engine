def PIECE_VALUE (PIECE):
    PAWN_VALUE = 1.00
    KNIGHT_VALUE = 3.05
    BISHOP_VALUE = 3.33
    ROOK_VALUE = 5.63
    QUEEN_VALUE = 9.5
    KING_VALUE = 100.00
    if (PIECE == 'BLACK_PAWN' or PIECE == 'WHITE_PAWN'):
        VALUE = PAWN_VALUE
    else:
        if (PIECE == 'BLACK_KNIGHT' or PIECE == 'WHITE_KNIGHT'):
            VALUE = KNIGHT_VALUE
        else:
            if (PIECE == 'BLACK_BISHOP' or PIECE == 'WHITE_BISHOP'):
                VALUE = BISHOP_VALUE
            else:
                if (PIECE == 'BLACK_ROOK' or PIECE == 'WHITE_ROOK'):
                    VALUE = ROOK_VALUE
                else:
                    if (PIECE == 'BLACK_QUEEN' or PIECE == 'WHITE_QUEEN'):
                        VALUE = QUEEN_VALUE
                    else:
                        if (PIECE == 'BLACK_KING' or PIECE == 'WHITE_KING'):
                            VALUE = KING_VALUE
                        else:
                            VALUE = 0.0
    
    return VALUE
    '''
Значения стоимости фигур даны в сантипешках. Точные значения взяты из
https://xchess.ru/alfa-zero-vladimir-kramnik-i-izobretenie-novykh-shakhmat.html

Цена короля взята примерно 100, возможно и увеличение стоимости до 400.
'''
    '''
ДЛЯ ОТЛАДКИ

n = 0
while (True):
    PIECE = input(' ')
    VALUE = PIECE_VALUE (PIECE)
    print (VALUE)
    '''
    
