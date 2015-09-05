#!/usr/bin/env python

import pygame
import pygame.gfxdraw

from Actor import Actor
from StateMachine import State, StateMachine



class ScatterState(State):
    name = 'ScatterState'
    def __init__(self):
        super(ScatterState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class FrightenedState(State):
    name = 'FrightenedState'
    def __init__(self):
       super(FrightenedState,self).__init__(type(self).name)
 
    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class GhostHouseIdleState(State):
    name = 'GhostHouseIdle'
    def __init__(self):
        super(GhostHouseIdleState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class GhostBrain(StateMachine):
    def __init__(self,name):
        super(GhostBrain,self).__init__(name)
        self.add(ScatterState())
        self.add(FrightenedState())
        self.add(GhostHouseIdleState())
        self.setStateByName(GhostHouseIdleState.name)


class Ghost(Actor):
    _body0 = []
    _body1 = []
    _transparent = (0,0,0)

    _frightenedColors0 = ((35,63,139),(253,189,150))
    _frightenedColors1 = ((231,235,223),(253,59,17))
    
    bodyColor = (0,255,0)

    def __init__(self,position,size,heading=None,maze=None):
        super(Ghost,self).__init__(position,size,heading)
        self.image.set_colorkey(self.bgcolor)
        self.target = None
        self.maze = maze
        self.value = 100
        self.brain = GhostBrain(type(self))

    def eaten(self):
        if type(self.brain.currentState) is FrightenedState:
            print 'i %s am eated' % type(self)
            return True
        else:
            print 'i %s eat you!' % type(self)
            return False

    def panic(self):
        print 'alas, i %s am panicing' % type(self)

        self.brain.setStateByName(FrightenedState.name)
        

    def update(self,time):
        self.render()

    def render(self):
        self.image.fill(self._transparent)
        x,y = self.bounds.center
        pygame.gfxdraw.filled_circle(self.image,
                                     x,y,
                                     (self.bounds.width/2)-5,
                                     self.bodyColor)
