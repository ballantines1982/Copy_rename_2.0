import pygame, sys
from pygame.locals import *
import random
import itertools

from pygame.sprite import Sprite

screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight])

BLACK = 0,0,0
WHITE = 255,255,255
box_directions = [[2,2], [-2,-2], [2,-2], [-2,2]]

score_num = 0 
bullets_shot = 1
bullets_hit = 1

all_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
text_sprites = pygame.sprite.Group()
NEWBOX = pygame.USEREVENT + 0

clock = pygame.time.Clock()

class Main():
    def __init__(self):
        self.screenWidth = 400
        self.screenHeight = 400
        self.screen = pygame.display.set_mode(self.screenWidth, self.screenHeight)
    
    def run(self):
        pass        
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((12,12))
        self.rect = self.image.get_rect()
        self.rect.y = screenHeight-20
        self.rect.x = screenWidth/2
        self.image.fill(WHITE)

    def update(self):
        if pygame.key.get_pressed()[K_RIGHT] and not self.rect.right > screenWidth:
            self.rect.x += 10
        if pygame.key.get_pressed()[K_LEFT] and not self.rect.x == 0:
            self.rect.x += -10

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((3,8))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
    def update(self):
        self.rect.y += -20
        if self.rect.top < 0: self.kill()
    

class Box(pygame.sprite.Sprite):
    def __init__(self, image=None, direction=None):
        super().__init__()
        self.image = pygame.image.load("blomma1.png")
        self.rect = self.image.get_rect()
        self.hp = 5
        self.rect.y = random.randint(20,screenHeight*0.75)
        self.rect.x = random.randint(20,screenWidth)
        self.direction = direction if direction else random.choice([[2,2], [-2,-2], [2,-2], [-2,2]])

    def update(self):
        pass
    
    
class Text(pygame.sprite.Sprite):
    def __init__(self, text, color, size):
        super().__init__()
        self.fontImpact = pygame.font.SysFont('Impact', size)
        self.renderFont = self.fontImpact.render(text, True, color)
        self.rect = self.renderFont.get_rect()
        self.rect.center = (screenWidth//2, screenHeight//2)
        

pygame.init()

player = Player()
all_sprites.add(player)
player_sprites.add(player)
        
for i in range(10):
    box = Box()
    box.rect.move(random.choice(box_directions))
    all_sprites.add(box)
    box_sprites.add(box)

prev_time = pygame.time.get_ticks()

#pygame.time.set_timer(NEWBOX, 1000)

game_run = True

while game_run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == NEWBOX:
            newbox = Box()
            newbox.rect.move(random.choice(box_directions))
            all_sprites.add(newbox)
            box_sprites.add(newbox)
    
    precicion = round(bullets_hit / bullets_shot  * 100, 2)
    
    score = Text('Score: ' + str(score_num), (255,255,255), 20)
    prec_text = Text("Precicion " +str(precicion)+ "%", (255,255,255), 20)
    prec_text.rect.x = screenWidth-130
    prec_text.rect.y= 0
    score.rect.x = 0
    score.rect.y = 0
    screen.fill(BLACK)
    
    if pygame.key.get_pressed()[K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - prev_time > 75:
            prev_time = current_time 
            bullet = Bullet()
            bullet_sprites.add(bullet)
            all_sprites.add(bullet)
            bullet.rect.x = player.rect.x     
            bullet.rect.y = player.rect.y
            bullets_shot += 1
    
    for box in box_sprites:
        for bullet in bullet_sprites:
            if pygame.sprite.collide_rect(bullet, box):
                box.hp -= 1

                bullets_hit += 1
                bullet.kill()
                
                if box.hp == 0:
                    box.kill()
                    score_num += 1

    for boxes in box_sprites:
        if boxes.rect.right > screenWidth and boxes.direction == box_directions[0]:
            boxes.direction = box_directions[3]
        elif boxes.rect.right > screenWidth and boxes.direction == box_directions[2]:
            boxes.direction = box_directions[1]

        if boxes.rect.top < 0 and boxes.direction == box_directions[2]:
            boxes.direction = box_directions[0]
        elif boxes.rect.top < 0 and boxes.direction == box_directions[1]:
            boxes.direction = box_directions[3]

        if boxes.rect.bottom > screenHeight and boxes.direction == box_directions[3]:
            boxes.direction = box_directions[1]
        elif boxes.rect.bottom > screenHeight and boxes.direction == box_directions[0]:
            boxes.direction = box_directions[2]

        if boxes.rect.left < 0 and boxes.direction == box_directions[1]:
            boxes.direction = box_directions[2]
        elif boxes.rect.left < 0 and boxes.direction == box_directions[3]:
            boxes.direction = box_directions[0]
        boxes.rect.move_ip(boxes.direction)
        
    if len(box_sprites) == 0:
        winText = Text('YOU WIN!', (0,255,0), 70)
        screen.blit(winText.renderFont, winText.rect)

    for box in box_sprites:
        for player in player_sprites:
            if pygame.sprite.collide_rect(box, player):
                gameOver = Text('GAME OVER', (255,0,0), 50)
                screen.blit(gameOver.renderFont, gameOver.rect)
                
            
    screen.blit(score.renderFont, score.rect)
    screen.blit(prec_text.renderFont, prec_text.rect)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(30)
    
