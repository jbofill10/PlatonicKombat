import pygame
import sys

def main():
    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode([1280, 720])

    player = pygame.image.load('Sprites/player.png')

    while True:
        screen.fill((255,255,255))
        screen.blit(player, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()
