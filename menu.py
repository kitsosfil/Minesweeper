from enum import Enum

class Difficulty(Enum):
    EASY = 10
    MEDIUM = 40
    HARD = 99

class BoardTiles(Enum):
    EASY = (9,9)
    MEDIUM = (15,15)
    HARD = (35,22)

class Menu():
    # Initialize Game Parameteres
    def __init__(self, _mode = Difficulty.HARD.value, _dimensions = BoardTiles.HARD.value):
        self._mode = _mode
        self._dimensions = _dimensions
        self.title = 'Menu'
        
        
        

    
    # Change parameters though Menu (difficulty, Board size)

