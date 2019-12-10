import os
path = os.getcwd()
global cWidth
global cHeight
# cWidth and cHeight are the dimentions of the display
cWidth = 1400
cHeight = 1000
class player(object):

    def __init__(self):
        # x1 & y1 are the coordinate position of player 1, and x2 & y2 are
        # similar for player 2  ---  we can change if to confusing
        self.a = []
        self.b = []
        self.x1 = 450
        self.y1 = 450
        self.x2 = 150
        self.y2 = 150
        self.h1 = 100
        self.h2 = 100
        # Below is just to help with the keys pressed
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.W = 0
        self.S = 0
        self.A = 0
        self.D = 0
        # Each player has own speed so can be adjusted with speed boost
        self.speed1 = 10
        self.speed2 = 10
        # Player dimensions --- just while they are a shape and not an image
        self.h = 20
        self.w = 20
    # Creating the two players

    def player1(self):
        fill(0)
        rect(self.x1, self.y1, self.w, self.h)

    def player2(self):
        fill(0)
        rect(self.x2, self.y2, self.w, self.h)

    # Function for movement and boundary
    def update(self):
        # Player 1
        self.x1 = self.x1 + (self.right - self.left) * self.speed1
        self.y1 = self.y1 + (self.down - self.up) * self.speed1
        if not (self.x1 >= (cWidth // 2)):
            self.x1 = (cWidth // 2)
        if not (self.x1 <= (cWidth - self.w)):
            self.x1 = (cWidth - self.w)
        if not (self.y1 >= 0):
            self.y1 = 0
        if not (self.y1 <= (cHeight - self.h)):
            self.y1 = (cHeight - self.h)

        # Player 2
        self.x2 = self.x2 + (self.D - self.A) * self.speed2
        self.y2 = self.y2 + (self.S - self.W) * self.speed2
        if not (self.x2 >= 0):
            self.x2 = 0
        if not (self.x2 <= ((cWidth // 2) - self.w)):
            self.x2 = ((cWidth // 2) - self.w)
        if not (self.y2 >= 0):
            self.y2 = 0
        if not (self.y2 <= (cHeight - self.h)):
            self.y2 = (cHeight - self.h)

    def shoot(self):
        self.a.append(Bullets(self.x1, self.y1, 0))

    def shoot1(self):
        self.b.append(Bullets(self.x2, self.y2, 1))

    def check_hit(self):
        for i in self.a:
            print(i)
            print(i.x)
            if self.x1 == i.x and self.y1 == i.y:
                print("HERE")
                
    # if self.x1==self.a[] and self.y1==self.a:
       # self.h1-=10

        pass
"""    def game_over(self):
        if self.h1=0:
            #
        if self.h2=0:
            #"""
    

class Barrier():

    def __init__(self, x, y, l, o, q, w, a, b):
        self.x = 100
        self.y = 100
        self.l = l
        self.o = o
        self.q = q
        self.w = w
        self.a = a
        self.b = b
        self.img = loadImage(path + "/images/barriers.png")

    def display(self):
        image(self.img, sel.x, self.y)

class Bullets:
    # x and y are starting coordinates and z dir

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 10
        self.h = 10

    def positionupdate(self):
        if self.z == 0:
            self.x -= 1 * 10
        if self.z == 1:
            self.x += 1 * 10

    def display(self):

        fill(0)
        rect(self.x, self.y, self.w, self.h)


class Abilities():
    # x-speed
    # y-shield
    # z-health

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class HealthBar1():
    # X-max health
    # y-health
    #z- Width

    def __init__(self):
        self.x = 100
        self.y = 100
        self.z = 200

    def display(self):
        if (self.x < 35):
            fill(255, 0, 0)
        else:
            fill(0, 255, 0)
        noStroke()
        delta = (self.y / self.x) * self.z
        rect(0, 0, delta, 20)
        stroke(0)
        noFill()
        rect(0, 0, self.z, 20)


class HealthBar2():
    # X-max health
    # y-health
    #z- Width

    def __init__(self):
        self.x = 100
        self.y = 100
        self.z = 200

    def display(self):
        if (self.x < 35):
            fill(255, 0, 0)
        else:
            fill(0, 255, 0)
        noStroke()
        delta = (self.y / self.x) * self.z
        rect(1200, 0, delta, 20)
        stroke(0)
        noFill()
        rect(1200, 0, self.z, 20)

        """
            # will end the game when one of the player will get zero health point
    def update(self):
        if self.x<=0: """


def setup():
    size(cWidth, cHeight)
    global p, healthbar1, healthbar2, barriers
    p = player()
    healthbar1 = HealthBar1()
    healthbar2 = HealthBar2()
  # barriers = Barrier()
    

    f

def draw():
    background(100)
    p.player1()
    p.player2()
    p.update()
    p.check_hit() #maybe not here
    n = len(p.a)
    g = len(p.b)
    for t in range(n):
        p.a[t].positionupdate()
        p.a[t].display()
    for k in range(g):
        p.b[k].positionupdate()
        p.b[k].display()

    healthbar1.display()
    healthbar2.display()
   # barriers.display()


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
    if key == 'm':
        p.shoot()
    if key == 'v':
        p.shoot1()


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
