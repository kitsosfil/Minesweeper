from types import SimpleNamespace

import pygame
import pygame_menu


from menu import Menu, Margins
from board import Board

class Minesweeper(): 
    def __init__(self):
        # we get difficulty mode and board dimensions
        self._settings = Menu() 
        # we initialize Board 
        self._board = Board(self._settings)
        
        self._running = True
        self.__margin = 10
        self.__menuHeight = 70
        self.UI = pygame.display.set_caption(" Minesweeper ")
        self.UI = pygame.display.set_mode(self.resolution(), pygame.RESIZABLE) # | pygame.NOFRAME | pygame.SCALED | HWSURFACE|DOUBLEBUF|) 
        
        self.__boardSurface = self.get_board() 
        self.__menuSurface = self.get_menu()
        self._board.on_init(self.boardSurface)
        # states (won, lost, playing, toStart, restart)
        
        # signal for timer
        self.gameOn = False
        # signal to restart game
        self.Restart = False
        self.drawMargins()


    # ===================================== Graphics =====================================
    @property
    def menuSurface(self):
        return self.get_menu()
    
    def get_menu(self):
        # get menu surface
        w, _ = pygame.display.get_surface().get_size()
        return pygame.Surface.copy(self.UI.subsurface(self.__margin, self.__margin , w - 2* self.__margin  ,self.__menuHeight))
        #return self.UI.copy()

    @property
    def boardSurface(self):
        return self.get_board()

    def get_board(self):
        # get board surface
        w, h = self._board.board_resolution()
        return pygame.Surface.copy(self.UI.subsurface(self.__margin, self.__menuHeight + 2 * self.__margin ,w,h))
        #return self.UI.copy()

    def get_board_resolution(self):
        pass

    def resolution(self):
        # Minesweeper will consist of Menu(height) + Board
        # Board Resolution in Pixels
        w, h = self._board.board_resolution()
        # Menu Resolution 
        w += 2 * self.__margin
        h += self.__menuHeight + 3 * self.__margin
        return w,h

    def drawMargins(self):
        w,h = self.UI.get_size()
        # draw corners
        self.UI.blit(Margins.topLeft.value,(0,0))
        self.UI.blit(Margins.topRight.value,(w - self.__margin, 0))
        self.UI.blit(Margins.bottomLeft.value,(0,h - self.__margin))  
        self.UI.blit(Margins.bottomRight.value,(w - self.__margin, h - self.__margin))  
        # draw rows
        for i in range( (w - 2* self.__margin) // 16):
            self.UI.blit(Margins.row.value, (self.__margin + (16* i), 0))
            self.UI.blit(Margins.row.value, (self.__margin + (16* i), self.__margin + self.__menuHeight))
            self.UI.blit(Margins.row.value, (self.__margin + (16* i), h - self.__margin ))

        self.UI.blit(Margins.row.value, ( w - self.__margin - 16 , 0 ) )    
        self.UI.blit(Margins.row.value, ( w - self.__margin - 16 , self.__margin + self.__menuHeight))
        self.UI.blit(Margins.row.value, ( w - self.__margin - 16 , h - self.__margin ))
        # draw menu columns
        for i in range(self.__margin, self.__margin + self.__menuHeight, 32):
            self.UI.blit(Margins.column.value, (0, i))
            self.UI.blit(Margins.column.value, (w - self.__margin , i))
        self.UI.blit(Margins.column.value,(0, self.__margin + self.__menuHeight - 32))
        self.UI.blit(Margins.column.value,(w - self.__margin, self.__margin + self.__menuHeight - 32))
        
        # draw joints
        self.UI.blit(Margins.jointl.value, (0, self.__margin + self.__menuHeight))
        self.UI.blit(Margins.jointr.value, (w - self.__margin, self.__margin + self.__menuHeight))
        
        # draw board columns
        for i in range(self.__margin * 2 + self.__menuHeight , h - self.__margin - 32 , 32):
            self.UI.blit(Margins.column.value, (0, i))
            self.UI.blit(Margins.column.value, (w - self.__margin, i))
        self.UI.blit(Margins.column.value,(0, h - 32 - self.__margin))
        self.UI.blit(Margins.column.value,(w - self.__margin, h - 32 - self.__margin))

    def resize(self, size):
        # here we get the size of pygame.event.RESIZABLE 
        # We keep the aspect ration the same by adjusting the height of the event
        # and adjust the tile size to so that they fit properly the new dimensions
        width = int(size[0])
        rows, columns = self._settings.dimensions
        # adjust tilesize, subtract margins from width
        self._board.adjustTile((width - 2 * self.__margin) / columns )
        # keep aspect ratio on board height and add menu and margin height
        # BOARD HEIGHT(ROWS * TILESIZE) + MENU + MARGINS
        height = ( (rows/columns) * (width - 2 * self.__margin)) + self.__menuHeight + 3 * self.__margin
        self.UI = pygame.display.set_mode((width,height), pygame.RESIZABLE)
        self.drawMargins()
    
    def on_render(self):
        menu = self._settings.on_render(self.get_menu(), self.__margin)
        board = self._board.on_render(self.get_board()) # -> get board surface 
        
        #self.UI.blit(pygame.transform.scale(surface, self.UI.get_rect().size), (0,0))  # -> scale board surface to fit the game frame
        self.UI.blit(menu,(self.__margin, self.__margin))
        #pygame.draw.rect(self.UI,(_,_,_),menu)
        #self.UI.blit(pygame.Surface(menu.width, menu.height),(self.__margin, self.__margin))
        self.UI.blit(board, (self.__margin, self.__menuHeight + 2 * self.__margin ))
    # ===================================== Actions =====================================
    
    def clickOnBoard(self, x,y):
        w,h = self._board.board_resolution()
        # If click on Tile board return True and Tile indexes
        if  self.__margin < x < w + self.__margin and self.__margin * 2 + self.__menuHeight < y < h + self.__margin * 2 + self.__menuHeight:
            return (x - self.__margin, y - (self.__margin * 2) - self.__menuHeight)
        else:
            self.gameRestart(x,y)
            return False
    
    def gameRestart(self, x, y):
        w,_ = self._board.board_resolution()
        if (w//2) + self.__margin - 25 < x < (w//2) + self.__margin + 25 and self.__margin * 2 < y < self.__menuHeight :        
            self.Restart = True
        return

    # Handle events
    def on_event(self, event):
        
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.VIDEORESIZE:
            self.resize(event.size)
        elif event.type == self._settings.timer_event and self.gameOn :
            self._settings.clockTick = 1

        # Button Pressed
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Block MouseMotion -> pygame.event.set_blocked(1024)
        #     # Allow MouseMotion -> pygame.event.set_allowed(1024)
        #     if event.button == 1:
        #         # Action: Open Tile
        #         output = {"event" : event.type, "pygameButtons": pygame.mouse.get_pressed(), "row" : event.pos[1] // self._board.tileSize.globalSize, "column": event.pos[0] // self._board.tileSize.globalSize}
        #     if event.button == 3:
        #         output = {"event" : event.type, "pygameButtons": pygame.mouse.get_pressed(), "row" : event.pos[1] // self._board.tileSize.globalSize, "column": event.pos[0] // self._board.tileSize.globalSize}

    def run(self):
        pygame.init()
        buttons = []
        pygame.event.set_blocked(1024)      
        
        while self._running: 
            for event in [pygame.event.wait()] + pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and (pos := self.clickOnBoard(event.pos[0], event.pos[1]) ):
                    if not self.gameOn: 
                        self.gameOn = True
                        pygame.time.set_timer(self._settings.timer_event, 1000)
                    buttons.append(SimpleNamespace(
                        eventID = event.type,
                        buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                        row = int(pos[1] // self._board.tileSize),
                        column = int(pos[0] // self._board.tileSize)))
                        # pygame.event.set_allowed(1024)
                elif event.type == pygame.MOUSEBUTTONUP and (pos := self.clickOnBoard(event.pos[0], event.pos[1]) ):
                    buttons.append(SimpleNamespace(
                        eventID = event.type,
                        buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                        row = int(pos[1] // self._board.tileSize),
                        column = int(pos[0] // self._board.tileSize)))
                    #self._running = self._board.action(buttons)        
                    self._board.action(buttons)
                    buttons = []
                    pygame.event.set_blocked(1024)
                # elif event.type == pygame.MOUSEMOTION:
                #     buttons.append(SimpleNamespace(
                #         eventID = event.type,
                #         buttons = (pygame.mouse.get_pressed()[0], pygame.mouse.get_pressed()[2]), 
                #         row = int(event.pos[1] // self._board.tileSize),
                #         column = int(event.pos[0] // self._board.tileSize)))      
                elif event.type == pygame.VIDEORESIZE or event.type == pygame.QUIT or event.type == self._settings.timer_event: 
                    self.on_event(event)
                    
                self._board.animate(buttons)
                
                if self.Restart and self.gameOn:
                    print("Game REstart")
                    self._settings = Menu() 
                    self._board = Board(self._settings)
                    self.Restart = False
                    self.gameOn = False
            self.on_render()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    Game = Minesweeper()
    Game.run()

