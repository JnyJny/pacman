#!/usr/bin/env python

import pygame

from Grid import Grid

from Blinky import Blinky
from Pinky import Pinky
from Inky import Inky
from Clyde import Clyde


def mutecolor(color,step):
    return tuple(map(lambda x: x * step,color))

class Void(Grid):
    _cmap = ' tTpbciBIPC%0123456789'
    fgcolor = (0,0,0)
    @classmethod
    def isVoidType(cls,c):
        return c in cls._cmap

    def __init__(self,x,y,width,voidType):
        super(Void,self).__init__(x,y,width,voidType)
        self.image = pygame.Surface(self.bounds.size)

        if self.isTunnel:
            self.bgcolor = mutecolor((0,255,0),0.3)
            
        if self.isTunnelMouth:
            self.bgcolor = mutecolor((0,255,0),0.4)

        if self.isBlinkyHomeTarget or self.isBlinkySpawn:
            self.bgcolor = mutecolor(Blinky.bodyColor,0.3)

        if self.isInkyHomeTarget or self.isInkySpawn:
            self.bgcolor = mutecolor(Inky.bodyColor,0.3)

        if self.isPinkyHomeTarget or self.isPinkySpawn:
            self.bgcolor = mutecolor(Pinky.bodyColor,0.3)

        if self.isClydeHomeTarget or self.isClydeSpawn:
            self.bgcolor = mutecolor(Clyde.bodyColor,0.3)

        if self.isPlayerSpawn:
            self.bgcolor = mutecolor((255,255,0),0.3)

        self.render()

    @property
    def isVoid(self):
        return self.type == ' '

    @property
    def isTunnel(self):
        return self.type == 't'

    @property
    def isTunnelMouth(self):
        return self.type == 'T'

    @property
    def isSpawn(self):
        return self.type in 'BIPC%0123456789'

    @property
    def isHomeTarget(self):
        return self.type in 'pbci'

    @property
    def isBlinkyHomeTarget(self):
        return self.type == 'b'

    @property
    def isPinkyHomeTarget(self):
        return self.type == 'p'

    @property
    def isInkyHomeTarget(self):
        return self.type == 'i'

    @property
    def isClydeHomeTarget(self):
        return self.type == 'c'

    @property
    def isBlinkySpawn(self):
        return self.type == 'B'

    @property
    def isInkySpawn(self):
        return self.type == 'I'
    
    @property
    def isPinkySpawn(self):
        return self.type == 'P'
    
    @property
    def isClydeSpawn(self):
        return self.type == 'C'

    @property
    def isPlayerSpawn(self):
        return self.type in '0123456789'

    @property
    def playerSpawnNumber(self):
        if self.isPlayerSpawn:
            return int(self.type)
        raise ValueError("this is not a player spawn void")

    @property
    def isFruitSpawn(self):
        return self.type == '%'
    
    def render(self):
        self.image.fill(self.bgcolor)
        self.mask = pygame.draw.rect(self.image,self.fgcolor,self.bounds,1)
