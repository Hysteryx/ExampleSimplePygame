import pygame #import de pygame

win_w = 800 #taille de vôtre fenetre 
win_h = 800
title = "Jeu Simple" #titre 
isRunning = True #permet à la boucle d'être active (c'est un while donc ça permet aussi de la coupée)

pygame.init() 
screen = pygame.display.set_mode((win_w, win_h)) #création de la fenetre 
pygame.display.set_caption(title) #ajout du titre 


#_src
image = pygame.image.load("_src/ball.png").convert()  #ajout de l'image 

x = 0 # position initiale 
y = 0 
speed = 5 #vitesse initiale 

fps = pygame.time.Clock() #fps 

while isRunning:
    for event in pygame.event.get(): #recupere les event en cours 
        if event.type == pygame.QUIT:
            isRunning = False 

    pressed = pygame.key.get_pressed() #recupere les touches actuellement préssée 
    if pressed[pygame.K_LEFT]:
        if x > 0:   #vérification que la balle n'est pas contre les bordure ou au délà 
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

    screen.fill((0,0,0)) #arriere plan 
    screen.blit(image, (x,y))
    pygame.display.flip() #actualisation 
    fps.tick(60) #fps max 

        

