#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((1024,768),RESIZABLE,32)

fonts = pygame.font.get_fonts()

fontsz = 8

fontname = fonts.pop()

try:
	font = pygame.font.Font("PressStart2P.ttf",fontsz)
except:
	font = pygame.font.SysFont(fontname,fontsz)



Score = font.render('SCORE', True, (0,0,0),(255,255,255))

srect = Score.get_rect()

Ready = font.render('Ready!', True, (255,255,255),(0,0,0))

rrect = Ready.get_rect()

r = screen.get_rect()

srect.midtop = r.midtop
rrect.center = r.center

while True:

    event = pygame.event.wait()

    print event

    if event.type == QUIT:
        exit()

#    if event.type == KEYUP:


    screen.fill((0,0,0))
    screen.blit(Score,srect.topleft)
    screen.blit(Ready,rrect.topleft)
    
    pygame.display.update()
