class SM_Projectile:
    x = 0
    y = 0
    vel = 2

    pygame = None
    projectile = None
    screen = None
    active = False
    hitbox = None 

    def __init__(self, x, y, pygame, screen):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.screen = screen
        self.hitbox = pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 30, 40), 3) 
        self.projectile = self.pygame.image.load('projectile.jpg')

    def update(self):
        if self.x <= 1200:
            self.x+=self.vel
            self.screen.blit(self.projectile, (self.x, self.y))
            active = True

        else: active = False

