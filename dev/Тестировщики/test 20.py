class Board (object):
    def __init__ (self):
        self.Board = [['.']*8 for y in range (8)]
        self.Board[0][0] = 'BOO'
    

    def __str__(self):        
        res = ''
        for y in range(8):
            res += ''.join(map(str, self.Board[y])) + "\n"
        return res

print(Board())
 
