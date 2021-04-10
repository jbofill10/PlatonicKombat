from character import Character

import pygame
import sys


def main():
    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode([1280, 720])
    
    x=y=0
    
    player = Character('socialmedia_addict', 100, pygame, x, y)

    while True:
        screen.fill((255,255,255))

        for event in pygame.event.get():
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
        
        player.manage_inputs()

        if player.left or player.right:
            if player.walkCount > 2:
            
                player.walkCount = 0

            if player.right:
        
                screen.blit(player.walk[player.walkCount], (player.x,player.y))
                player.walkCount+=1

            elif player.left:

                screen.blit(pygame.transform.flip(player.walk[player.walkCount], True, False), (player.x, player.y))
                player.walkCount+=1
        elif player.z_att:

            if player.z_att_count >= 1:
                player.z_att_count = 0

            screen.blit(player.z_attack[player.z_att_count] ,(player.x,player.y))
            
            player.z_att_count+=1


        elif player.x_att:
            if player.x_att_count >= 1:
                player.x_att_count = 0

            
            screen.blit(player.x_attack[player.x_att_count] ,(player.x,player.y))

            player.x_att_count+=1

        else:
            screen.blit(player.current_image, (player.x,player.y))
            
        pygame.display.update()

if __name__ == '__main__':
    main()
