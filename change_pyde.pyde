import random
import os
path = os.getcwd()
global cWidth
global cHeight
cWidth = 1400
cHeight = 1000

img_health=loadImage(path+"/images/"+"health.png")
img_speed=loadImage(path+"/images/"+"speed.png")
img_shield=loadImage(path+"/images/"+"shield.png")

skills=[img_health, img_speed, img_shield]

skill1=random.randint(1,500)
skill2=random.randint(1,500)



class Game():
    def __init__(self):
        self.p1 = newPlayer(0)
        self.p2 = newPlayer(1)
        self.barrier_x = random.randint(0, cWidth)
        self.barrier_y = random.randint(0, cHeight)
        self.barrier_height = random.randint(20, (cHeight//10))
        self.b = Barrier(self.barrier_x, self.barrier_y, self.barrier_height)
        self.win = 0
    """    self.blocks=[] 
for i in range(7):
            a=random.randint()
            b=random.randint()
            
            self.blocks.append(Barrier())"""
                
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
            textSize(32)
            
        
        elif self.win == 2:
            text("Player 2 has won!", 600, 400)
            textSize(32)
            
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
        fill(255)
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

    def __init__(self, x, y,ability):
        self.x = x
        self.y = y
        self.ability=ability
        self.display_ability = False
        self.start_display_frame = 0

    def change_abilitity_position(self):
        self.ability=skills[random.randint(0,2)]
        self.x = random.randint(100,1000)
        self.y = random.randint(100,1000)
        
    def display(self):
        if frameCount - self.start_display_frame == 100:
            self.display_ability = False
        if self.display_ability:
            image(self.ability,self.x,self.y, 40, 40)
            
    def check_for_display(self):
        if frameCount % 200 == 0:
            self.display_ability = True
            self.change_abilitity_position()
            self.start_display_frame = frameCount


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
    global game, barriers, img1
    game = Game()
   # img1= loadImage(path+"/images/"+"backgroundimage.png")

  # barriers = Barrier()
ability=skills[random.randint(0,2)]
a = Abilities(skill1,skill2,ability)


def draw():
    global img1
    background(100)
  #  image(img1,0,0,1400,1000)

    game.display()
    a.check_for_display()
    a.display()

    # if p.update(self.x)==a.position(self.x):
    #     if a.ability==img_health1:
    #         p.newPlayer.self.healthbar+=10        
    #     if a.ability == img_speed:
    #         p.update.self.speed+=10    
    #     if a.ability == img_shield:
    #         p.newPlayer.self.healthbar+=1000
            
            
        
        
    
    
#   if position of ability and player equals
#    if speed img 

    # if health and if shjield

    
    
    
    
def keyPressed():
    game.key_go()
    

def keyReleased():
    game.key_no()

   # barriers.display()
#restart
