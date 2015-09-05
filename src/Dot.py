#!/usr/bin/env python

import pygame
from Grid import Grid

class Dot(Grid):
    _cmap = '.+'
    _fgcolor = (255,255,255)
    @classmethod
    def isDotType(cls,c):
        return c in cls._cmap

    def __init__(self,x,y,width,dotType):
        super(Dot,self).__init__(x,y,width,dotType)
        self.image = pygame.Surface(self.bounds.size)
        self.render()

    @property
    def isEnergizer(self):
        return self.type == '+'

    @property
    def isDot(self):
        return self.type == '.'

    @property
    def value(self):
        if self.isEnergizer:
            return 50
        return 10

    @property
    def radius(self):
        if self.isEnergizer:
            return self.bounds.width / 4
        return self.bounds.width / 8

    def render(self):
        self.image.fill(self.bgcolor)
        self.mask = pygame.draw.circle(self.image,
                                       self.fgcolor,
                                       self.bounds.center,
                                       self.radius,0)
