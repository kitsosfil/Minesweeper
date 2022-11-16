import random
from menu import Menu
from tile import Tile
import pygame

class Board():
    def __init__(self, _settings):
        self.__rows, self.__columns = _settings.dimensions
        self._mines = _settings.mode
        self.tileSize = Tile().size
        self.createBoard()
        self.on_init
    
    @property
    def rows(self):
        return self.__rows
    @property
    def columns(self):
        return self.__columns
    @property
    def dimensions(self):
        return self.__rows, self.__columns

    def adjustTile(self, size): 
        self.tileSize = size
        Tile.changeSize(size)
    
    def createBoard(self):
        def createMines():
        # dictionary as a stack for bombs
            mines = set() 
            while len(mines) < self._mines:
                x, y = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
                if (x,y) not in mines: 
                    mines.add((x,y))
            return mines    

        mines = createMines()
        # print(f"CreateBoard width: {self.width}, height: {self.height}")
        print(f" Create board Dimensions:{self.dimensions}")
        self._board = [ [ Tile() for _ in range(self.columns) ] for _  in range(self.rows)]
        
        # Add Bombs
        
        for mine in mines:
            x, y = mine
            self._board[x][y].bomb =  True
        self.tileContent()
        
        
    def on_init(self, surface):
        size = self._board[0][0].size
        for i in range(self.rows):
            for j in range(self.columns):
                image = self._board[i][j].getTile()
                surface.blit(image, (j * size, i * size))        
        print(self._board)
        pygame.display.flip()

    def on_render(self, surface):
        size = self._board[0][0].size
        for i in range(self.rows):
            for j in range(self.columns):                        
                image = self._board[i][j].getTile()
                surface.blit(image, (j * size, i * size))        
        return surface
    
    def action(self, buttons):
        m1 , m2  = False, False
        for keys in buttons:
            if keys.eventID == 1025:
                m1 = m1 or keys.buttons[0]
                m2 = m2 or keys.buttons[1]
            if keys.eventID == 1026:
                row, column = keys.row, keys.column
        if m1 and not m2:
            self.openTiles(row,column)
        elif not m1 and m2:
            if not self._board[keys.row][keys.column].flagged:
                self._board[keys.row][keys.column].flagged = True
            else: 
                self._board[keys.row][keys.column].flagged = False
            
    def openTiles(self, row, column):
        if not self._board[row][column].flagged:
            self._board[row][column].opened = True
            if self._board[row][column].neighbours == 0:
                
                up = True if row > 0 else False
                down = True if row < self.rows - 1 else False
                left = True if column > 0 else False
                right = True if column < self.columns - 1  else False 
                
                if up and not self._board[row - 1][column].opened:
                    self.openTiles(row - 1, column)
                if right and not self._board[row][column + 1].opened:
                    self.openTiles(row, column + 1)
                if down and not self._board[row + 1][column].opened:
                    self.openTiles(row + 1, column)
                if left and not self._board[row][column - 1].opened:
                    self.openTiles(row, column - 1)
                if up and right and not self._board[row - 1][column + 1].opened:
                    self.openTiles(row - 1, column + 1)
                if down and right and not self._board[row + 1][column + 1].opened:
                    self.openTiles(row + 1, column + 1)
                if down and left and not self._board[row + 1][column - 1].opened:
                    self.openTiles(row + 1, column - 1)
                if up and left and not self._board[row - 1][column - 1].opened:
                    self.openTiles(row - 1, column - 1)

        
        
    # check for content
    def animate(self, buttons):
        pass

    def tileContent(self):   
        
        
        for row in range(self.rows):
            for column in range(self.columns):
                bombCounter = 0 
                if not(self._board[row][column].bomb):
                    
                    up = True if row > 0 else False
                    down = True if row < self.rows - 1 else False
                    left = True if column > 0  else False
                    right = True if column < self.columns - 1  else False
                    if up:
                        bombCounter += 1 if self._board[row - 1][column].bomb else 0
                    if up and left:
                        bombCounter += 1 if self._board[row - 1][column - 1].bomb else 0
                    if up and right:
                        bombCounter += 1 if self._board[row - 1][column + 1].bomb else 0
                    if left:
                        bombCounter += 1 if self._board[row][column - 1].bomb else 0
                    if right:
                        bombCounter += 1 if self._board[row][column + 1].bomb else 0
                    if down and left:
                        bombCounter += 1 if self._board[row + 1][column - 1].bomb else 0
                    if down:
                        bombCounter += 1 if self._board[row + 1][column].bomb else 0
                    if down and right:
                        bombCounter += 1 if self._board[row + 1][column + 1].bomb else 0
                self._board[row][column].setNeighbours(bombCounter)    
                
                    

