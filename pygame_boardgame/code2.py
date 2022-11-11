
import pygame
import sys
from pygame.locals import *
import os


class GameState():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def update(self, moveX, moveY):
        self.x += moveX
        self.y += moveY


class Tiles():
    def __init__(self, surface, width, height, numberOfTiles):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.surface = surface
        self.numberOfTiles = numberOfTiles
        self.tileList = self.render()
        
    
    def render(self):
        tempList = []
        x = 0
        y = 0
        xincrement = self.width//self.numberOfTiles
        yincrement = self.height//self.numberOfTiles
        #while len(self.tileList) != numberOfTiles**2:
        tile = pygame.draw.rect(self.surface, (255,0,0), (x,y, self.width//self.numberOfTiles, self.height//self.numberOfTiles),1)
        tempList.append(tile)
        
        while tempList[-1].x <= self.width and tempList[-1].y <= self.width:
            if x < self.width:
                tile = pygame.draw.rect(self.surface, (255,0,0), (x,y, self.width//self.numberOfTiles, self.height//self.numberOfTiles),1)
                print(f'X: {tile.x}, Y: {tile.y}')
                tempList.append(tile)
                x += xincrement
            if x >= self.width:
                pygame.draw.rect(self.surface, (255,0,0), (x,y, self.width//self.numberOfTiles, self.height//self.numberOfTiles),1)
                tempList.append(tile)
                x = 0
                y += yincrement
    
        return tempList




class Main():
    def __init__(self, width, height, boardtiles):
        pygame.init()
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width,height))
        self.numberOfTiles = boardtiles
        self.gameboard = Tiles(self.window, width, height, boardtiles)
        self.gameState = GameState(37,37)
        self.startingPos = self.gameboard.tileList[0].center
        # self.gameboard.tileList[0].center[0] = self.gameState.x
        # self.gameboard.tileList[0].center[1] = self.gameState.y
        print(self.startingPos)

        self.running = True
        self.moveX = 0
        self.moveY = 0
        
    def inputs(self):
        self.moveX = 0
        self.moveY = 0
        self.step = self.gameboard.tileList[2].x - self.gameboard.tileList[1].x
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
            
                elif event.key == pygame.K_RIGHT:
                    self.moveX = self.step
                elif event.key == pygame.K_LEFT:
                    self.moveX = -self.step
                elif event.key == pygame.K_DOWN:
                    self.moveY = self.step
                elif event.key == pygame.K_UP:
                    self.moveY = -self.step
            # elif  event.type == pygame.KEYUP:
            #     print('KEY UP')
            #     self.moveX = 0
            #     self.moveY = 0
                
            
    def update(self):
        self.gameState.update(self.moveX, self.moveY)
        
    def render(self):
        self.window.fill((0,0,0))
        x = self.gameState.x
        y = self.gameState.y
        player = pygame.draw.rect(self.window, (0,0,255), (x,y,40,40))
        player.center = self.gameboard.tileList[0].center
        print(player.center, self.gameboard.tileList[0].center)
        
        for tile in self.gameboard.tileList:
            pygame.draw.rect(self.window, (255,0,0), tile, 4)
            
        pygame.display.update()
        
    def run(self):
        while self.running:
            self.inputs()
            self.update()
            self.render()
            self.clock.tick(60)
            
            
if __name__ == '__main__':
    go = Main(600,600,8)
    go.run()