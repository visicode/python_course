# WRITE YOUR SOLUTION HERE:
import pygame,random

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()

rx = (ww-rw)/2
ry = (wh-rh)/2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if rx<=x<=rx+rw and ry<=y<=ry+rh:
                while True:
                    rx=random.randint(0,ww-rw)
                    ry=random.randint(0,wh-rh)
                    if rx>x or rx<x-rw or ry>y or ry<y-rh:
                        break


        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (rx, ry))
    pygame.display.flip()

    clock.tick(60)