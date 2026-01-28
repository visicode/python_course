# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

rw = ball.get_width()
rh = ball.get_height()
ww = window.get_width()
wh = window.get_height()
x = 50
y = 70
xv = 2
yv = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    x+=xv
    y+=yv

    if xv > 0 and x+rw >= ww: 
        xv=-xv
    if xv < 0 and x <= 0: 
        xv=-xv
    if yv > 0 and y+rh >= wh: 
        yv=-yv
    if yv < 0 and y <= 0: 
        yv=-yv

    clock.tick(60)