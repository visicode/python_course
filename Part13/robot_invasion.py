# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()


class Robot:
    def __init__(self):
        self.x=random.randint(0,ww-rw)
        self.y=-rh
        self.vx=0
        self.vy=v #start speed is falling

    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        if self.y>=(wh-rh) and self.vy>0:
            self.vy=0
            if self.x>ww//2:
                self.vx=v
            else:
                self.vx=-v

    def __str__(self):
        return f"x:{self.x},y:{self.y}"
    
class RobotArmy:
    
    def __init__(self):
        self.robots=[]
        self.max_r = 20 #Do not create more than this

    def create_robot(self):
        if len(self.robots)<self.max_r:
            self.robots.append(Robot())

    def check_robot_remove(self):
        res=[]
        for robi in self.robots:
            if (0-rw)<robi.x<ww: #still inside of the window
                res.append(robi)
        self.robots=res

    def move_robots(self):
        for robi in self.robots:
            #print(robi)
            robi.move()

    def draw_robots(self):
        for robi in self.robots:
            window.blit(robot, (robi.x, robi.y))

    def __str__(self):
        return f"Robots exists: {len(self.robots)}"
        


v = 2 #speed of robots
mingen = 8
maxgen = 50 #how often to create robots
ra = RobotArmy()

clock = pygame.time.Clock()
last_robi = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    if last_robi == 0:
        ra.create_robot()
        last_robi = random.randint(mingen,maxgen)

    ra.move_robots()
    ra.draw_robots()
    ra.check_robot_remove()
    
    pygame.display.flip()

    #print(ra)

    last_robi-=1
    clock.tick(60)