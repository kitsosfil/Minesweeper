import pygame
import pygame_menu

from menu import Menu
from board import Board

class Minesweeper():
    
    def __init__(self):
        # we get difficulty mode and board dimensions
        self._settings = Menu() 
        # we initialize Board 
        self._board = Board(self._settings)
        self.UI = pygame.display.set_caption(" Minesweeper ")
        self.UI = pygame.display.set_mode(self.resolution(), pygame.RESIZABLE)# | pygame.NOFRAME | pygame.SCALED) 
        self._surface = self.createFake() 
        self._board.on_init(self._surface)
       
        self._running = True
       
    def createFake(self):
        return self.UI.copy()

    def resolution(self):
        # Default resolution 
        print(list(map(lambda d: d* self._board._board[0][0].getSize(), self._settings._dimensions)))
        w, h = list(map(lambda d: d* self._board._board[0][0].getSize(), self._settings._dimensions))
        return (w,h)
        #self._surface.fill((210,210,210))

        # Minesweeper will consist of Menu(height) + Board
        # return self._board._re solution

    # def createMenu(self):
    #     return pygame_menu.Menu('Settings',self._board._resolution, 100, theme = pygame_menu.themes.THEME_BLUE)

    # Handle events
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        # get mouse click
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     (event.pos[0] // self._board._board[0][0].getSize(), event.pos[1] // self._board._board[0][0].getSize())
        # video resize
        elif event.type == pygame.VIDEORESIZE:
            self.resize(event.size)
        
    # def on_init(self):
    #     image = pygame.transform.scale(pygame.image.load('img/empty-block.png'),(self._board._board[0][0].getSize(),self._board._board[0][0].getSize()))
    #     for i in range(len(self._board._board)):
    #         for j in range(len(self._board._board[0])):                        
    #             self.UI.blit(image, (i* self._board._board[0][0].getSize(), j * self._board._board[0][0].getSize()))
    #     pygame.display.flip()
    
    def resize(self, size):
        width = size[0]
        w,h = self._settings._dimensions
        height = (h/w) * width
        self._board.adjustTile(width/w)
        self.UI = pygame.display.set_mode((width,height), pygame.RESIZABLE)# | pygame.NOFRAME | pygame.SCALED) 
        

    def on_render(self):
        surface = self._board.on_render(self.createFake())
        self.UI.blit(pygame.transform.scale(surface, self.UI.get_rect().size), (0,0))     
        
       

    def run(self):
        pygame.init()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)                
            self.on_render()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    Game = Minesweeper()
    Game.run()