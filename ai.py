from character import Character
import random

class AI():

    name = None
    hp = None
    current_image = None 
    pygame = None

    walk = []
    z_attack = []
    x_attack = []
    c_attack = []
    
    left = False
    right = False
    z_att = False
    x_att = False
    c_att = False

    x = 0
    y = 0
    hitbox = 0
    
    walkCount = 0
    z_att_count = 0
    x_att_count = 0
    c_att_count = 0

    screen = None

    def __init__(self, name, hp, pygame, screen, x, y):
        self.name = name
        self.hp = hp
        self.pygame = pygame
        self.x = x
        self.y = y
        self.screen = screen

        self.load_sprites()

    def load_sprites(self):
        self.walk = [self.pygame.image.load(f'Sprites/{self.name}/walk/walk0.png'),
                self.pygame.image.load(f'Sprites/{self.name}/walk/walk1.png'),
                self.pygame.image.load(f'Sprites/{self.name}/walk/walk2.png')]

        self.z_attack = [self.pygame.image.load(f'Sprites/{self.name}/attacks/z_attack/z_attack0.png')]

        self.x_attack = [self.pygame.image.load(f'Sprites/{self.name}/attacks/x_attack/x_attack1.png')]

        self.current_image = self.pygame.image.load(f'Sprites/{self.name}/player.png')


            
    def move(self, target_x):
        
        if self.walkCount > 2:
            self.walkCount = 0

        if target_x > self.x and self.x < 1220:
            self.x += 1.5

            self.screen.blit(self.walk[self.walkCount], (self.x, self.y))

            self.walkCount+=1
        elif target_x < self.x and self.x > 0:
            self.x -= 1.5        
            self.screen.blit(self.pygame.transform.flip(self.walk[self.walkCount], True, False), (self.x, self.y))

            self.walkCount+=1
        else:

            self.screen.blit(self.current_image, (self.x, self.y))

