#!/usr/bin/env

import pygame
from Ghost import Ghost
from StateMachine import State


class BlinkyChaseState(State):
    name = 'BlinkyChase'
    def __init__(self):
        super(BlinkyChaseState,self).__init__(type(self).name)

    def enterAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class CruiseElroyState(State):
    pass

class FirstCruiseElroyState(CruiseElroyState):
    name = 'FirstCruiseElroyState'
    def __init__(self):
        super(FirstCruiseElroyState,self).__init__(type(self).name)

    def enteryAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class SecondCruiseElroyState(CruiseElroyState):
    name = 'SecondCruiseElroyState'
    def __init__(self):
        super(SecondCruiseElroyState,self).__init__(type(self).name)

    def enteryAction(self):
        pass

    def stateAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass


class Blinky(Ghost):
    bodyColor = (253,59,17)
    def __init__(self,position,size,heading,maze):
        super(Blinky,self).__init__(position,size,heading,maze)
        self.brain.add(BlinkyChaseState())
        self.brain.add(FirstCruiseElroyState())
        self.brain.add(SecondCruiseElroyState())
        self.brain.setStateByName(BlinkyChaseState.name)
