#!/usr/bin/env python

import pygame
import pygame.gfxdraw

from Grid import Grid
from math import radians
from Pinky import Pinky

class Wall(Grid):
    _cmap = 'jklmJKLM[]_-|~gwxyz'
    fgcolor = (0,0,255)
    @classmethod
    def isWallType(cls,c):
        return c in cls._cmap

    def __init__(self,x,y,width,wallType):
        super(Wall,self).__init__(x,y,width,wallType)
        self.image = pygame.Surface(self.bounds.size)

        self.isGhostDoor = self.type == 'g'

        if self.isGhostDoor:
            self.fgcolor = Pinky.bodyColor

        self.render()


    def __str__(self):
        return "type %s\n\trect %s\n\tbounds %s" % (self.type,
                                                    self.bounds,
                                                    self.rect)


    def render(self):
        self.image.fill(self.bgcolor)

        radius = self.bounds.w / 2

        if self.type in 'JKLM':

            if self.type is 'J':
                x,y = self.bounds.bottomright
                start = 0
                stop = 270
            
            if self.type is 'K':
                x,y = self.bounds.bottomleft
                start = 90
                stop = 0

            if self.type is 'L':
                x,y = self.bounds.topright
                start = 270
                stop = 180

            if self.type is 'M':
                x,y = self.bounds.topleft
                start = 180
                stop = 90

            pygame.gfxdraw.arc(self.image,
                               x-2,y-2,
                               radius,
                               start,
                               stop,
                               self.fgcolor)

            pygame.gfxdraw.arc(self.image,
                               x+2,y+2,
                               radius,
                               start,
                               stop,
                               self.fgcolor)
            return
            
        
        if self.type in 'jklm':
            if self.type is 'j':
                x,y = self.bounds.bottomright
                start = 0
                stop = 270
            
            if self.type is 'k':
                x,y = self.bounds.bottomleft
                start = 90
                stop = 0

            if self.type is 'l':
                x,y = self.bounds.topright
                start = 270
                stop = 180

            if self.type is 'm':
                x,y = self.bounds.topleft
                start = 180
                stop = 90

            pygame.gfxdraw.arc(self.image,
                               x,y,
                               radius,
                               start,
                               stop,
                               self.fgcolor)
            return

        if self.type in '_-':
            x1,y = self.bounds.midleft
            x2 = self.bounds.midright[0]
            pygame.gfxdraw.hline(self.image,x1,x2,y,self.fgcolor)
            return

        if self.type in '[]':
            x,y1 = self.bounds.midtop
            y2 = self.bounds.midbottom[1]
            pygame.gfxdraw.vline(self.image,x,y1,y2,self.fgcolor)
            return


        if self.type in 'g~':
            x1,y = self.bounds.midleft
            x2 = self.bounds.midright[0]
            pygame.gfxdraw.hline(self.image,x1,x2,y-2,self.fgcolor)
            pygame.gfxdraw.hline(self.image,x1,x2,y+2,self.fgcolor)
            return

        if self.type in '|':
            x,y1 = self.bounds.midtop
            y2 = self.bounds.midbottom[1]
            pygame.gfxdraw.vline(self.image,x-2,y1,y2,self.fgcolor)
            pygame.gfxdraw.vline(self.image,x+2,y1,y2,self.fgcolor)
            return

        raise Exception("problem drawing a wall: %s" % (self))

            

