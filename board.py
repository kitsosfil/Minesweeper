import random
from menu import Menu
from tile import Tile
import pygame

class Board():
    def __init__(self, _settings):
        # self._mode
        # self._dimensions
        self._width, self._height = _settings._dimensions
        self._mines = _settings._mode
        self.createBoard()
        self.on_init
    
    def on_init(self, surface):
        size = self._board[0][0].getSize()

        #image = pygame.transform.scale(pygame.image.load('img/empty-block.png'),(self._board[0][0].getSize(),self._board[0][0].getSize()))
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):                        
                image = self._board[i][j].getTile()
                surface.blit(image, (i* size, j * size))
        pygame.display.flip()
    
    def on_render(self, surface):
        size = self._board[0][0].getSize()
        for i in range(self._width):
            for j in range(self._height):                        
                image = self._board[i][j].getTile()
                surface.blit(image, (i * size, j * size))        
        return surface


    def createBoard(self):
        mines = self.createMines()
        self._board = [ [ Tile() for _ in range(self._height) ] for _  in range(self._width)]    
                
        # Add Bombs
        for mine in mines.keys():
            x = mines[mine][0] // self._width
            y = mines[mine][1] % self._height
            self._board[x][y].bomb = True
            # get content, assign bomb
        
    
    def createMines(self):
        # dictionary as a stack for bombs
        mines = {} 
        while len(mines) < self._mines:
            x, y = random.randint(0, self._width), random.randint(0, self._height)
            coordinates = (x*self._width) + y
            if coordinates not in mines: 
                mines[coordinates] = [x,y]
        return mines

    def get_dimensions(self):
        return self._height, self._width,       
    
    def adjustTile(self, size):
        for row in range(self._width):
            for column in range(self._height):
                self._board[row][column].changeSize(size)

    # check for content
    def tileContent(self):   
        for row in range(self._width):
            for column in range(self._height):
                bombCounter = 0 
                if not(self._board[row][column].bomb):
                    up = True if row > 0 else False
                    down = True if row < self._height-1 else False
                    left = True if column > 0  else False
                    right = True if column < self._width - 1  else False
                    
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
                
                    

