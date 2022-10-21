import pygame

# create a rectable object that has inside an image
image = pygame.image.load('img/empty-block.png')
rect =image.get_rect()
print(image)

pygame.init()

# initiate surface
screen = pygame.display.set_mode(rect.size)

screen.blit(image, rect)
pygame.display.update()


while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()