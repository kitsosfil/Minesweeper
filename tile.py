# draw class for tile
import pygame
from enum import Enum 

img = pygame.image.load('img/sprite100.gif')

class TileImage(Enum):
    UNCLICKED = img.subsurface(0, 39, 16, 16)
    FLAG = img.subsurface(16, 39, 16, 16)
    BOMB_CLICKED = img.subsurface(32, 39, 16, 16)
    WRONG_FLAG = img.subsurface(48, 39, 16, 16)
    BOMB_UNCLICKED = img.subsurface(64, 39, 16, 16)

    ZERO = img.subsurface(0, 23, 16, 16)
    ONE = img.subsurface(16, 23, 16, 16)
    TWO = img.subsurface(32, 23, 16, 16)
    THREE = img.subsurface(48, 23, 16, 16)
    FOUR = img.subsurface(64, 23, 16, 16)
    FIVE = img.subsurface(80, 23, 16, 16)
    SIX = img.subsurface(96, 23, 16, 16)
    SEVEN = img.subsurface(112, 23, 16, 16)
    EIGHT = img.subsurface(128, 23, 16, 16)
    

    # UNCLICKED = pygame.image.load('img/empty-block.png')
    # FLAG =  pygame.image.load('img/flag.png')
    # WRONG_FLAG =  pygame.image.load('img/wrong-flag.png')
    # ZERO = pygame.image.load('img/0.png')
    # ONE = pygame.image.load('img/1.png')
    # TWO = pygame.image.load('img/2.png')
    # THREE = pygame.image.load('img/3.png')
    # FOUR = pygame.image.load('img/4.png')
    # FIVE = pygame.image.load('img/5.png')
    # SIX = pygame.image.load('img/6.png')
    # SEVEN = pygame.image.load('img/7.png')
    # EIGHT = pygame.image.load('img/8.png')
    
    # BOMB_CLICKED = pygame.image.load('img/bomb-at-clicked-block.png')
    # BOMB_UNCLICKED = pygame.image.load('img/unclicked-bomb.png')

# class TileSize():
#     __shared_state = {}

#     def __init__(self):
#         self.__dict__ = self.__shared_state 
#         self.__global_size = 30

#     @property
#     def globalSize(self):
#         return self.__global_size
    
#     @globalSize.setter
#     def globalSize(self,value):
#         self.__global_size = value


class Tile():
    __size = 30
    def changeSize(value):
        Tile.__size = value
    
    def __init__(self):       
        self.__opened = False
        self.clicked = False
        self.flagged = False
        self.__bomb =  False
        self.image = TileImage.UNCLICKED.value
        self.neighbours = None
        # state = {close, open, flagged}
        # content(neighbours or Bomb)
        # 
    @property
    def size(self):
        return Tile.__size
    #@size.setter
   
    @property
    def bomb(self):
        return self.__bomb
    @bomb.setter
    def bomb(self, value):
        self.__bomb = value
    
    @property
    def open(self): return self.__opened

    @open.setter
    def open(self, value = True):
        self.__opened = value
        self.flagged = False

    def __repr__(self):
        return str(self.neighbours)
    
    def getTile(self):
        if self.clicked:
            self.image =  pygame.transform.scale(TileImage.BOMB_CLICKED.value,(self.size,self.size))
        elif self.open:
            if self.bomb:
                self.image =  pygame.transform.scale(TileImage.BOMB_CLICKED.value,(self.size,self.size))
            else:
                if self.neighbours == 0: self.image = pygame.transform.scale(TileImage.ZERO.value,(self.size,self.size))
                if self.neighbours == 1: self.image = pygame.transform.scale(TileImage.ONE.value,(self.size,self.size))
                if self.neighbours == 2: self.image = pygame.transform.scale(TileImage.TWO.value,(self.size,self.size))
                if self.neighbours == 3: self.image = pygame.transform.scale(TileImage.THREE.value,(self.size,self.size))
                if self.neighbours == 4: self.image = pygame.transform.scale(TileImage.FOUR.value,(self.size,self.size))
                if self.neighbours == 5: self.image = pygame.transform.scale(TileImage.FIVE.value,(self.size,self.size))
                if self.neighbours == 6: self.image = pygame.transform.scale(TileImage.SIX.value,(self.size,self.size))
                if self.neighbours == 7: self.image = pygame.transform.scale(TileImage.SEVEN.value,(self.size,self.size))
                if self.neighbours == 8: self.image = pygame.transform.scale(TileImage.EIGHT.value,(self.size,self.size))
                
        elif self.flagged:
            self.image =  pygame.transform.scale(TileImage.FLAG.value,(self.size,self.size))
        elif self.clicked == False:
            self.image =  pygame.transform.scale(TileImage.UNCLICKED.value,(self.size,self.size))
        return self.image

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours

    def isBomb(self):
        return self.bomb

# content will have values from 0 to 8 and bomb on initialization
# after that on gameplay it will be able to be marked with ?, flag  

# class Content(Enum)
