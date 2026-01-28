# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

ww = window.get_width()
wh = window.get_height()
rw = robot.get_width()
rh= robot.get_height()
#print (rw,rh)

window.fill((0, 0, 0))

begin=(ww-12*rw)//2

for i in range(10):
    for j in range(10):
        window.blit(robot, (begin+j*rw,rh+i*rh/5))
    begin+=rw/5

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
