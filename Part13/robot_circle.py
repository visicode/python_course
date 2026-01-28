# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()
r = 150

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        ra = angle+(2*math.pi)-(i*(2*math.pi)/10)
        x = ww/2+math.cos(ra)*r-rw/2
        y = wh/2+math.sin(ra)*r-rh/2
        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)