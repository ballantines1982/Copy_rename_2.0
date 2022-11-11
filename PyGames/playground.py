import pygame, sys, os
from pygame.locals import *
import random

score = 0

pygame.init()

SIZE = 600,600
screen = pygame.display.set_mode(SIZE)
screen.get_rect()
background = pygame.image.load('background.jpg')

clock = pygame.time.Clock()
drop_locX_global = [0,60,120,180,240,300,360,420,480,540]

def clear_scr():
    """Rensar terminalen"""
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
def collide_if_not_self(left, right):
    if left != right:
        return pygame.sprite.collide_rect(left, right)
    return False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20,30))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.mouse = pygame.mouse.get_pos()
        self.rect.x = 0
        self.rect.y = 600-30-30
        
    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.rect.x = self.mouse[0]
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((45,45))
        self.rect = self.image.get_rect()
        self.image.fill((random.randint(100,255),random.randint(100,255),random.randint(100,255)))
        self.drop_locx = drop_locX_global
        self.rect.x = self.dropLoc()
        self.rect.y = -45
        self.speed = random.randint(3,5)
        self.acc = self.speed 
        
        
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y >= 645:
            self.kill()


    def dropLoc(self):
        dropLoc = random.choice(drop_locX_global)
        drop_locX_global.remove(dropLoc)
        return dropLoc    
    


                
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SIZE[0], 30))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = 645
    
    def update(self):
        pass
                      
enemy_list = []
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
ground_sprite = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
ground = Ground()
all_sprites.add(ground)
ground_sprite.add(ground)

enemy_count = 0

prev_time = pygame.time.get_ticks()


while True:
    screen.blit(background, (0,0))
    clear_scr()
    print("Score: " + str(score))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
   
    current_time = pygame.time.get_ticks()
    if current_time - prev_time > 150 and len(enemy_sprites) <= 50:
        prev_time = current_time
        enemy = Enemy()
        enemy_count += 1
        #print("Enemy Count: " +str(enemy_count))
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)
        #enemy_list.append(enemy)
        
    for enemy in enemy_sprites:    
        if pygame.sprite.spritecollide(enemy, enemy_sprites, True, collide_if_not_self):
            pass

    for enemy in enemy_sprites:
        for ground in ground_sprite:
            if pygame.sprite.collide_rect(enemy, ground):
                score += 1
                enemy.kill()
                       


        
    if len(drop_locX_global) == 0:
        drop_locX_global = [0,60,120,180,240,300,360,420,480,540]

        

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    
