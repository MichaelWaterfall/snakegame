import pygame, time, random

snakeSpeed = 15

windowX = 720
windowY = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

# Music/Sound
music = pygame.mixer.music.load('./Audio/snakeGameMusic.mp3')
pygame.mixer.music.play(-1)
prizeSound = pygame.mixer.Sound('./Audio/prizeWon.mp3')

pygame.display.set_caption('Michael Waterfall Snake Game')
gameWindow = pygame.display.set_mode((windowX, windowY))

fps = pygame.time.Clock()

snakePosition = [100, 50]

# Defining first 4 blocks of snake body
snakeBody = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Prize position
prizePosition = [random.randrange(1, (windowX//10)) * 10, 
                  random.randrange(1, (windowY//10)) * 10]

prizeSpawn = True

# Setting default snake direction towards
# Right
direction = 'RIGHT'
changeTo = direction

score = 0

def showScore(choice, color, font, size):
  
    scoreFont = pygame.font.SysFont(font, size)
    
    scoreSurface = scoreFont.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    scoreRect = scoreSurface.get_rect()
    
    # displaying text
    gameWindow.blit(scoreSurface, scoreRect)

# game over function
def gameOver():
  
    # creating font object myFont
    myFont = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    getOverSurface = myFont.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    gameOverRect = getOverSurface.get_rect()
    
    # setting position of the text
    gameOverRect.midtop = (windowX/2, windowY/4)
    
    # blit will draw the text on screen
    gameWindow.blit(getOverSurface, gameOverRect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.key == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key == pygame.K_RIGHT:
                changeTo = 'RIGHT'

    if changeTo == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changeTo == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snakePosition[1] -= 10
    if direction == 'DOWN':
        snakePosition[1] += 10
    if direction == 'LEFT':
        snakePosition[0] -= 10
    if direction == 'RIGHT':
        snakePosition[0] += 10

    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == prizePosition[0] and snakePosition[1] == prizePosition[1]:
        pygame.mixer.Sound.play(prizeSound)
        score += 10
        prizeSpawn = False
    else:
        snakeBody.pop()
        
    if not prizeSpawn:
        prizePosition = [random.randrange(1, (windowX//10)) * 10, 
                          random.randrange(1, (windowY//10)) * 10]
        
    prizeSpawn = True
    gameWindow.fill(black)
    
    for pos in snakeBody:
        pygame.draw.rect(gameWindow, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(gameWindow, white, pygame.Rect(
        prizePosition[0], prizePosition[1], 10, 10))

    if snakePosition[0] < 0 or snakePosition[0] > windowX-10:
        gameOver()
    if snakePosition[1] < 0 or snakePosition[1] > windowY-10:
        gameOver()

    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameOver()

    showScore(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snakeSpeed)