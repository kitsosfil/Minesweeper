# draw class for tile
import pygame
from enum import Enum 


class TileImage(Enum):
    UNCLICKED = pygame.image.load('img/empty-block.png')
    
    FLAG =  pygame.image.load('img/flag.png')
    WRONG_FLAG =  pygame.image.load('img/wrong-flag.png')

    ZERO = pygame.image.load('img/0.png')
    ONE = pygame.image.load('img/1.png')
    TWO = pygame.image.load('img/2.png')
    THREE = pygame.image.load('img/3.png')
    FOUR = pygame.image.load('img/4.png')
    FIVE = pygame.image.load('img/5.png')
    SIX = pygame.image.load('img/6.png')
    SEVEN = pygame.image.load('img/7.png')
    EIGHT = pygame.image.load('img/8.png')
    
    BOMB_CLICKED = pygame.image.load('img/bomb-at-clicked-block.png')
    BOMB_UNCLICKED = pygame.image.load('img/unclicked-bomb.png')


    
class Tile():
    def __init__(self, size = 30):
        self.size = size
        self.clicked = False
        self.flagged = False
        self.bomb =  False
        self.image = TileImage.UNCLICKED.value
        self.neighbours = None
        

    def __repr__(self):
        if self.bomb:
            return '*'
        else:
            return ' '
    
    def getTile(self):
        if self.clicked:
            if self.bomb:
                self.image =  pygame.transform.scale(TileImage.BOMB_CLICKED.value,(self.size,self.size))
            else:
                if self.neighbours == 0: pygame.transform.scale(TileImage.ZERO.value,(self.size,self.size))
                if self.neighbours == 1: pygame.transform.scale(TileImage.ONE.value,(self.size,self.size))
                if self.neighbours == 2: pygame.transform.scale(TileImage.TWO.value,(self.size,self.size))
                if self.neighbours == 3: pygame.transform.scale(TileImage.THREE.value,(self.size,self.size))
                if self.neighbours == 4: pygame.transform.scale(TileImage.FOUR.value,(self.size,self.size))
                if self.neighbours == 5: pygame.transform.scale(TileImage.FIVE.value,(self.size,self.size))
                if self.neighbours == 6: pygame.transform.scale(TileImage.SIX.value,(self.size,self.size))
                if self.neighbours == 7: pygame.transform.scale(TileImage.SEVEN.value,(self.size,self.size))
                if self.neighbours == 8: pygame.transform.scale(TileImage.EIGHT.value,(self.size,self.size))


        # image = pygame.transform.scale(pygame.image.load('img/empty-block.png')
        if self.clicked == False:
            self.image =  pygame.transform.scale(TileImage.UNCLICKED.value,(self.size,self.size))
            #self.image = TileImage.UNCLICKED.value.get_rect().inflate(self.size,self.size)
        elif self.flagged:
            self.image =  pygame.transform.scale(TileImage.FLAG.value,(self.size,self.size))
            # self.image = TileImage.FLAG.value.get_rect().inflate(self.size,self.size)
        return self.image

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours

    def getSize(self):
        return self.size
    
    def changeSize(self , size):
        self.size = size

    def isBomb(self):
        return self.bomb

# content will have values from 0 to 8 and bomb on initialization
# after that on gameplay it will be able to be marked with ?, flag  

# class Content(Enum)
