from character import Character
from ai import AI
from sm_projectile import SM_Projectile

import pygame
import sys


def main():
    pygame.init()
    
    pygame.mixer.init()
    pygame.mixer.music.load('amongus.wav')
    pygame.mixer.music.play()
    
    fps = 60
    fpsClock = pygame.time.Clock()

    screen = pygame.display.set_mode([1200, 620])
    
    bg = pygame.image.load("bg.jpg")
    projectiles = []
    x=0
    y=320
    
    player = Character('average_joe', 100, pygame, screen, x, y)

    cpu = AI('socialmedia_addict', 100, pygame, screen, 1000, y)
    
    while True:
        screen.blit(bg, (0,0))

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

            if player.name == 'socialmedia_addict':
                projectiles.append(SM_Projectile(player.x, 350, pygame, screen))

            player.z_att_count+=1


        elif player.x_att:
            if player.x_att_count >= 1:
                player.x_att_count = 0

            screen.blit(player.x_attack[player.x_att_count] ,(player.x,player.y))

            player.x_att_count+=1

        else:
            screen.blit(player.current_image, (player.x,player.y))
        
        hitbox_2 = pygame.draw.rect(screen, (255,0,0), (cpu.x, cpu.y, 64, 220), 0)
        hitbox = pygame.draw.rect(screen, (225, 0, 0), (player.x, player.y, 64, 220), 0)
        
        cpu.move(player.x)

        if (player.x_att or player.z_att):
            if collision_check(hitbox, hitbox_2):
                cpu.x = 1000
        for proj in projectiles:
            proj.update()
            if collision_check(proj.hitbox, hitbox_2):
                cpu.x = 1000

        pygame.display.update()

def collision_check(src, target):
    return src.colliderect(target)

if __name__ == '__main__':
    main()
