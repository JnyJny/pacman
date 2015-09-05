#!/usr/bin/env python

import sys
import time
import pygame
from pygame.locals import *
from Maze import Maze
from Constants import *
from StateMachine import State, StateMachine

FONTNAME='PressStart2P.ttf'

class LevelSpecification(object):
    pass

class LevelSpecifications(object):

    SCHEMA = ['level',
              'bonusSymbol',
              'bonusPoints',
              'pacmanSpeed',
              'pacmanDotsSpeed',
              'ghostSpeed',
              'ghostTunnlSpeed',
              'elroy1DotsLeft',
              'elroy1Speed',
              'elroy2DotsLeft',
              'elroy2Speed',
              'panicPacmanSpeed',
              'panicPacmanDot']


    def __init__(self,filename):
        f = open(filename)
        for line in map(str.strip,f.readlines()):
            print 'X',line,'X'


class GameMode(State):

    def __init__(self,game):
        super(GameMode,self).__init__(type(self).name)
        self.game = game
        self.events = {}
        self.controls = {}
        self.addEvent(QUIT,sys.exit)

    def addEvent(self,event,action):
        name = pygame.event.event_name(event)
        self.events.setdefault(name,action)

    def addControl(self,keycode,action):
        self.controls.setdefault(keycode,action)
            
    def dispatch_pressed(self):
        pressed = pygame.key.get_pressed()
        for key, action in self.controls.items():
            if pressed[key]:
                action()

    def dispatch_events(self):
        for event in pygame.event.get():
            name = pygame.event.event_name(event.type)
            try:
                self.events[name](event)
            except KeyError:
                pass

class AttractMode(GameMode):
    name = 'AttractMode'

    def stateAction(self):
        pass

    def enterAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass

class SetupLevelMode(GameMode):
    name = 'SetupLevelMode'
        
    def checkConditions(self):
        return None
    def enterAction(self):
        pass
    def exitAction(self):
        pass
    def stateAction(self):
        pass
        

class PlayingMode(GameMode):
    name = 'PlayingMode'
    def __init__(self,game):
        super(PlayingMode,self).__init__(game)
        self.addEvent(KEYUP,self.keyUp)
        self.addControl(K_w, self.game.up)
        self.addControl(K_s, self.game.down)
        self.addControl(K_a, self.game.left)
        self.addControl(K_d, self.game.right)
        self.addControl(K_ESCAPE, self.game.quit)

    def keyUp(self,event):
        if event.key == K_SPACE:
            self.game.paused = not self.game.paused

    def checkConditions(self):
        if self.game.lives == 0:
            return GameOverMode.name

        if len(self.game.maze.dots) == 0:
            return SetupLevelMode.name
        
        return None

    def enterAction(self):
        self.game.lives = 3
        self.game.maze.reset(self.game.maze.level + 1)
        # do "Ready!" animation here

    def exitAction(self):
        pass

    def stateAction(self):

        self.dispatch_events()
                
        self.dispatch_pressed()

        self.game.update()

        self.game.draw()

        pygame.display.update()


class IntermissionMode(GameMode):
    name = 'IntermissionMode'
    def __init__(self,game):
        super(IntermissionMode,self).__init__(type(self).name)
        self.game = game

    def checkConditions(self):
        if self.countDown == 0:
            return SetupLevelMode.name
        return none

    def enterAction(self):
        self.count = 100

    def exitAction(self):
        pass

    def stateAction(self):
        self.count -= 1
        pygame.time.delay(250)
        print 'intermission... '

class GameOverMode(GameMode):
    name = 'GameOverMode'
    def __init__(self,game):
        super(GameOverMode,self).__init__(type(self).name)
        self.game = game

    def stateAction(self):
        pass

    def enterAction(self):
        pass

    def exitAction(self):
        pass

    def checkConditions(self):
        pass




class Game(StateMachine):

    def __init__(self,gridSize=32,frameRate=60):
        super(Game,self).__init__('TheGame.You Lost It.')

        pygame.init()

        self.framerate = frameRate
        self.maze = Maze(gridSize)
        self.maze.read("theMaze")
        self.screen = pygame.display.set_mode(self.maze.rect.size,0,32)
        self.clock = pygame.time.Clock()
        self.paused = False

        self.add(AttractMode(self))
        self.add(SetupLevelMode(self))
        self.add(PlayingMode(self))
        self.add(IntermissionMode(self))
        self.add(GameOverMode(self))
        self.setStateByName(PlayingMode.name)


    @property
    def time(self):
        ms = self.clock.tick(self.framerate)
        return ms / 1000.0

    @property
    def font(self):
        try:
            return self._font
        except AttributeError:
            pass
        self._font = pygame.font.Font(FONTNAME,self.maze.gridWidth)
        return self._font

    @property
    def highScoreLabel(self):
        try:
            return self._highScoreLabel
        except AttributeError:
            pass
        self._highScoreLabel = self.font.render("HIGH SCORE", True, (255,255,255),(0,0,0))
        return self._highScoreLabel

    @property
    def oneUpLabel(self):
        try:
            return self._oneUpLabel
        except AttributeError:
            pass
        self._oneUpLabel = self.font.render("1UP", True, (255,255,255),(0,0,0))
        return self._oneUpLabel

    @property
    def twoUpLabel(self):
        try:
            return self._twoUpLabel
        except AttributeError:
            pass
        self._twoUpLabel = self.font.render("2UP", True, (255,255,255),(0,0,0))
        return self._twoUpLabel

    @property
    def readyLabel(self):
        try:
            return self._readyLabel
        except AttributeError:
            pass
        self._readyLabel = self.font.render("Ready!", True, (255,255,0),(0,0,0))
        return self._readyLabel


    def start(self):
        pass

    def up(self):
        self.maze.puckman.newHeading = UP

    def down(self):
        self.maze.puckman.newHeading = DOWN

    def left(self):
        self.maze.puckman.newHeading = LEFT

    def right(self):
        self.maze.puckman.newHeading = RIGHT

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def run(self):
        while True:
            self.think()

    def quit(self):
        print "quitting"
        exit()

    def drawHighScore(self):
        lrect = self.highScoreLabel.get_rect()
        srect = self.screen.get_rect()
        lrect.midtop = srect.midtop
        self.screen.blit(self.highScoreLabel,lrect.topleft)

    def draw1UpScore(self,score):
        r = self.screen.get_rect()
        scoreText = self.font.render("%d" % score, True, (255,255,0),(0,0,0))
        lrect = scoreText.get_rect()

        x,y = r.midtop

        x /= 4
        y += self.maze.gridWidth

        lrect.midtop = (x,y)
        self.screen.blit(scoreText,lrect.topleft)
        

    def draw1Up(self):
        lrect = self.oneUpLabel.get_rect()
        srect = self.screen.get_rect()
        x,y = srect.midtop
        x /= 2
        lrect.midtop = (x,y)
        self.screen.blit(self.oneUpLabel,lrect.topleft)
        

    def draw2Up(self):
        pass

    def drawFruit(self):
        pass

    def update(self):
        if self.paused:
            self.time
        else:
            self.maze.update(self.time)

    def draw(self):

        self.maze.draw(self.screen)

        self.drawHighScore()
        self.draw1Up()
        self.draw1UpScore(self.maze.puckman.score)
        self.draw2Up()
        self.drawFruit()

if __name__ == '__main__':
    Game().run()
