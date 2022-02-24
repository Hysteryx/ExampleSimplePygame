from asyncio import events
import pygame 

win_w = 800
win_h = 800
title = "Jeu Simple"
isRunning = True 

pygame.init()
screen = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption(title)


#_src
image = pygame.image.load("_src/ball.png").convert()

x = 0 
y = 0 
speed = 5 

clock = pygame.time.Clock()

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False 

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if x > 0:
            x -= speed
    if pressed[pygame.K_RIGHT]:
        if x < win_w-100:
            x += speed
    if pressed[pygame.K_DOWN]:
        if y < win_h-100: #100*100 dim img 
            y += speed
    if pressed[pygame.K_UP]:
        if y > 0:
            y -= speed
    if pressed[pygame.K_F1]:
        if speed < 20:
            speed += 0.1
    if pressed[pygame.K_F2]:
        if speed > 1:
            speed -= 0.1

    screen.fill((0,0,0))
    screen.blit(image, (x,y))
    pygame.display.flip()
    clock.tick(60)

        

