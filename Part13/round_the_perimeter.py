# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()
x = 0
y = 0
xv = 1
yv = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x+=xv
    y+=yv

    if xv > 0 and x+rw >= ww: #corner up-right
        xv=0
        yv=1
    if xv < 0 and x <= 0: #lower-left
        xv=0
        yv=-1
    if yv > 0 and y+rh >= wh: #lower-right
        xv=-1
        yv=0
    if yv < 0 and y <= 0: #upper-left
        xv=1
        yv=0

    clock.tick(60)