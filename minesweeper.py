import pygame
import pygame_menu

from menu import Menu
from board import Board

from types import SimpleNamespace

class Minesweeper():
    
    def __init__(self):
        # we get difficulty mode and board dimensions
        self._settings = Menu() 
        # we initialize Board 
        self._board = Board(self._settings)
        self.UI = pygame.display.set_caption(" Minesweeper ")
        self.UI = pygame.display.set_mode(self.resolution(), pygame.RESIZABLE)# | pygame.NOFRAME | pygame.SCALED) 
        print(self.resolution())
        self._surface = self.createFake() 
        self._board.on_init(self._surface)
       
        self._running = True
       
    def createFake(self):
        return self.UI.copy()

    def resolution(self):
        # Default resolution 
        h, w = list(map(lambda d: d* self._board._board[0][0].size, self._settings.dimensions))
        #print(f"resolution width: {w}, height: {h}")
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
        elif event.type == pygame.VIDEORESIZE:
            self.resize(event.size)
        # Button Pressed
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Block MouseMotion -> pygame.event.set_blocked(1024)
        #     # Allow MouseMotion -> pygame.event.set_allowed(1024)
        #     if event.button == 1:
        #         # Action: Open Tile
        #         output = {"event" : event.type, "pygameButtons": pygame.mouse.get_pressed(), "row" : event.pos[1] // self._board.tileSize.globalSize, "column": event.pos[0] // self._board.tileSize.globalSize}
        #     if event.button == 3:
        #         output = {"event" : event.type, "pygameButtons": pygame.mouse.get_pressed(), "row" : event.pos[1] // self._board.tileSize.globalSize, "column": event.pos[0] // self._board.tileSize.globalSize}
        
         
        
    # def on_init(self):
    #     image = pygame.transform.scale(pygame.image.load('img/empty-block.png'),(self._board._board[0][0].getSize(),self._board._board[0][0].getSize()))
    #     for i in range(len(self._board._board)):
    #         for j in range(len(self._board._board[0])):                        
    #             self.UI.blit(image, (i* self._board._board[0][0].getSize(), j * self._board._board[0][0].getSize()))
    #     pygame.display.flip()
    
    def resize(self, size):
        width = size[0]
        rows, columns = self._settings.dimensions
        height = (rows/columns) * width
        self._board.adjustTile(width/columns)
        self.UI = pygame.display.set_mode((width,height), pygame.RESIZABLE)# | pygame.NOFRAME | pygame.SCALED) 
        
    def on_render(self):
        surface = self._board.on_render(self.createFake())
        self.UI.blit(pygame.transform.scale(surface, self.UI.get_rect().size), (0,0))     

    def run(self):
        pygame.init()
        buttons = []
        pygame.event.set_blocked(1024)      
        while self._running:
            for event in [pygame.event.wait()]+pygame.event.get():
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons.append(SimpleNamespace(
                        eventID = event.type,
                        buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                        row = int(event.pos[1] // self._board.tileSize),
                        column = int(event.pos[0] // self._board.tileSize)))
                    pygame.event.set_allowed(1024)
                elif event.type == pygame.MOUSEMOTION:
                    buttons.append(SimpleNamespace(
                        eventID = event.type,
                        buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                        row = int(event.pos[1] // self._board.tileSize),
                        column = int(event.pos[0] // self._board.tileSize)))
                elif event.type == pygame.MOUSEBUTTONUP and buttons != []:
                    buttons.append(SimpleNamespace(
                        eventID = event.type,
                        buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                        row = int(event.pos[1] // self._board.tileSize),
                        column = int(event.pos[0] // self._board.tileSize)))
                    
                    self._board.action(buttons)
                    buttons = []
                    pygame.event.set_blocked(1024)      
                elif event.type == pygame.VIDEORESIZE or event.type == pygame.QUIT: 
                    self.on_event(event)
                    buttons = []
                self._board.animate(buttons)
            self.on_render()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    Game = Minesweeper()
    Game.run()