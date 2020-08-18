import Pong4
import pygame, sys
import time,os

pygame.init()
gameDisplay= pygame.display.set_mode((640,480))
gameDisplay.fill((20,20,20))

RED   = (255, 50, 50)
GREEN = (100, 255, 100)
BLUE  = (100, 100, 255)
WHITE = (255, 255, 255)

os.environ['SDL_VIDEO_CENTERED'] = '1'
gameExit = False

font1 = pygame.font.SysFont("arial", 35)
font2 = pygame.font.SysFont("arial", 20)
font3 = pygame.font.SysFont("Monotype Corsiva", 18)
    
screen_text = font1.render("INSTRUCTIONS: ", True, GREEN)
gameDisplay.blit(screen_text, [10,10])

screen_text = font2.render("*   Player has the Blue paddle and the computer has the Red paddle.", True, WHITE)
gameDisplay.blit(screen_text, [10,70])
screen_text = font2.render("*   Use the mouse to control the Blue paddle.", True, WHITE)
gameDisplay.blit(screen_text, [10,100])
screen_text = font2.render("*   Objective:  Do not let the Green ball touch your wall.", True, WHITE)
gameDisplay.blit(screen_text, [10,130])
screen_text = font2.render("*   2 points if the player stops the ball from hitting the his wall.", True, WHITE)
gameDisplay.blit(screen_text, [10,160])
screen_text = font2.render("*   5 points for the computer if the ball touches the player's wall.", True, WHITE)
gameDisplay.blit(screen_text, [10,190])
screen_text = font2.render("*   5 points for the player if the ball touches the computer's wall.", True, WHITE)
gameDisplay.blit(screen_text, [10,220])

font4 = pygame.font.SysFont("Times New Roman", 25)
screen_text = font4.render("Back to Menu", True, GREEN)
gameDisplay.blit(screen_text, [15,445])
Rectplace1 = pygame.draw.rect(gameDisplay, (250, 0, 0),(0,440, 200, 40), 2)
screen_text = font3.render("Press any key to continue... ", True, BLUE)
gameDisplay.blit(screen_text, [465,455])
pygame.display.set_caption('Ping Pong - Instructions')
pygame.display.update()
while True:
    pos = pygame.mouse.get_pos()
    (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
    if Rectplace1.collidepoint(pos) & pressed1 == 1:
        import Start_Game
    for event in pygame.event.get():
        if event.type ==  pygame.KEYDOWN:
            Pong4.main()
    
