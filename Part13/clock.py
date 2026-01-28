# WRITE YOUR SOLUTION HERE:
import pygame,datetime,math

pygame.init()
ww=640
wh=480
window = pygame.display.set_mode((ww, wh))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    n = datetime.datetime.now()
    h=n.hour
    m=n.minute
    s=n.second
    pygame.display.set_caption(f"{h:02}:{m:02}:{s:02}")

    window.fill((0, 0, 0))
    #borders
    pygame.draw.circle(window, (255, 0, 0), (ww/2, wh/2), wh/2-40, 5)
    pygame.draw.circle(window, (255, 0, 0), (ww/2, wh/2), 10, 10)
    #hours
    if h>12:
        ph=h-12
    else:
        ph=h
    hr = wh/2-120
    hx = ww/2+math.cos(2*math.pi/12*ph-(math.pi/2))*hr
    hy = wh/2+math.sin(2*math.pi/12*ph-(math.pi/2))*hr
    pygame.draw.line(window, (0, 0, 255), (ww/2, wh/2), (hx, hy),6)
    #minutes
    mr = wh/2-80
    mx = ww/2+math.cos(2*math.pi/60*m-(math.pi/2))*mr
    my = wh/2+math.sin(2*math.pi/60*m-(math.pi/2))*mr
    pygame.draw.line(window, (0, 0, 255), (ww/2, wh/2), (mx, my),3)
    #seconds
    sr = wh/2-60
    sx = ww/2+math.cos(2*math.pi/60*s-(math.pi/2))*sr
    sy = wh/2+math.sin(2*math.pi/60*s-(math.pi/2))*sr
    pygame.draw.line(window, (0, 0, 255), (ww/2, wh/2), (sx, sy),1)

    pygame.display.flip()

    clock.tick(1)