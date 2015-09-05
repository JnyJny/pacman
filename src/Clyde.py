#!/usr/bin/env python

import pygame
from Ghost import Ghost
from StateMachine import State


class ClydeChaseState(State):
    name = 'ClydeChase'
    def __init__(self):
        super(ClydeChaseState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass


class Clyde(Ghost):
    bodyColor = (255,191,87)
    def __init__(self,position,size,heading,maze):
        super(Clyde,self).__init__(position,size,heading,maze)
        self.brain.add(ClydeChaseState())
