from enum import Enum

class Difficulty(Enum):
    EASY = 10
    MEDIUM = 40
    HARD = 99

class BoardTiles(Enum):
    EASY = (9,9)
    MEDIUM = (16,16)
    HARD = (16, 30)

class Menu():
    # Initialize Game Parameteres
    def __init__(self, mode = Difficulty.HARD.value, dimensions = BoardTiles.HARD.value):
        self.__mode = mode
        self.__dimensions = dimensions
        self.title = 'Menu'

    @property
    def dimensions(self):
        return self.__dimensions

    @property
    def mode(self):
        return self.__mode
        

    
    # Change parameters though Menu (difficulty, Board size)

