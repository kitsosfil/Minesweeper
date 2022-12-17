# #global size = 30
# class Tile(object):
#     size = 30

#     def __init__(self):
#         self.value = False

#     def changesize(self, value):
#         self.size = value

# if __name__ == "__main__":
#     a = Tile()
#     b = Tile()
#     print(a.size, b.size, a.value, b.value)
#     Tile.size = 45
#     a.value = True
#     print(a.size, b.size, a.value, b.value)
import pygame

class Board(object):
    def __init__(self):
        self.__clicked = False
        self._observers = []

    @property 
    def click(self):
        return self.__clicked
        #return self.__icon[0] if self.__toggle else self.__icon[0]
    
    @click.setter
    def action(self,value):
        self.__clicked 
        
class Tile(object):
    def __init__(self, board):
        self.board = board 
        self.__icon = ["Happy", " Sad"]
        self.__toggle = False

pygame.init()
window = pygame.display.set_mode((200, 200))
#clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
counter = 10
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)


run = True
while run:
    #clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, (0, 128, 0))

    window.fill((255, 255, 255))
    text_rect = text.get_rect(center = window.get_rect().center)
    window.blit(text, text_rect)
    pygame.display.flip()