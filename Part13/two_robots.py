# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()
x = 0
y = 50
x2 = 0
y2 = 50+2*rh
vx = 1 #robot1
wx = 2 #robot2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x += vx
    x2+= wx
    if vx > 0 and x+rw >= ww:
        vx = -vx
    if vx < 0 and x <= 0:
        vx = -vx
    if wx > 0 and x2+rw >= ww:
        wx = -wx
    if wx < 0 and x2 <= 0:
        wx = -wx

    clock.tick(60)