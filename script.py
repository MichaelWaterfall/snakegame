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