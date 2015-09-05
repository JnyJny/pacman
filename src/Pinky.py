#!/usr/bin/env python

import pygame
from Ghost import Ghost
from StateMachine import State

class PinkyChaseState(State):
    name = 'PinkyChase'
    def __init__(self):
        super(PinkyChaseState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass



class Pinky(Ghost):
    bodyColor = (253,195,212)
    def __init__(self,position,size,heading,maze):
        super(Pinky,self).__init__(position,size,heading,maze)
        self.brain.add(PinkyChaseState())
