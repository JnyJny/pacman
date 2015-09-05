#!/usr/bin/env python

import pygame
from Ghost import Ghost
from StateMachine import State

class InkyChaseState(State):
    name = 'InkyChase'
    def __init__(self):
        super(InkyChaseState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass


class Inky(Ghost):
    bodyColor = (73,223,202)
    def __init__(self,position,size,heading,maze):
        super(Inky,self).__init__(position,size,heading,maze)
        self.brain.add(InkyChaseState)
