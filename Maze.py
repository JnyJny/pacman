#!/usr/bin/env python

import pygame

from Void import Void
from Wall import Wall
from Dot import Dot

from Blinky import Blinky
from Inky import Inky
from Pinky import Pinky
from Clyde import Clyde
from Puckman import Puckman
from Fruit import Fruit

from Constants import *

##
## http://home.comcast.net/~jpittman2/pacman/pacmandossier.html
##



def collide_center(left,right):
    return left.collidepoint(right.center)

class GridFactory(object):
    @classmethod
    def gridForType(cls,x,y,width,gridType):

        if Void.isVoidType(gridType):
            return Void(x,y,width,gridType)

        if Dot.isDotType(gridType):
            return Dot(x,y,width,gridType)

        if Wall.isWallType(gridType):
            return Wall(x,y,width,gridType)
        
        raise ValueError("unknown grid type %s" % (gridType))


class Maze(pygame.sprite.RenderUpdates):
    bgcolor = (0,0,255)
    def __init__(self,gridWidth=8):
        self.level = 0
        self.gridWidth = gridWidth
        self.grids = {}         # key is tuple (x,y) in game coords

        self.legal = pygame.sprite.RenderUpdates()   # dots and voids
        self.illegal = pygame.sprite.RenderUpdates() # walls
        self.dots = pygame.sprite.RenderUpdates()    # just dots
        self.eaten = []                      # move eaten dots here
        self.tunnelMouths = []               # collect tunnel mouths
        self.players = pygame.sprite.RenderUpdates()
        self.ghosts = pygame.sprite.RenderUpdates()
        self.guys = pygame.sprite.RenderUpdates()

        self.guys.add(Puckman((0,0),(gridWidth,gridWidth),LEFT,self))
        self.guys.add(Puckman((0,0),(gridWidth,gridWidth),LEFT,self))
        self.guys.add(Puckman((0,0),(gridWidth,gridWidth),LEFT,self))

    def __str__(self):
        s = []
        s.extend(self.map)
        s.append("W/H = %d,%d" % (self.width,self.height))
        return '\n'.join(s)



    @property
    def rect(self):
        try:
            return self._rect
        except AttributeError:
            pass
        w = self.width * self.gridWidth
        h = self.height * self.gridWidth
        self._rect = pygame.rect.Rect((0,0),(w,h))
        return self._rect
        
        
    def reset(self,nextLevel):
        '''
        repopulate maze with dots
        reset various global per-level counters and variables
        '''
#        self.read(self.filename)
        self.level = nextLevel


    def read(self,filename):
        self.filename = filename
        try:
            f = open(filename)
        except IOError:
            f = open(filename+'.mz')
        self.map = [l.strip('\n') for l in f.readlines()]
        f.close()
        # self.map is an array of lines of characters

        for y in xrange(self.height):
            line = self.map[y]
            for x in xrange(self.width):
                c = line[x]
                try:
                    grid = GridFactory.gridForType(x,y,self.gridWidth,c)
                except ValueError, e:
                    print e
                    continue

                self.grids.setdefault((x,y),grid)

                gridType = type(grid)

                if gridType is Wall:
                    self.illegal.add(grid)
                    continue
                
                if gridType is Dot:
                    self.legal.add(grid)
                    self.dots.add(grid)
                    continue

                if gridType is Void:
                    self.legal.add(grid)
                    if grid.isTunnelMouth:
                        self.tunnelMouths.append(grid)
                        if len(self.tunnelMouths) == 2:
                            self.tunnelMouths[0].target = self.tunnelMouths[1]
                            self.tunnelMouths[1].target = self.tunnelMouths[0]

                    continue

        for grid in self.legal:
            if type(grid) != Void:
                continue

            if grid.isSpawn == False:
                continue

            if grid.isPlayerSpawn:
                self.puckman = Puckman((0,0),(grid.rect.w,grid.rect.w),LEFT,self)
                self.puckman.rect.center = grid.rect.midright
                self.players.add(self.puckman)
                continue

            if grid.isBlinkySpawn:
                self.Blinky = Blinky(grid.rect.midright,
                                     grid.rect.size,
                                     LEFT,
                                     self)
                self.ghosts.add(self.Blinky)
                                
                continue

            if grid.isInkySpawn:

                self.Inky = Inky(grid.rect.midright,
                                 grid.rect.size,
                                 UP,
                                 self)
                self.ghosts.add(self.Inky)
                continue

            if grid.isPinkySpawn:

                self.Pinky = Pinky(grid.rect.midright,
                                   grid.rect.size,
                                   DOWN,
                                   self)
                self.ghosts.add(self.Pinky)
                continue

            if grid.isClydeSpawn:
                self.Clyde = Clyde(grid.rect.midright,
                                   grid.rect.size,
                                   UP,
                                   self)
                self.ghosts.add(self.Clyde)
                continue

            if grid.isFruitSpawn:
                self.Fruit = Fruit(grid.rect.midright,
                                   grid.rect.size,
                                   self)
                continue

            
            

    @property
    def height(self):
        try:
            return self._height
        except AttributeError:
            self._height = len(self.map)
        return self._height

    @property
    def width(self):
        try:
            return self._width
        except AttributeError:
            self._width = 0
            for l in self.map:
                self._width = max(self._width,len(l))
        return self._width
            

    def write(self,filename):
        pass

    def update(self,time):

        self.illegal.update(time)
        self.legal.update(time)
        self.ghosts.update(time)
        self.players.update(time)

        dots = pygame.sprite.spritecollide(self.puckman,self.dots,True)

        if len(dots):
            for dot in dots:
                self.puckman.eat(dot)

            if self.puckman.isEnergized:
                self.Blinky.panic()
                self.Inky.panic()
                self.Pinky.panic()
                self.Clyde.panic()

            print "Score: ",self.puckman.score,"dots left:", len(self.dots)

        ghosts = pygame.sprite.spritecollide(self.puckman,self.ghosts,False)

        if len(ghosts):
            for ghost in ghosts:
                self.puckman.eat(ghost)

        

    def draw(self,surface):
        surface.fill((0,0,0))
        self.illegal.draw(surface)
        self.legal.draw(surface)
        self.ghosts.draw(surface)
        self.players.draw(surface)

    def gridForCoordinates(self,coords):
        x,y = tuple(map(lambda v:v / self.gridWidth,coords))
        return self.grids[(x,y)]

    def locateGrid(self,srcGrid,heading,distance=1):
        x = srcGrid.x + (heading.x * distance)
        y = srcGrid.y + (heading.y * distance)
        return self.grids[(x,y)]

    @property
    def puckmanSpeedScale(self):
        return 1.0

    @property
    def ghostSpeedScale(self):
        return 1.0

    @property
    def puckmanEnergizeTime(self):
        return 10.0

if __name__ == '__main__':
    m = Maze()
    m.read("theMaze")
    print m
