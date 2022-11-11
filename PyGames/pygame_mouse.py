import pygame, sys
from pygame.locals import *
import random
import math

WIDTH = 400
HEIGHT = 400

BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (120,30,200)
PINK = (200,30,120)

pygame.init()

clock = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
mx, my = mouse[0], mouse[1]

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen_rect = screen.get_rect()
screen.fill(BLACK)


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.image.load('blomma1.png')
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = w
        self.rect.y = h
        self.rect.center = (self.x, self.y)
        self.speed = 2
        self.posx = mx - self.rect.x
        self.posy = my - self.rect.y
        self.scale_step = (10,10)
        
    def _update_surf(self):  
        self.image = pygame.transform.scale(self.image, self.scale_step) 
        self.rect = self.image.get_rect()
        
    def update(self):
        self._update_surf()
    

box1 = Box(50,50, 50,50)
box_sprites = pygame.sprite.Group()
box_sprites.add(box1)
 
font_arial = pygame.font.SysFont('Arial', 15)

while True:
    screen.fill(BLACK)      
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    nl = box1.rect.y - mouse[1]
    ms = box1.rect.x - mouse[0]
    angle = math.atan2(nl, ms)
    cos = math.cos(angle)
    degr = math.degrees(cos)    
    mouse = pygame.mouse.get_pos()
    
    mouse_cords = font_arial.render(str(mouse[0]) + "/" + str(mouse[1]), True, WHITE)
    screen.blit(mouse_cords, (WIDTH-60, HEIGHT-35))
    
    

    box1.update() 
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)