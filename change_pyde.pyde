import random
import os
path = os.getcwd()
global cWidth
global cHeight
cWidth = 1400
cHeight = 1000


class Game():
    def __init__(self):
        self.p1 = newPlayer(0)
        self.p2 = newPlayer(1)
        self.barrier_x = random.randint(0, cWidth)
        self.barrier_y = random.randint(0, cHeight)
        self.barrier_height = random.randint(20, (cHeight//10))
        self.b = Barrier(self.barrier_x, self.barrier_y, self.barrier_height)
        self.win = 0
        
    def display(self):
        if self.win == 0:
            self.p1.player()
            self.p2.player()
            self.p1.update()
            self.p2.update()
            self.p1.player1_side()
            self.p2.player2_side()
            self.check_hit()
            self.b.display()
            self.won()
            n = len(self.p1.a)
            g = len(self.p2.a)
            for t in range(n):
                self.p1.a[t].positionupdate()
                self.p1.a[t].display()
            for k in range(g):
                self.p2.a[k].positionupdate()
                self.p2.a[k].display()
            
        elif self.win == 1:
            text("Player 1 has won!", 600, 400)
            textSize(26);
            
        
        elif self.win == 2:
            text("Player 2 has won!", 600, 400)
            textSize(26);
            
    # def barrier_appear(self, barrier_x, barrier_y):
        
            
    def check_hit(self):
        for i in self.p1.a:
            print(i)
            print(i.x)
            if (self.p2.x <= i.x) and (i.x <= self.p2.x + self.p2.w) and (self.p2.y <= i.y) and (i.y <= self.p2.y +self.p2.h):
                # self.b.remove()
                self.p2.healthbar.z -= 10
        
        for i in self.p2.a:
            print(i)
            print(i.x)
            if (self.p1.x <= i.x) and (i.x <= self.p1.x + self.p2.w) and (self.p1.y <= i.y) and (i.y <= self.p1.y +self.p1.h):
                # self.b.remove()
                self.p1.healthbar.z -= 10
                
                
    def won(self):
        if self.p1.healthbar.z == 0:
            self.win = 2
        elif self.p2.healthbar.z == 0:
            self.win = 1

            
    def key_go(self):
        if keyCode == UP:
            self.p2.up = 1
        if keyCode == DOWN:
            self.p2.down = 1
        if keyCode == LEFT:
            self.p2.left = 1
        if keyCode == RIGHT:
            self.p2.right = 1
    
        if key == 'w':
            self.p1.up = 1
        if key == 's':
            self.p1.down = 1
        if key == 'a':
            self.p1.left = 1
        if key == 'd':
            self.p1.right = 1
            
        if key == 'm':
            self.p2.shoot()
        if key == 'v':
            self.p1.shoot()
    
    
    def key_no(self):
        if keyCode == UP:
            self.p2.up = 0
        if keyCode == DOWN:
            self.p2.down = 0
        if keyCode == LEFT:
            self.p2.left = 0
        if keyCode == RIGHT:
            self.p2.right = 0
    
        if key == 'w':
            self.p1.up = 0
        if key == 's':
            self.p1.down = 0
        if key == 'a':
            self.p1.left = 0
        if key == 'd':
            self.p1.right = 0
            
        


class newPlayer(object):
    def __init__(self, id):
        self.a = []
        self.b = []
        self.id = id
        if (id == 0):
            self.x = cWidth*1/4
            self.y = cHeight*1/4
            self.healthbar = HealthBar(0)
        else:
            self.x = cWidth*3/4
            self.y = cHeight*3/4
            self.healthbar = HealthBar(1200)
            
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.speed = 10
        self.h = 20
        self.w = 20


    def player(self):
        fill(0)
        rect(self.x, self.y, self.w, self.h)
        self.healthbar.display()
        
    # Function for movement and boundary
    def update(self):

        self.x = self.x + (self.right - self.left) * self.speed
        self.y = self.y + (self.down - self.up) * self.speed
        
    def player1_side(self):
            if not (self.x >= 0):
                self.x = 0
            if not (self.x <= ((cWidth // 2) - self.w)):
                self.x = ((cWidth // 2) - self.w)
            if not (self.y >= 0):
                self.y = 0
            if not (self.y <= (cHeight - self.h)):
                self.y = (cHeight - self.h)
        
    def player2_side(self):
            if not (self.x >= (cWidth // 2)):
                self.x = (cWidth // 2)
            if not (self.x <= (cWidth - self.w)):
                self.x = (cWidth - self.w)
            if not (self.y >= 0):
                self.y = 0
            if not (self.y <= (cHeight - self.h)):
                self.y = (cHeight - self.h)

    def shoot(self):
        self.a.append(Bullets(self.x, self.y, self.id))
        
            
# class game():
        

class Barrier(object):
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.w = 10
        self.h = h
        self.img = loadImage(path + "/images/barriers.png")

    def display(self):
        # image(self.img, sel.x, self.y)
        rect(self.x, self.y, self.w, self.h)

class Bullets(object):
    # x and y are starting coordinates and z dir

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 10
        self.h = 10

    def positionupdate(self):
        if self.z == 1:
            self.x -= 1 * 10
        if self.z == 0:
            self.x += 1 * 10
            
    def remove_bullet(self):
        if self.x<0 or self.y<0 or self.x>cWidth or self.y>cHeight:
            self.a.remove()
            
    def display(self):
        fill(0)
        rect(self.x, self.y, self.w, self.h)


class Abilities(object):
    # x-speed
    # y-shield
    # z-health

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class HealthBar(object):
    # X-max health
    # y-health
    # z-Width

    def __init__(self, h):
        self.x = 100
        self.y = 100
        self.z = 200
        self.h = h

    def display(self):
        if (self.x < 35):
            fill(255, 0, 0)
        else:
            fill(0, 255, 0)
        noStroke()
        delta = (self.y / self.x) * self.z
        rect(self.h, 0, self.z, 20)
        stroke(0)
        noFill()
        rect(self.h, 0, self.z, 20)

        """
            # will end the game when one of the player will get zero health point
    def update(self):
        if self.x<=0: """


def setup():
    size(cWidth, cHeight)
    global game, barriers
    game = Game()

  # barriers = Barrier()
    

def draw():
    background(100)
    game.display()
    
    
    
def keyPressed():
    game.key_go()
    

def keyReleased():
    game.key_no()

   # barriers.display()
