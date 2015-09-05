#!/usr/bin/env python


import pygame
import pygame.gfxdraw
from math import sin
from Actor import Actor
from Wall import Wall
from Void import Void
from Constants import *
from Dot import Dot
from Ghost import Ghost
from time import time


class Puckman(Actor):
    bodyColor = (255,227,0)
    fgcolor = (255,227,0)
    def __init__(self,position,size,heading,maze):
        super(Puckman,self).__init__(position,size,heading)
        self.maze = maze
        self.renderCount = 0
        self.newHeading = self.heading
        self.speed = self.maxSpeedPPS
        self.score = 0
	self.isEnergized = False
        
    @property
    def maxSpeedPPS(self):
        return int(self.pixelsPerSecond * self.maze.puckmanSpeedScale)

    @property
    def isEnergized(self):
        return self._energizeTime > 0

    @isEnergized.setter
    def isEnergized(self,value):
        if value:
            self._energizeTime = self.maze.puckmanEnergizeTime
        else:
            self._energizeTime = 0
        

    def die(self):
        print "Puckman is dying!"

    def eat(self,thing):
        if type(thing) is Dot:
            self.score += thing.value
            if thing.isEnergizer:
                self.isEnergized = True
            return

        if type(thing) is Ghost:
            if self.isEnergized:
                thing.eaten()
                self.score += thing.vaue
                return
        self.die()

    
        

    def update(self,time):

        self.speed = self.maxSpeedPPS

        if self.isEnergized:
            self._energizeTime -= time
            print "Energized for %f more seconds" % self._energizeTime

        self.grid = self.maze.gridForCoordinates(self.rect.center)

        try:
            if self.grid.isTunnelMouth:
                self.target = self.maze.locateGrid(self.grid.target,self.heading)
                self.rect.center = self.target.rect.center # WARP!
                return
        except AttributeError:
            pass

        # !WARP

        self.target = self.maze.locateGrid(self.grid,self.newHeading)

        if type(self.target) is not Wall:
            self.heading = self.newHeading
        else:
            self.target = self.maze.locateGrid(self.grid,self.heading)
            if type(self.target) is Wall:
                self.speed = 0

        self.move(time)
        self.render()

    def render(self):
        self.renderCount += 1  # free running counter, drives mouth animation

        self.image.fill(self.bgcolor)

        pygame.draw.circle(self.image,
                             self.bodyColor,
                             self.bounds.center,
                             self.bounds.width/2)

        h = int((self.bounds.width / 2) * sin(self.renderCount))

        offset = self.bounds.width / 10

        if self.heading not in DIRECTIONS:
            raise Exception("Puckman's heading is not cardinal: %s" % self.heading)

        if self.heading is UP:
            cx,cy = self.bounds.center
            x2,y2 = self.bounds.topleft
            x3,y3 = self.bounds.topright
            x2 -= h
            x3 += h 
            cy += offset

        if self.heading is DOWN:
            cx,cy = self.bounds.center
            x2,y2 = self.bounds.bottomleft
            x3,y3 = self.bounds.bottomright
            x2 += h
            x3 -= h
            cy -= offset

        if self.heading is RIGHT:
            cx,cy = self.bounds.center
            x2,y2 = self.bounds.topright
            x3,y3 = self.bounds.bottomright
            y2 += h
            y3 -= h
            cx -= offset

        if self.heading is LEFT:
            cx,cy = self.bounds.center
            x2,y2 = self.bounds.topleft
            x3,y3 = self.bounds.bottomleft
            y2 += h
            y3 -= h
            cx += offset

        pygame.gfxdraw.filled_trigon(self.image,
                                     cx,cy,
                                     x2,y2,
                                     x3,y3,
                                     (0,0,0))


    @property
    def newHeading(self):
        try:
            return self._newHeading
        except AttributeError:
            pass
        return self.heading

    @newHeading.setter
    def newHeading(self,newHeading):
        self._newHeading = newHeading
        self.speed = self.maxSpeedPPS
