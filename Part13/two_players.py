# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

rw = robot.get_width()
rh = robot.get_height()
ww = window.get_width()
wh = window.get_height()

x1 = 400
y1 = 100
x2 = 100
y2 = 100

to_right = False
to_left = False
to_up = False
to_down = False
to_d = False
to_a = False
to_w = False
to_s = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_a:
                to_a = True
            if event.key == pygame.K_d:
                to_d = True
            if event.key == pygame.K_w:
                to_w = True
            if event.key == pygame.K_s:
                to_s = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_a:
                to_a = False
            if event.key == pygame.K_d:
                to_d = False
            if event.key == pygame.K_w:
                to_w = False
            if event.key == pygame.K_s:
                to_s = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x1<ww-rw:
        x1 += 2
    if to_left and x1>0:
        x1 -= 2
    if to_up and y1>0:
        y1-=2
    if to_down and y1<wh-rh:
        y1+=2
    if to_d and x2<ww-rw:
        x2 += 2
    if to_a and x2>0:
        x2 -= 2
    if to_w and y2>0:
        y2-=2
    if to_s and y2<wh-rh:
        y2+=2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
