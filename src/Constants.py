#!/usr/bin/env python

import pygame

STOP= pygame.rect.Rect(( 0, 0),(0,0))

UP=   pygame.rect.Rect(( 0,-1),(0,0))
DOWN= pygame.rect.Rect(( 0, 1),(0,0))
LEFT= pygame.rect.Rect((-1, 0),(0,0))
RIGHT=pygame.rect.Rect(( 1, 0),(0,0))

DIRECTIONS = [UP,DOWN,LEFT,RIGHT]
