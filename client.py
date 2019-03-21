import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from network import Network
from blockclass import block
from game import player

clientNumber = 0

def generateRandomFood(gridRows, player):
    playerBlockPositions = player.playerBody

    while 1:
        x = random.randrange(gridRows)
        y = random.randrange(gridRows)

        if len(list(filter(lambda z:z.position == (x, y), playerBlockPositions))) > 0:
            continue
        else:
            break
        # for i in playerBlockPositions:
        #     if(x == playerBlockPositions[0] and y == playerBlockPositions[1]):
        #         continue
        #     else:
        #         break
        # break
    randomFoodPos = (x,y)
    return randomFoodPos


def notificationBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


# def displayScoreAndResetPlayer(p):
#
#     Score = len(p.playerBody)
#     # print('Score: ', len(p.playerBody))
#
#     notificationBox('You Lost!', 'Your Score was ' + str(Score) + '. Play again?')
#     p.resetPlayer((10, 10))





def generateGrid(screenWidth, gridRows, screenSurface):
    distanceBetweenLines = screenWidth // gridRows

    xDraw = 0
    yDraw = 0
    lineColor = (195, 190, 187)

    for i in range(gridRows):

        xDraw+=distanceBetweenLines
        yDraw+=distanceBetweenLines

        pygame.draw.line(screenSurface,lineColor,(xDraw,0),(xDraw,screenWidth))
        pygame.draw.line(screenSurface,lineColor,(0,yDraw),(screenWidth,yDraw))


def RerenderWindow(screenSurface, screenColor, screenWidth, gridRows, p, p2):
    screenSurface.fill(screenColor)
    p.drawPlayer(screenSurface)
    p2.drawPlayer(screenSurface)
    #food.drawBlock(screenSurface)
    generateGrid(screenWidth, gridRows, screenSurface)
    pygame.display.update()

#gameWindow = screenSurface they are the same thing i.e the application window

def main():

    pygame.init()
    screenWidth = 500
    screenHeight = 500
    screenColor = (207,206,204)
    gridRows = 20

    gameWindow = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption('Client')


    playerColor = (244, 238, 238)
    intialPlayerPosition = (10,10)

    n = Network()
    p = n.getP()
    #food = block(generateRandomFood(gridRows,p),blockColor=(253, 152, 90))


    gameRunning = True
    gameClock = pygame.time.Clock()
    while(gameRunning):

        pygame.time.delay(50)
        gameClock.tick(10)
        p2 = n.send(p)
        # print(p2.playerBody)
        # print(block)
        p.movePlayer()
        #if (p.playerBody[0].position == food.position):
           # p.increasePlayerLength()
            #food = block(generateRandomFood(gridRows, p), blockColor=(253, 152, 90))
        p.snakeCollisionWithItself()
        p.borderCollision()
        #print(p.getPos())
        #print(p2.getPos())

        RerenderWindow(gameWindow, screenColor, screenWidth, gridRows, p, p2) #removed food



main()