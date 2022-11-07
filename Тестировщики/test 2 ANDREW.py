class figure:
    x=0
    y=0
    c = ''
     def __init__(self, _x, _y, _c):
        self.x = _x
        self.y = _y
        self.c = _c
    
    def moveTo(self):
        return 0
    
    def getCoords(self):
        return self.x*10+self.y
    
class peshka(figure):
    def moveTo(self, _xn, _yn):
        if self.c=='w':
            if self.x==_xn and _yn<=8 and (_yn-self.y==1 or (_yn-self.y==2 and self.y==2)):
                self.x=_xn
                self.y=_yn
                return 1
            else:
                
                return 0
        else:
            if self.x==_xn and _yn>=1 and (_yn-self.y==-1 or (_yn-self.y==-2 and self.y==7)):
                self.x=_xn
                self.y=_yn
                return 1
            else:
                return 0
FIELD = [[],[],[],[],[],[],[],[]]
for i in range(8):
    FIELD[i] = ["NONE", "NONE","NONE","NONE","NONE","NONE","NONE","NONE"]

xs=1
ys=2
f = peshka(xs, ys, 'w')
FIELD[xs][ys] = f
print(f.getCoords())
xd = 1
yd = 3
if(f.moveTo(xd, yd)==1):
    FIELD[xd][yd] =f
else:
    print("FUCK YOU, SIR!")
print(f.getCoords())
print(FIELD[1][2])
