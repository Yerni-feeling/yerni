global cWidth
global cHeight
#cWidth and cHeight are the dimentions of the display
cWidth = 600
cHeight = 600
class player(object):
    def __init__(self):
        #x1 & y1 are the coordinate position of player 1, and x2 & y2 are similar for player 2  ---  we can change if to confusing
        self.x1 = 450
        self.y1 = 450
        self.x2 = 150
        self.y2 = 150
        #Below is just to help with the keys pressed 
        self.up = 0 
        self.down = 0
        self.left = 0
        self.right = 0
        self.W = 0
        self.S = 0
        self.A = 0
        self.D = 0
        #Each player has own speed so can be adjusted with speed boost
        self.speed1 = 3
        self.speed2 = 3
        #Player dimensions --- just while they are a shape and not an image
        self.h = 20
        self.w = 20
    #Creating the two players
    def player1(self):
        fill(0)
        rect(self.x1,self.y1,self.w,self.h)
    def player2(self):
        fill(0)
        rect(self.x2,self.y2,self.w,self.h)
        
    #Function for movement and boundary
    def update(self):
        #Player 1
        self.x1 = self.x1 + (self.right - self.left)*self.speed1
        self.y1 = self.y1 + (self.down - self.up)*self.speed1
        if not (self.x1 >= (cWidth // 2)):
            self.x1 = (cWidth // 2)
        if not (self.x1 <= (cWidth - self.w)):
            self.x1 = (cWidth - self.w)
        if not  (self.y1 >= 0):
            self.y1 = 0
        if not (self.y1 <= (cHeight - self.h)):
            self.y1 = (cHeight - self.h) 
        
        #Player 2     
        self.x2 = self.x2 + (self.D - self.A)*self.speed2
        self.y2 = self.y2 + (self.S - self.W)*self.speed2
        if not (self.x2 >= 0):
            self.x2 = 0
        if not (self.x2 <= ((cWidth // 2) - self.w)):
            self.x2 = ((cWidth // 2) - self.w)
        if not  (self.y2 >= 0):
            self.y2 = 0
        if not (self.y2 <= (cHeight - self.h)):
            self.y2 = (cHeight - self.h) 
        

def setup():
    size(cWidth,cHeight)
    global p
    p = player()
    
def draw():
    background(100)
    p.player1()
    p.player2()
    p.update()
    
def keyPressed():
    if keyCode == UP:
        p.up = 1
    if keyCode == DOWN:
        p.down = 1
    if keyCode == LEFT:
        p.left = 1
    if keyCode == RIGHT:
        p.right = 1
    
    if key == 'w':
        p.W = 1
    if key == 's':
        p.S = 1
    if key == 'a':
        p.A = 1
    if key == 'd':
        p.D = 1
        
def keyReleased():
    if keyCode == UP:
        p.up = 0
    if keyCode == DOWN:
        p.down = 0
    if keyCode == LEFT:
        p.left = 0
    if keyCode == RIGHT:
        p.right = 0
        
    if key == 'w':
        p.W = 0
    if key == 's':
        p.S = 0
    if key == 'a':
        p.A = 0
    if key == 'd':
        p.D = 0
