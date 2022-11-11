import sys, pygame
from pygame.locals import *
pygame.init()

size = width, height = 320, 240
speed = [2, 3]
black = 0, 0, 0
blue = 50, 50, 50

screen = pygame.display.set_mode(size)

ball = pygame.image.load("no_move.png")
ballrect = ball.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_DOWN] and not(ballrect.bottom > height or ballrect.right > width):
        ball = pygame.image.load("right_down.png")
        ballrect.y +=2
        ballrect.x +=2
    elif pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_DOWN] and not(ballrect.bottom > height or ballrect.left < 0):
        ball = pygame.image.load("left_down.png")
        ballrect.y +=2
        ballrect.x -=2
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_UP] and not(ballrect.top < 0 or ballrect.right > width):
        ball = pygame.image.load("right_up.png")
        ballrect.y -=2
        ballrect.x +=2
    elif pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_UP] and not(ballrect.top < 0 or ballrect.left < 0):
        ball = pygame.image.load("left_up.png")
        ballrect.y -=2
        ballrect.x -=2
    elif pygame.key.get_pressed()[pygame.K_LEFT] and not ballrect.left < 0:
        ball = pygame.image.load("left.png")
        ballrect.x -=2
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and not ballrect.right > width:
        ball = pygame.image.load("right.png")
        ballrect.x +=2
    elif pygame.key.get_pressed()[pygame.K_DOWN] and not ballrect.bottom > height:
        ball = pygame.image.load("down.png")
        ballrect.y +=2
    elif pygame.key.get_pressed()[pygame.K_UP] and not ballrect.top < 0:
        ball = pygame.image.load("up.png")
        ballrect.y -=2
    else:
        ball = pygame.image.load("no_move.png")
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]
    pygame.time.delay(10)
    screen.fill(black)
    screen.blit(ball, ballrect)
    enemy = pygame.draw.rect(screen, blue,(50,50,50,20))
    pygame.display.flip()