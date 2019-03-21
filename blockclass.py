import pygame

class block(object):
    gridRows = 20
    screenWidth = 500
    def __init__(self,startpos,dx=0,dy=1,blockColor=(244, 238, 238)):
        self.position = startpos
        self.dx = 1
        self.dy = 0
        self.blockColor = blockColor

    def moveBlock(self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.position = (self.position[0] + self.dx, self.position[1] + self.dy)

    def drawBlock(self, screenSurface):
        blockLength = self.screenWidth // self.gridRows

        currRow = self.position[0]
        currCol = self.position[1]

        rectDimensions =  (currRow*blockLength+1,currCol*blockLength+1, blockLength-2, blockLength-2)

        pygame.draw.rect(screenSurface, self.blockColor,rectDimensions)