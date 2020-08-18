'''

 Game with the mouse controls and opposing Artificial Intelligence
 To develop: Ball to be circular
 _Allen
 
'''

import pygame, sys, os
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Number of frames per second. Speed value changed by this
FPS = 230

#Global Variables to be used through our program

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 10

# Assigning the colours to variables for easier programming

BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)
GREEN     = (0,255,0)
BLUE      = (0,0,255)
RED       = (255,0,0)

#Draws the arena the game will be played in.

def drawArena():
    DISPLAYSURF.fill((20,20,20))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS)
    #Draw centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))


#Draws the paddle1
    
def drawPaddle1(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, BLUE, paddle)

#Draws the paddle2
def drawPaddle2(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, RED, paddle)


#draws the ball
    
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, GREEN, ball)  


#moves the ball returns new position
    
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

#Checks for a collision with a wall, and 'bounces' ball off it.
#Returns new direction

def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * -1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY

#Checks is the ball has hit a paddle, and 'bounces' ball off it

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top <= ball.bottom and paddle1.bottom >= ball.top:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top <= ball.bottom and paddle2.bottom >= ball.top:
        return -1
    else: return 1

#Points for Player
    
def checkPointScored(paddle1, ball, score, ballDirX):
    # 1 point for hitting the ball
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top <= ball.bottom and paddle1.bottom >= ball.top:
        score += 1
        return score
    # 5 points for beating the other paddle
    elif ball.right == WINDOWWIDTH - LINETHICKNESS:
        score += 5
        return score
    # if no points scored, return score unchanged
    else: return score

#Points for computer
    
def checkPointScored2(paddle2, ball, score2, ballDirX):
    # 5 points for beatin the other paddle
    if  ball.left == LINETHICKNESS:
        score2 += 5
        return score2
    # if no points scored, return score unchanged
    else: return score2

#Artificial Intelligence of computer player
    
def artificialIntelligence(ball, ballDirX, paddle2):
    #If ball is moving away from paddle, center bat
    if ballDirX == -1:
        if paddle2.centery < (WINDOWHEIGHT/2):
            paddle2.y += 1
        elif paddle2.centery > (WINDOWHEIGHT/2):
            paddle2.y -= 1
    #if ball moving towards bat, track its movement
            
    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -=1
    return paddle2

#Displays the PLAYERS score on the screen

def displayScore1(score):
    resultSurf = BASICFONT.render('%s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (270, 210)
    DISPLAYSURF.blit(resultSurf, resultRect)

#Displays the COMPUTERS score on the screen

def displayScore2(score2):
    resultSurf = BASICFONT.render('%s' %(score2), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (350, 210)
    DISPLAYSURF.blit(resultSurf, resultRect)

#Main function
    
def main():
    pygame.init()
    global DISPLAYSURF
    # Font information
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 30
    BASICFONT = pygame.font.SysFont('arial', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Ping Pong')

    #Initiate variable and set starting positions
    #any future changes made within rectangles
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2
    score = 0
    score2= 0

    #Keeps track of ball direction
    ballDirX = -1 ## -1 = left 1 = right
    ballDirY = -1 ## -1 = up 1 = down

    #Creates Rectangles for ball and paddles.
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    #Draws the starting position of the Arena
    drawArena()
    drawPaddle1(paddle1)
    drawPaddle2(paddle2)
    drawBall(ball)

    pygame.mouse.set_visible(0) # make cursor invisible

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                paddle1.y = mousey

        drawArena()
        drawPaddle1(paddle1)
        drawPaddle2(paddle2)
        drawBall(ball)

        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        score = checkPointScored(paddle1, ball, score, ballDirX)
        score2 =  checkPointScored2(paddle2, ball, score2, ballDirX)
        ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
        paddle2 = artificialIntelligence (ball, ballDirX, paddle2)

        displayScore1(score)
        displayScore2(score2)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
