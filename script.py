import pygame
import time
import random

snakeSpeed = 15

windowX = 720
windowY = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Michael Waterfall Snake Game')
gameWindow = pygame.display.set_mode((windowX, windowY))

fps = pygame.time.Clock()

snakePosition = [100, 50]

snakeBody = [ 
                [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

prizePosition = [random.randrange(1, (windowX//10)) * 10,
                  random.randrange(1, (windowY//10)) * 10]

prizeSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

def showScore(choice, color, font, size):
    scoreFront = pygame.font.SysFont(font, size)
    scoreSurface = scoreFront.render('Score: ' + str(score), True, color)
    ScoreRect = scoreSurface.get_rect()
    gameWindow.blit(scoreSurface, ScoreRect)

def gameOver():
    myFont = pygame.font.SysFont('times new roman', 50)
    gameOverSurface = myFont.render('Your score is : ' + str(score), True, red)

    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (windowX/2, windowY/4)
    gameWindow.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

