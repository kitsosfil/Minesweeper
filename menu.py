from enum import Enum
import pygame

img = pygame.image.load('img/sprite100.gif') # 144 x 91


class MenuIcons(Enum):
    IDLE = pygame.transform.scale(img.subsurface(0, 55, 26, 26),(50,50))
    HAPPY_CLICKED = pygame.transform.scale(img.subsurface(26, 55, 26, 26),(50, 50))
    CLICKED = pygame.transform.scale(img.subsurface(52, 55, 26, 26),(50, 50))
    LOSER = pygame.transform.scale(img.subsurface(78, 55, 26, 26),(50, 50))
    WINNER = pygame.transform.scale(img.subsurface(104, 55, 26, 26),(50, 50))
    
class Digits(Enum):    
    zero = pygame.transform.scale(img.subsurface(0, 0, 13, 23), (28,50))
    one = pygame.transform.scale(img.subsurface(13, 0, 13, 23), (28,50))
    two = pygame.transform.scale(img.subsurface(26, 0, 13, 23), (28,50))
    three = pygame.transform.scale(img.subsurface(39, 0, 13, 23), (28,50))
    four = pygame.transform.scale(img.subsurface(52, 0, 13, 23), (28,50))
    five = pygame.transform.scale(img.subsurface(65, 0, 13, 23), (28,50))
    six = pygame.transform.scale(img.subsurface(78, 0, 13, 23), (28,50))
    seven = pygame.transform.scale(img.subsurface(91, 0, 13, 23), (28,50))
    eight = pygame.transform.scale(img.subsurface(104, 0, 13, 23), (28,50))
    nine = pygame.transform.scale(img.subsurface(117, 0, 13, 23), (28,50))
    #dash = img.subsurface(130, 13, 13, 23)

class Margins(Enum):
    row = img.subsurface(40, 81, 16, 10)
    column = img.subsurface(134, 39, 10, 32)
    topLeft = img.subsurface(0, 81, 10, 10)
    topRight = img.subsurface(10, 81, 10, 10)
    bottomLeft = img.subsurface(20,81,10,10)
    bottomRight = img.subsurface(30,81,10,10)
    jointl = img.subsurface(56,81,10,10)
    jointr = img.subsurface(66,81,10,10)

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
    digits = {index: digit.value for (index, digit) in enumerate(Digits)} 
    def __init__(self, mode = Difficulty.HARD.value, dimensions = BoardTiles.HARD.value):
        self.__mode = mode
        self.__dimensions = dimensions
        self.__face = 0
        self.__seconds = 0        
        self.__flagged = self.__mode
        self.__displayDimensions = (84,50)
        self.title = 'Menu'
        self.faces = self.getFaces()
        self.timer_event = pygame.USEREVENT + 1
    
    @property
    def dimensions(self):
        return self.__dimensions

    @property
    def mode(self):
        return self.__mode

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def clockTick(self, value):
        if self.__seconds < 999:
            self.__seconds += value
            #self.drawClock()

    @property
    def flagged(self):
        return self.__flagged
    
    @flagged.setter
    def found(self, value):
        if 0 < self.found < 99:
            self += value
            #self.drawBombCounter()
    @property
    def getFace(self):
        return self.faces[self.__face].value

    @getFace.setter
    def getFace(self,value):
        self.__face = value

    def getFaces(self):
        faces = []
        for icon in MenuIcons:faces.append(icon)
        return faces

    def drawClock(self):
        clock = pygame.Surface(self.__displayDimensions)
        for index, digit in enumerate([self.digits[i] for i in list(map(int,(self.seconds // 100, self.seconds // 10 % 10, self.seconds % 10)))]):
           pygame.Surface.blit( clock, digit, (index * (self.__displayDimensions[0] // 3) , 0) )        
        return clock
        
        
        
    def drawBombCounter(self):
        bombCounter = pygame.Surface(self.__displayDimensions)
        for index, digit in enumerate([self.digits[i] for i in list(map(int,(self.found // 100, self.found // 10 % 10, self.found % 10)))]):
           pygame.Surface.blit( bombCounter, digit, (index * (self.__displayDimensions[0] // 3) , 0) )
        return bombCounter
        

    def on_render(self,menuSurface, margin):
        menuSurface.fill((210,210,210))
        menuSurface.blit(self.drawBombCounter(), (margin, margin))
        menuSurface.blit(self.getFace,((menuSurface.get_width() // 2) - 20, margin))
        menuSurface.blit(self.drawClock(), (menuSurface.get_width() - self.__displayDimensions[0] - margin, margin))
        self.drawBombCounter()
        # draw margins
        # topleft       ---         rows        ---      topright
        # column | bombcounter |    face    |   timer   | column
        # joinl         ---         rows        ---       joinr
        #
        #                           board
        #
        # bottomleft    ---         rows        ---     bottomright
        
        # big rect and draw rect in rect
        # 
        # menu list [3 rows][5 columns] with dynamic column width and fixed height
        # scale them to fit using dynamic proportions
        # keep borders width in place
        # 10px --- 50px -- stretch face -- 50px -- 10px
        #menuSurface = pygame.Surface((600,800))
        # menuMap = [ [ [None] for _ in range(5)] for _ in range(3) ]
        return menuSurface


    
# Change parameters though Menu (difficulty, Board size)
# def run(self):
#     pygame.init()
#     self.running = True

#     while self.running:
#         self.surface = pygame.display.set_mode((600,400), pygame.RESIZABLE)

#         self.surface.blit(self.drawMenu(),(0,0))
#         # for index, face in enumerate(self.faces):
#         #     self.surface.blit(face,(index * 25,0))  
#         for event in [pygame.event.wait()]+pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             pygame.display.update()
#     pygame.quit()
        

if __name__ == "__main__":
    menu = Menu()
    menu.run()