import pygame, sys
from pygame.locals import *
import random

pygame.init()

vec = pygame.math.Vector2
width = 400
height = 400
ACC = 0.5
FRIC = -0.08
screen = pygame.display.set_mode((width, height))
screen.fill((0,0,0))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_rect()
        self.image.fill((0,255,0))
        self.pos = vec(10,360)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def move(self):
        self.acc = vec(0,0.5)
        
        if pygame.key.get_pressed()[K_LEFT]:
            self.acc.x = -ACC
        if pygame.key.get_pressed()[K_RIGHT]:
            self.acc.x = ACC

        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
            
        self.rect.midbottom = self.pos 
    
    def jump(self):
        hits = pygame.sprite.spritecollide(player, platform_sprites, False)
        if hits:
           self.vel.y = -15
           
    def update(self):
        hits = pygame.sprite.spritecollide(player, platform_sprites, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0  
                self.pos.y = hits[0].rect.top + 1
       
                
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((random.randint(20,70), random.randint(20,70)))
        self.rect = self.image.get_rect(center = (random.randint(0,width-10),random.randint(0, height-30)))
        self.image.fill((255,0,0))
    
    def move(self):
        pass
        
player_sprites = pygame.sprite.Group()
platform_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

ground = Platform()
ground.image = pygame.Surface((width*10, 20))
ground.rect = ground.image.get_rect(center = (width/2, height-10))
ground.image.fill((0,0,255))
platform_sprites.add(ground)
all_sprites.add(ground)

player = Player()
player_sprites.add(player)
all_sprites.add(player)

for i in range(2):
    plat = Platform()
    platform_sprites.add(plat)
    all_sprites.add(plat)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    if player.rect.right > width-130:
        player.pos.x = width-130
        for sprite in platform_sprites:
            sprite.rect.x -= player.vel.x
    if player.rect.left < 130 and not ground.rect.x == 0:
        for sprite in platform_sprites:
            sprite.rect.x += player.vel.x
    
    screen.fill((0,0,0))
    player.update()
                  
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()
        
    pygame.display.update()
    clock.tick(60)
    
