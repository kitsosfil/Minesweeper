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
        Tile.changeSize(size)
        self.tileSize = size
        
    
    def board_resolution(self):
        h, w = list(map(lambda d: d * self._board[0][0].size, (self.rows, self.columns)))
        return (w,h)

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
        self._board = [ [ Tile() for _ in range(self.columns) ] for _  in range(self.rows)]
        
        # Add Bombs
        for mine in mines:
            x, y = mine
            self._board[x][y].bomb =  True
        self.tileContent()
        
    def on_init(self, surface):
        size = self._board[0][0].size
        image = self._board[0][0].getTile()
        surf = [[image, (j * size, i * size)]  for i in range(self.rows) for j in range(self.columns) ]
        #for i in range(self.rows):
            #for j in range(self.columns):
                #image = self._board[i][j].getTile()
                #surface.blit(image, (j * size, i * size))        
        surface.blits((surf))
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
        # M1 Click
        if m1 and not m2:
            self.openTiles(row,column)
        # M2
        elif not m1 and m2:
            if not self._board[row][column].open:
                self._board[row][column].flagged = False if self._board[row][column].flagged else True
        # M1 + M2
        elif m1 and m2 and self._board[row][column].open:
            flags = 0
            neighbours = self.checkNeighbours(row, column)
            for neighbour in neighbours:
                if self._board[row + neighbour[0]][column + neighbour[1]].flagged:
                    print(f"row: {neighbour[0]}, column: {neighbour[1]}")
                    flags += 1
            print(f"Flags->{flags} --- Neighbours->{self._board[row][column].neighbours}")
            if flags == self._board[row][column].neighbours:
                for neighbour in neighbours:
                    if not self._board[row + neighbour[0]][column + neighbour[1]].flagged and not self._board[row + neighbour[0]][column + neighbour[1]].open:
                        self.openTiles(row + neighbour[0],column + neighbour[1]) 
            # if is opened and flags around match the value of the square open the squares
        print(f"Is tile Opened: {self._board[row][column].open}")
        # After each action we should return values to update the respectable counters  


    # Return indeces of valid neighbours (handle edges)
    def checkNeighbours(self, row, column):
        """
            0 | 1 | 2
            3 | x | 4
            5 | 6 | 7
        """
        square = []
        up = True if row > 0 else False
        down = True if row < self.rows - 1 else False
        left = True if column > 0 else False
        right = True if column < self.columns - 1  else False 
        square.append((-1,-1)) if up and left else False
        square.append((-1, 0)) if up else False
        square.append((-1, 1)) if up and right else False
        square.append(( 0,-1)) if left else False
        square.append(( 0, 1)) if right else False
        square.append(( 1,-1)) if down and left else False
        square.append(( 1, 0)) if down else False
        square.append(( 1, 1)) if down and right else False
        return square

    # Open tiles on M1
    def openTiles(self, row, column):
        if not self._board[row][column].flagged :
            self._board[row][column].open = True
            if self._board[row][column].neighbours == 0:
                
                up = True if row > 0 else False
                down = True if row < self.rows - 1 else False
                left = True if column > 0 else False
                right = True if column < self.columns - 1  else False 
                
                if up and not self._board[row - 1][column].open:
                    self.openTiles(row - 1, column)
                if right and not self._board[row][column + 1].open:
                    self.openTiles(row, column + 1)
                if down and not self._board[row + 1][column].open:
                    self.openTiles(row + 1, column)
                if left and not self._board[row][column - 1].open:
                    self.openTiles(row, column - 1)
                if up and right and not self._board[row - 1][column + 1].open:
                    self.openTiles(row - 1, column + 1)
                if down and right and not self._board[row + 1][column + 1].open:
                    self.openTiles(row + 1, column + 1)
                if down and left and not self._board[row + 1][column - 1].open:
                    self.openTiles(row + 1, column - 1)
                if up and left and not self._board[row - 1][column - 1].open:
                    self.openTiles(row - 1, column - 1)
            #elif self._board[row][column].bomb == True:
                # pygame.quit()   
    
    # check for content
    def animate(self, buttons):
        pass

    # Assign Tile values after bombs have been set
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