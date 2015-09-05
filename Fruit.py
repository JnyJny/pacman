#!/usr/bin/env python

from Actor import Actor
from StateMachine import StateMachine



class FruitBrain(StateMachine):
    def __init__(self):
        super(FruitBrain,self).__init__('FruitBrain')

class Fruit(Actor):
    def __init__(self,position,size,maze):
        super(Fruit,self).__init__(position,size)
        self.brain = FruitBrain()
        self.maze = maze
        self.dotCounter = 0
