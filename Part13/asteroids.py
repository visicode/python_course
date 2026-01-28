# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
robotw = robot.get_width()
roboth = robot.get_height()
rockw = rock.get_width()
rockh = rock.get_height()
ww = window.get_width()
wh = window.get_height()
v=1 #rock fall speed


class Rock:
    def __init__(self):
        self.x=random.randint(0,ww-rockw)
        self.y=-rockh
        self.vy=v 

    def move(self):
        self.y+=self.vy

    def __str__(self):
        return f"x:{self.x},y:{self.y}"
    
class RockArmy:    
    def __init__(self):
        self.rocks=[]
        self.max_r = 20 #Do not create more than this
        self.point=0

    def create_rock(self):
        if len(self.rocks)<self.max_r:
            self.rocks.append(Rock())

    def check_rock_point(self,robox:int, roboy:int)->int:
        res=[]
        for rocki in self.rocks:
            if roboy<(rocki.y+rockh)<wh and robox<(rocki.x+rockw) and rocki.x<(robox+robotw): #collision
                self.point+=1
            else:
                res.append(rocki) #no collision with this rock - draw it again
        self.rocks=res
        return self.point
    
    def check_rock_overflow(self)->bool:
        for rocki in self.rocks:
            if rocki.y+rockh>wh:
                return True
        return False

    def move_rocks(self):
        for rocki in self.rocks:
            rocki.move()

    def draw_rocks(self):
        for rocki in self.rocks:
            window.blit(rock, (rocki.x, rocki.y))

    def __str__(self):
        return f"Rocks exists: {len(self.rocks)}"
        

tick=50 #fps
mingen = 60
maxgen = 90 #how often to create rocks
ra = RockArmy()
rx=(ww-robotw)/2 #robot coordinates
ry=wh-roboth
to_right = False
to_left = False
clock = pygame.time.Clock()
last_rock = 0 #how many frames to wait to create a new rock

pygame.display.set_caption(f"Asteroids")
game_font = pygame.font.SysFont("Arial", 24)
was_increased=True #Increase difficulty

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    window.fill((0, 0, 0))

    #add new rock when timer 0
    if last_rock == 0:
        ra.create_rock()
        last_rock = random.randint(mingen,maxgen)
        was_increased=False

    ra.move_rocks()
    ra.draw_rocks()

    if to_right and rx+robotw<ww: #move robot
        rx += 4*v
    if to_left and rx>0:
        rx -= 4*v
    window.blit(robot, (rx, ry))

    points=ra.check_rock_point(rx,ry) #write points
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (ww-150, 40))

    if ra.check_rock_overflow(): #check endgame
        print(f"Final point was: {points}") #have some memory for the gamer ;-)
        exit()
    
    pygame.display.flip()
    #increase difficulty level by every 20 points 
    if points%20==0 and was_increased==False and points>0:
        tick+=10
        was_increased=True

    last_rock-=1
    clock.tick(tick)