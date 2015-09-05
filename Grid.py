#!/usr/bin/env python

import pygame
from math import sqrt

class Grid(pygame.sprite.Sprite):
    _cmap = None
    fgcolor = (255,255,255)
    bgcolor = (0,0,0)
    def __init__(self,x,y,width,gridType):
        super(Grid,self).__init__()
        self.rect = pygame.rect.Rect((x*width,y*width),(width,width))
        self.bounds = pygame.rect.Rect((0,0),(width,width))
        self.x = x
        self.y = y
        self.type = gridType

    def __str__(self):
        s = super(Grid,self).__str__()
        return "%s @ type %s %d,%d\n\trect: %s\n\tbounds: %s" % (s,
                                                                 self.type,
                                                                 self.x,self.y,
                                                                 self.rect,
                                                                 self.bounds)

    def distance(self,grid):
        '''
        Grid distance between two grid squares.
        '''
        x = self.x + grid.x
        y = self.y + grid.y
        return int(sqrt((x*x)+(y*y)))

    def heading(self,grid):
        '''
        Unit vector Rect between self and other grid.
        '''

        d = self.distance(grid)

        x = self.x + grid.x
        y = self.y + grid.y

        return pygame.rect.Rect((x/d,y/d),(0,0))
        
        

        
