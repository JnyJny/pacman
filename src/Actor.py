#!/usr/bin/env python

import pygame

class Actor(pygame.sprite.Sprite):
    bgcolor = (0,0,0)
    def __init__(self,position,size,heading=None):
        super(Actor,self).__init__()
        self.pixelsPerSecond = 11 * size[0]
        size = tuple(map(lambda x: x*2,size))
        self.rect = pygame.rect.Rect((0,0),size)
        self.rect.center = position
        self.bounds = pygame.rect.Rect((0,0),size)
        self.heading = heading
        self.speed = 0
        self.image = pygame.Surface(self.rect.size)
        self.image.set_colorkey(self.bgcolor)

    def __str__(self):
        return "%s\n\t%s" % (super(Actor,self).__str__(),
                             self.rect)

    def move(self,time):
        '''
        '''
        d = self.speed * time
        dx,dy = self.heading.x * d, self.heading.y * d
        self.rect.move_ip(dx,dy)

    def moveTo(self,time,targetPoint):

        dtx,dty = map(lambda v: v[0] - v[1],zip(self.rect.center,targetPoint))

        d = self.speed * time

        dx,dy = self.heading.x * min(d,dtx), self.heading.y * min(d,dty)

        self.rect.move_ip(dx,dy)
        
    def update(self,time):
        pass

    def draw(self):
        pass

    def render(self):
        pass
