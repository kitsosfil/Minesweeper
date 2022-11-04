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
        print(list(map(lambda d: d* self._board._board[0][0].size, self._settings.dimensions)))
        w, h = list(map(lambda d: d* self._board._board[0][0].size, self._settings.dimensions))
        return (w,h)
        #self._surface.fill((210,210,210))

        # Minesweeper will consist of Menu(height) + Board
        # return self._board._re solution

    # def createMenu(self):
    #     return pygame_menu.Menu('Settings',self._board._resolution, 100, theme = pygame_menu.themes.THEME_BLUE)

    # Handle events
    def on_event(self, event):
        # poll = pygame.event.poll()
        # print(pygame.event.wait())
        buttons = pygame.mouse.get_pressed()
        pressed = ""
        action = ""
        if event.type == pygame.QUIT:
            self._running = False
        # Button Pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Block MouseMotion -> pygame.event.set_blocked(1024)
            # Allow MouseMotion -> pygame.event.set_allowed(1024)
            # pygame.event.wait() ???
            if event.button == 1:
                # Action: Open Tile
                action = "Pressed | Open Tile "
                column, row = (event.pos[0] // self._board.tileSize.globalSize, event.pos[1] // self._board.tileSize.globalSize)
                pressed += "m1"
            if event.button == 3:
                # Action: Flag Tile
                action = "Pressed | Flag Tile"
                column, row = (event.pos[0] // self._board.tileSize.globalSize, event.pos[1] // self._board.tileSize.globalSize)
                pressed += "m2"
            print(action, pressed, column, row)

        # Button Released  
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Action: Open Tile
                action = "Released | Open Tile"
                column, row = (event.pos[0] // self._board.tileSize.globalSize, event.pos[1] // self._board.tileSize.globalSize)
            if event.button == 3:
                # Action: Flag Tile
                action = "Released | Flag Tile"
                column, row = (event.pos[0] // self._board.tileSize.globalSize, event.pos[1] // self._board.tileSize.globalSize)
            
            print(action, pressed, column, row)
            
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
        w,h = self._settings.dimensions
        height = (h/w) * width
        self._board.adjustTile(width/w)
        self.UI = pygame.display.set_mode((width,height), pygame.RESIZABLE)# | pygame.NOFRAME | pygame.SCALED) 
        

    def on_render(self):
        surface = self._board.on_render(self.createFake())
        self.UI.blit(pygame.transform.scale(surface, self.UI.get_rect().size), (0,0))     
        
       

    def run(self):
        
        pygame.init()
        while self._running:
            actions = []
            for event in [pygame.event.wait()]+pygame.event.get():
                actions.append(self.on_event(event)) 
            self.on_render()
            pygame.display.flip()
            print(actions)            
        pygame.quit()


if __name__ == "__main__":
    Game = Minesweeper()
    Game.run()