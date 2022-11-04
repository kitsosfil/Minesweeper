import pygame
import pygame_menu


from enum import Enum

class Difficulty(Enum):
    EASY = 10
    MEDIUM = 40
    HARD = 99

class BoardTiles(Enum):
    EASY = (9,9)
    MEDIUM = (15,15)
    HARD = (22,35)

class tileSize():
    def __init__(self, size = 40):
        self.size = size
        self.image = pygame.image.load('img/empty-block.png')


class Menu():
    #def __init__(self, mode = Difficulty.EASY, size = BoardTiles.EASY.value ):
    def __init__(self):
        self.mode = Difficulty.EASY.value
        self.size = BoardTiles.EASY.value
       
class Game():
    
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.settings = Menu()
        self.resolution = self.height, self.width = 640,400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.resolution, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_cleanup(self):
        pygame.quit()
  
    def on_loop(self):
        pass
    def on_render(self):
        pass

    def run(self):
        if self.on_init() == False:
            self._running = True

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    newGame = Game()
    newGame.run()