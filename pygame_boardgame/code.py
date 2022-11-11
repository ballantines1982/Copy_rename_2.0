from turtle import update
from matplotlib.pyplot import spring
import pygame as pg
import sys
from pygame.locals import *

WIDTH = 200
HEIGHT = 200
SIZE = WIDTH, HEIGHT
BOXSIZE = 40

class Player():
    def __init__(self, xpos, ypos):
        self.image = pg.image.load('player.png').convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.step = 57
        

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y
        


class Box():
    def __init__(self, xpos, ypos):
        self.image = pg.image.load('box1.png').convert()
        self.image.set_colorkey((255,255,255))
        #self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos,ypos)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self):
        pass

        

class Main():
    def __init__(self, boardwidth):
        pg.init()
        self.display = pg.display.set_mode(((BOXSIZE+4)*boardwidth, (BOXSIZE+4)*boardwidth))
        self.clock = pg.time.Clock()

        boxes = []
        index = 0
        
        for i in range(boardwidth):
            index+=1
            if index == 1:
                ypos = 25
            else:
                ypos = i * 43 + 25
            for xpos in range(25, (3 + BOXSIZE) * boardwidth, BOXSIZE+3):
                box = Box(xpos, ypos)
                print(box.rect.center)
                print(box.rect.x, box.rect.y)
                boxes.append(box)

        p1 = Player(boxes[0].rect.width//2-10, boxes[0].rect.height//2-10)
        
        pg.display.flip()

        while True:
            pressed_keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if pressed_keys[K_LEFT]:
                    p1.rect.centerx = -57
                if pressed_keys[K_RIGHT]:
                    p1.rect.centerx = 57
                    
                # if event.type == pg.KEYDOWN:
                #     print('KEYDOWN')    
                #     if event.type == pg.K_d:
                #         p1.rect.centery = 57
                #         print('right')
                #     if event.type == pg.K_a:
                #         p1.rect.centery = -57
                #         print('left')
            
            for box in boxes: 
                box.draw(self.display)
                
                
            p1.update
            p1.draw(self.display)    
            pg.display.update()
            self.clock.tick(60)
                
        

        



if __name__ == '__main__':
    Main(8)