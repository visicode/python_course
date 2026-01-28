# WRITE YOUR SOLUTION HERE:
import pygame,random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

ww = window.get_width()
wh = window.get_height()
rw = robot.get_width()
rh= robot.get_height()
#print (rw,rh)

window.fill((0, 0, 0))

for i in range(1000):
    x=random.randint(0,ww-rw)
    y=random.randint(0,wh-rh)
    window.blit(robot, (x,y))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
