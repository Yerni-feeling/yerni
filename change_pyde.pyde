import random
import os
path = os.getcwd()
global cWidth
global cHeight
cWidth = 1400
cHeight = 1000
img_health=loadImage(path+"/images/"+"health1.png")
img_speed=loadImage(path+"/images/"+"speed.png")
img_shield=loadImage(path+"/images/"+"shield.png")

skills=[img_health, img_speed, img_shield]

skill1=random.randint(1,500)
skill2=random.randint(1,500)




class Game():
    def __init__(self):
        self.p1 = newPlayer(0)
        self.p2 = newPlayer(1)
        self.b0 = Barrier(0)
        self.b1 = Barrier(1)
        self.b2 = Barrier(2)
        self.b3 = Barrier(3)
        self.win = 3
        
        
    def display(self):
        if self.win == 0:
            self.p1.player()
            self.p2.player()
            self.p1.update()
            self.p2.update()
            self.p1.player1_side()
            self.p2.player2_side()
            self.check_hit()
            self.b0.check_for_display()
            self.b0.display()
            self.b1.check_for_display()
            self.b1.display()
            self.b2.check_for_display()
            self.b2.display()
            self.b3.check_for_display()
            self.b3.display()
            self.won()
            n = len(self.p1.a)
            g = len(self.p2.a)
            for t in range(n):
                self.p1.a[t].positionupdate()
                self.p1.a[t].display()
            for k in range(g):
                self.p2.a[k].positionupdate()
                self.p2.a[k].display()
                
        elif self.win == 3:
            background(0)
            textSize(30)
            if self.win == 3 and cWidth//2.5 < mouseX < cWidth//2.5 + 220 and cHeight//3 < mouseY < cHeight//3+50:
                fill(102,178,225)
            else:
                fill(225)
            text(" PLAY GAME ", cWidth//2.5+10, cHeight//3+40)
                
            fill(225)
            text(" How to play: Aim of the game, kill your opponent!\n Abilities, including extra health, force field and rapid fire, will pop up on the board.\n Pass over them to gain the abilities.\n Barriers to protect you will appear randomly on the display and disappear at random.\n P.S: Player 1 use WASD keys to move and V key to shoot.\n \t \t Player 2 use arrow keys to move and M key to shoot!", 70, cHeight//3+140)
            
        elif self.win == 1:
            background(0)
            textSize(30)
            fill(255,0,0)
            text("Player 1 has won!", cWidth//2.5+10, cHeight//2.5+10)
            
        
        elif self.win == 2:
            background(0)
            textSize(30)
            fill(255,0,0)
            text("Player 2 has won!", cWidth//2.5+10, cHeight//2.5+10)
            
            
    def check_hit(self):
        for i in self.p1.a:
            if (self.p2.x <= i.x) and (i.x <= self.p2.x + self.p2.w) and (self.p2.y <= i.y) and (i.y <= self.p2.y + self.p2.h):
                self.p2.healthbar.z -= 10
                self.p1.a.remove(i)
            elif (self.b0.x <= i.x) and (i.x <= self.b0.x + 10) and (self.b0.y <= i.y) and (i.y <= self.b0.y + self.b0.h):
                self.p1.a.remove(i)
            elif (self.b1.x <= i.x) and (i.x <= self.b1.x + 10) and (self.b1.y <= i.y) and (i.y <= self.b1.y + self.b1.h):
                self.p1.a.remove(i)
            elif (self.b2.x <= i.x) and (i.x <= self.b2.x + 10) and (self.b2.y <= i.y) and (i.y <= self.b2.y + self.b2.h):
                self.p1.a.remove(i)
            elif (self.b3.x <= i.x) and (i.x <= self.b3.x + 10) and (self.b3.y <= i.y) and (i.y <= self.b3.y + self.b3.h):
                self.p1.a.remove(i)
        
        for i in self.p2.a:
            if (self.p1.x <= i.x) and (i.x <= self.p1.x + self.p2.w) and (self.p1.y <= i.y) and (i.y <= self.p1.y +self.p1.h):
                self.p1.healthbar.z -= 10
                self.p2.a.remove(i)
            elif (self.b0.x <= i.x) and (i.x <= self.b0.x + 10) and (self.b0.y <= i.y) and (i.y <= self.b0.y + self.b0.h):
                self.p2.a.remove(i)
            elif (self.b1.x <= i.x) and (i.x <= self.b1.x + 10) and (self.b1.y <= i.y) and (i.y <= self.b1.y + self.b1.h):
                self.p2.a.remove(i)
            elif (self.b2.x <= i.x) and (i.x <= self.b2.x + 10) and (self.b2.y <= i.y) and (i.y <= self.b2.y + self.b2.h):
                self.p2.a.remove(i)
            elif (self.b3.x <= i.x) and (i.x <= self.b3.x + 10) and (self.b3.y <= i.y) and (i.y <= self.b3.y + self.b3.h):
                self.p2.a.remove(i)
                
                
    def won(self):
        if self.p1.healthbar.z == 0:
            self.win = 2
        elif self.p2.healthbar.z == 0:
            self.win = 1
            
    def mouse_click(self):
        if self.win == 3 and cWidth//2.5 < mouseX < cWidth//2.5 + 220 and cHeight//3 < mouseY < cHeight//3+50:
            self.win = 0

            
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
        self.h = 40
        self.w = 90
        self.img1 = loadImage(path+"/images/"+"spaceship1.png")



    def player(self):
        fill(0)
      #  rect(self.x, self.y, self.w, self.h)
        image(self.img1,self.x,self.y,self.w,self.h)
        self.healthbar.display()
        
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
        

class Barrier(object):
    def __init__(self, id):
        self.id = id
        self.w = 10
        self.h = 70
        self.x = random.randint(20, (cWidth-20))
        self.y = random.randint(20, (cHeight-120))
        self.display_wall = False
        self.start_display_frame = 0
        self.img = loadImage(path + "/images/barriers.png")
        
    def change_wall_position(self):
        self.h = 70
        self.x = random.randint(20, (cWidth-20))
        self.y = random.randint(20, (cHeight-120))

    def display(self):
        # image(self.img, sel.x, self.y)
        if frameCount - self.start_display_frame == 200:
            self.display_wall = False
        if self.display_wall:
            fill(0)
            rect(self.x, self.y, self.w, self.h)
            
    def check_for_display(self):
        if frameCount % random.randint(100, 500) == 0:
            self.display_wall = True
            self.change_wall_position()
            self.start_display_frame = frameCount
        

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
        
ability=skills[random.randint(0,2)]
a = Abilities(skill1,skill2,ability)
start_display_frame = 0

def setup():
    size(cWidth, cHeight)
    global game, barriers
    game = Game()
    

def draw():
    background(100)
    game.display()
    a.check_for_display()
    a.display()
    
    #if game.p1.x==a.x and game.p1.y==a.y:
        
    if (game.p1.x <= a.x) and (a.x <= game.p1.x + game.p1.w) and (game.p1.y <= a.y) and (a.y <= game.p1.y +game.p1.h):
        if a.ability==img_health:
            game.p1.healthbar.z+=1
        
        if a.ability==img_speed:
            game.p1.speed=14
    
        if a.ability==img_shield:
            game.p1.speed=14
        
    if (game.p2.x <= a.x) and (a.x <= game.p2.x + game.p2.w) and (game.p2.y <= a.y) and (a.y <= game.p2.y +game.p2.h):
        if a.ability==img_health:
            #game.p2.speed+=20
            game.p2.healthbar.z+=2
        
        if a.ability==img_speed:
            game.p2.speed=14
    
        if a.ability==img_shield:
            game.p2.speed=14

      
def mouseClicked():
    game.mouse_click()
    
    
def keyPressed():
    game.key_go()
    

def keyReleased():
    game.key_no()

#def mousePressed():
  #  if game.win==2 or game.win==1:
   #     game.win=3
        
