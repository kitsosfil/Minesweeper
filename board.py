import random
from menu import Menu
from tile import Tile, TileSize
import pygame

class Board():
    def __init__(self, _settings):
        self.__width, self.__height = _settings.dimensions
        self._mines = _settings.mode
        self.tileSize = TileSize()
        self.createBoard()
        self.on_init
    
    @property
    def dimensions(self):
        return self.__height, self.__width,       
    @property
    def height(self):
        return self.__height
    @property
    def width(self):
        return self.__width

    def adjustTile(self, size): 
        self.tileSize.globalSize = size
    
    def createBoard(self):
        def createMines():
        # dictionary as a stack for bombs
            mines = {} 
            while len(mines) < self._mines:
                x, y = random.randint(0, self.width), random.randint(0, self.height)
                coordinates = (x*self.__width) + y
                if coordinates not in mines: 
                    mines[coordinates] = [x,y]
            return mines    

        mines = createMines()
        self._board = [ [ Tile() for _ in range(self.height) ] for _  in range(self.width)]
        # Add Bombs
        for mine in mines.keys():
            x = mines[mine][0] // self.width
            y = mines[mine][1] % self.height
            self._board[x][y].bomb = True
            # get content, assign bomb
        
    def on_init(self, surface):
        #size = self._board[0][0].size
        size = self.tileSize.globalSize
        #image = pygame.transform.scale(pygame.image.load('img/empty-block.png'),(self._board[0][0].getSize(),self._board[0][0].getSize()))
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):                        
                image = self._board[i][j].getTile()
                surface.blit(image, (i* size, j * size))
        pygame.display.flip()
    
    def on_render(self, surface):
        #size = self._board[0][0].size
        size = self.tileSize.globalSize
        for i in range(self.width):
            for j in range(self.height):                        
                image = self._board[i][j].getTile()
                surface.blit(image, (i * size, j * size))        
        return surface

    # check for content
    def tileContent(self):   
        for row in range(self.width):
            for column in range(self.height):
                bombCounter = 0 
                if not(self._board[row][column].bomb):
                    up = True if row > 0 else False
                    down = True if row < self.height-1 else False
                    left = True if column > 0  else False
                    right = True if column < self.width - 1  else False
                    
                    if up:
                        bombCounter += 1 if self._board[row - 1][column].bomb else 0
                    if up and left:
                        bombCounter += 1 if self._board[row - 1][column - 1].bomb else 0
                    if up and right:
                        bombCounter += 1 if self._board[row + 1][column + 1].bomb else 0
                    if left:
                        bombCounter += 1 if self._board[row][column - 1].bomb else 0
                    if right:
                        bombCounter += 1 if self._board[row][column + 1].bomb else 0
                    if down and left:
                        bombCounter += 1 if self._board[row - 1][column - 1].bomb else 0
                    if down:
                        bombCounter += 1 if self._board[row][column - 1].bomb else 0
                    if down and right:
                        bombCounter += 1 if self._board[row + 1][column + 1].bomb else 0
                self._board[row][column].setNeighbours(bombCounter)    
                
                    

