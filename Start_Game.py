import pygame,os
os.environ['SDL_VIDEO_CENTERED'] = '1'

class Option:
    hovered = False
 

    def __init__(self, text, pos):

        self.text = text

        self.pos = pos

        self.set_rect()

        self.draw()

            

    def draw(self):

        self.set_rend()

        screen.blit(self.rend, self.rect)

        

    def set_rend(self):

        self.rend = menu_font.render(self.text, True, self.get_color())

        

    def get_color(self):

        if self.hovered:

            return (100, 100, 255)

        else:

            return (255, 255, 255)

        

    def set_rect(self):

        self.set_rend()

        self.rect = self.rend.get_rect()

        self.rect.topleft = self.pos



pygame.init()

screen = pygame.display.set_mode((650, 480))

menu_font = pygame.font.Font(None, 40)

options = [Option(" 1.  Ping Pong", (10, 100)), Option(" 2.  Snake Game", (10, 145)),

           Option(" 3.  Tic Tac Toe", (10, 190))]

font1 = pygame.font.SysFont("Monotype Corsiva",22)
font2 = pygame.font.SysFont("Times New Roman",50)
font3 = pygame.font.SysFont("arial",28)

def othertexts():
    screen_text = font2.render("--------- Arcade Games ---------", True, (50,255,50))
    screen.blit(screen_text, [10,10])
   
    screen_text = font1.render("Programming - Allen", True, (255,255,255))
    screen.blit(screen_text, [475,360])

    screen_text = font1.render("Developing - Baivab", True, (255,255,255))
    screen.blit(screen_text, [475,390])

    screen_text = font1.render("Testing - Ankit", True, (255,255,255))
    screen.blit(screen_text, [475,420])

    screen_text = font1.render("Designing - Shrestha", True, (255,255,255))
    screen.blit(screen_text, [475,450])
#Draw Once
Rectplace1 = pygame.draw.rect(screen, (250, 0, 0),(0, 90, 300, 46), 1)
Rectplace2 = pygame.draw.rect(screen, (0, 250, 0),(0, 135, 300, 46), 1)
Rectplace3 = pygame.draw.rect(screen, (0, 0, 250),(0, 180, 300, 46), 1)

while True:
    pos = pygame.mouse.get_pos()
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
    
    pygame.event.pump()
    
    screen.fill((20,20,20))
    pygame.draw.rect(screen, (50, 255, 50),(460, 350, 192, 132), 2)
    pygame.draw.rect(screen, (100, 100, 255),(457, 347, 195, 135), 2)
    pygame.display.set_caption('Group-1: Games')

    if Rectplace1.collidepoint(pos)& pressed1==1:
        import Instructions_Ping_Pong
    if Rectplace2.collidepoint(pos)& pressed1==1:
        import Instructions_Snake_Game
    if Rectplace3.collidepoint(pos)& pressed1==1:
        import Instructions_Tic_Tac_Toe
    for option in options:

        if option.rect.collidepoint(pygame.mouse.get_pos()):

            option.hovered = True
            

        else:

            option.hovered = False

        option.draw()
        othertexts()

    pygame.display.update()
