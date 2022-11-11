import pygame, sys
from pygame.locals import *

WHITE = 255,255,255
BLACK = 0,0,0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("up.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        if pygame.key.get_pressed()[K_LEFT] and not self.rect.left <= 0:
            self.rect.x += -5
        if pygame.key.get_pressed()[K_RIGHT] and self.rect.right < screenWidth:
            self.rect.x += 5


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([3,9])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y -= 10
        
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.gif")
        self.rect = self.image.get_rect()
        self.rect.x = screenWidth-20
        self.rect.y = 20
        
    def update(self):
        self.rect.x -=5
        if self.rect.x < 0:
            self.rect.x +=5
        elif self.rect.x > screenWidth:
            self.rect.x -=5
            

pygame.init()

screenWidth = 300
screenHeight = 700
screen = pygame.display.set_mode([screenWidth, screenHeight])

clock = pygame.time.Clock()

all_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
        
player = Player()
all_sprite_list.add(player)

enemy = Enemy()
all_sprite_list.add(enemy)
enemy_list.add(enemy)

player.rect.y = screenHeight-50
player.rect.x = screenWidth/2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if pygame.key.get_pressed()[K_SPACE]:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprite_list.add(bullet)
            bullet_list.add(bullet)
            
        for bullet in all_sprite_list:
            if bullet.rect.y < -10:
                all_sprite_list.remove(bullet)
                bullet_list.remove(bullet)
    
    
    screen.fill(BLACK)        
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    
    
    pygame.display.flip()            
    clock.tick(60)