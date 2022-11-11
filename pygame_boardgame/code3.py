import pygame, sys
from pygame.math import Vector2


class Player():
    def __init__(self):
        self.worldSize = Vector2(10,10)
        self.playerPos = Vector2(0,0)
    
    def update(self, movePlayer):
        self.playerPos += movePlayer
        
    def move(self):
        pass

    
    
class Main():
    def __init__(self):
        pygame.init()
        
        self.player = Player()
        
        self.cellSize = Vector2(64,64)
        self.windowSize = self.player.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(self.windowSize.x), int(self.windowSize.y)))
        
        self.playerTexture = pygame.image.load('player2.png').convert()
        self.playerTexture.set_colorkey((255,255,255))
        
        
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.movePlayer = Vector2(0,0)
        
    def inputs(self):
        self.movePlayer = Vector2(0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.movePlayer.x = 1
                elif event.key == pygame.K_LEFT:
                    self.movePlayer.x = -1

    
    def update(self):
        self.player.update(self.movePlayer)
    
    def render(self):
        self.window.fill((0,0,0))
        # for x in range(int(self.player.worldSize.x)):
        #     print(x)
        #     for y in range(int(self.player.worldSize.y)):
        #         pygame.draw.rect(self.window, (255,0,0), (x,y, self.cellSize.x, self.cellSize.y))
        spritePoint = self.player.playerPos.elementwise()*self.cellSize
        # texturePoint = Vector2(1,0).elementwise()*self.cellSize
        # textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
        self.window.blit(self.playerTexture, spritePoint)
        pygame.display.update()
        
        
    def run(self):
        while self.running:
            self.inputs()
            self.update()
            self.render()
            self.clock.tick(60)    
    
if __name__ == '__main__':
    program = Main()
    program.run()