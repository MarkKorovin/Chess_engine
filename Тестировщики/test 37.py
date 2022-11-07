class Pawn(object):
    def __init__(self, color, x, y, defence=0):
        self.color = color
        self.x = x
        self.y = y
        self.defence = defence
        

Pawn('White', 4, 3)
