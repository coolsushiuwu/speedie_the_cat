import pygame
pygame.init()
screen= pygame.display.set_mode((1000,600))
pygame.display.set_caption('speedie the cat')
screen.fill('deepskyblue4')
clock = pygame.time.Clock()
space_background= pygame.Surface((1000,500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(space_background,(0,0))

    pygame.display.update()
    clock.tick(60)
