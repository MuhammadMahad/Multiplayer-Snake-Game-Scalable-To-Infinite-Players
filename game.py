import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from network import Network
from blockclass import block

class player(object):
    # playerBody = []
    # headTurns = {}
    # blocks = []

    def __init__(self, position, playerColor):
        self.playerBody = []
        self.headTurns = {}
        self.blocks = []
        self.playerColor = playerColor
        self.head = block(position)
        self.pos = position
        self.playerBody.append(self.head)

        self.dx = 0
        self.dy = 1

        self.lose = False


    def getPos(self):
        return self.pos

    def updateTurns(self):
        self.headTurns[self.head.position[:]] = [self.dx, self.dy]


    def buttonEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            pressedKeys = pygame.key.get_pressed()

            for pressedKey in pressedKeys:
                if pressedKeys[pygame.K_UP]:
                    self.dx = 0
                    self.dy = -1
                    self.updateTurns()

                elif pressedKeys[pygame.K_DOWN]:
                    self.dx = 0
                    self.dy = 1
                    self.updateTurns()

                elif pressedKeys[pygame.K_LEFT]:
                    self.dx = -1
                    self.dy = 0
                    self.updateTurns()

                elif pressedKeys[pygame.K_RIGHT]:
                    self.dx = 1
                    self.dy = 0
                    self.updateTurns()



    def borderCollision(self):
        for i, block in enumerate(self.playerBody):
            blockpos = block.position[:]
            if block.dx == -1 and block.position[0] < 0:
                #displayScoreAndResetPlayer(self)
                self.lose = True
            elif block.dx == 1 and block.position[0] > block.gridRows - 1:
                self.lose = True
                #displayScoreAndResetPlayer(self)
            elif block.dy == 1 and block.position[1] > block.gridRows - 1:
                self.lose = True
                #displayScoreAndResetPlayer(self)
            elif block.dy == -1 and block.position[1] < 0:
                self.lose = True
                #displayScoreAndResetPlayer(self)
            # else:
            #     return True

    #     blockpos = block.position[:]
    def turn(self):
        for i, block in enumerate(self.playerBody):
            blockpos = block.position[:]
            if blockpos in self.headTurns:
                directionToTurn = self.headTurns[blockpos]
                block.moveBlock(directionToTurn[0],directionToTurn[1])
                if i == len(self.playerBody)-1:
                    self.headTurns.pop(blockpos)

                # elif:
                #     borderCollision()

            # else:
            #     if block.dx == -1 and block.position[0] <= 0:
            #         block.position = (block.gridRows - 1, block.position[1])
            #     elif block.dx == 1 and block.position[0] >= block.gridRows - 1:
            #         block.position = (0, block.position[1])
            #     elif block.dy == 1 and block.position[1] >= block.gridRows - 1:
            #         block.position = (block.position[0], 0)
            #     elif block.dy == -1 and block.position[1] <= 0:
            #         block.position = (block.position[0], block.gridRows - 1)
            #     else:
            #         block.moveBlock(block.dx, block.dy)

            else:
                block.moveBlock(block.dx,block.dy)

                    #elif snakeCollision()

    def movePlayer(self):
        self.buttonEvents()
        self.turn()

    def drawPlayer(self, screenSurface):
        for i, block in enumerate(self.playerBody):
            block.drawBlock(screenSurface)

    def increasePlayerLength(self):
        tail = self.playerBody[-1]
        currdx = tail.dx
        currdy = tail.dy

        if currdx == 0 and currdy == 1:
            self.playerBody.append(block((tail.position[0],tail.position[1]-1)))
        elif currdx == 0 and currdy == -1:
            self.playerBody.append(block((tail.position[0],tail.position[1]+1)))
        elif currdx == 1 and currdy == 0:
            self.playerBody.append(block((tail.position[0]-1,tail.position[1])))
        elif currdx == -1 and currdy == 0:
            self.playerBody.append(block((tail.position[0]+1,tail.position[1])))

        self.playerBody[-1].dx = currdx
        self.playerBody[-1].dy = currdy




    def resetPlayer(self, position):
        self.head = block(position)
        self.playerBody = []
        self.playerBody.append(self.head)
        self.headTurns = {}
        self.dx = 1
        self.dy = 0

    def snakeCollisionWithItself(self):
        for x in range(len(self.playerBody)):
            if self.playerBody[x].position in list(map(lambda z: z.position, self.playerBody[x + 1:])):
                self.lose = True
                #displayScoreAndResetPlayer(self)
                break




