import pygame, sys, random
import pygame.freetype
from pygame.locals import *
import _4x3, _4x4                                           

#COLORS
GRAY     = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE    = (255, 255, 255)
RED      = (255, 0, 0)
GREEN    = (0, 255, 0)
BLUE     = (0, 0, 255)
YELLOW   = (255, 255, 0)
ORANGE   = (255, 128, 0)
PURPLE   = (255, 0, 255)
CYAN     = (0, 255, 255)
BLACK    = (0, 0, 0)
DARK_BLUE = (0, 0, 20)

BGCOLOR = DARK_BLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = GREEN
HIGHLIGHTCOLOR = WHITE

CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (CIRCLE, SQUARE, DIAMOND)

class Jogo:
    def __init__(self):
        self.menuVisible = True
        self.game = 0
        
jogo = Jogo()



def buttom(screen, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "nivel1":
                jogo.menuVisible = False
                jogo.game = 0
            elif action == "nivel2":
                jogo.menuVisible = False
                jogo.game = 1
            elif action == "nivel3":
                jogo.menuVisible = False
                jogo.game = 2
            elif action == "nivel4":
                jogo.menuVisible = False
                jogo.game = 3
            elif action == "nivel5":
                jogo.menuVisible = False
                jogo.game = 4
            elif action == "exit":
                pygame.quit()
                quit()
            elif action == "menu":
                jogo.menuVisible = True
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))


def menu(screen):   
    # Desenha o menu(X,Y, Largura e Altura, cor inativa, cor ativa)
    buttom(screen, 600, 550, 150, 50, YELLOW, RED,"exit")
    buttom(screen, 600, 500, 150, 50, YELLOW, WHITE,"nivel5")
    buttom(screen, 600, 450, 150, 50, YELLOW, WHITE,"nivel4")
    buttom(screen, 600, 400, 150, 50, YELLOW, WHITE,"nivel3")
    buttom(screen, 600, 350, 150, 50, YELLOW, WHITE,"nivel2")
    buttom(screen, 600, 300, 150, 50, YELLOW, WHITE,"nivel1")
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    nivel1 = font.render("3x4", True, (BLACK))
    nivel2 = font.render("4x4", True, (BLACK))
    nivel3 = font.render("5x4", True, (BLACK))
    nivel4= font.render("6x5", True, (BLACK))
    nivel5 = font.render("6x6", True, (BLACK))
    exit = font.render("Exit", True, (BLACK))
    
    screen.blit(nivel1,(650,310))
    screen.blit(nivel2,(650,360))
    screen.blit(nivel3,(650,410))
    screen.blit(nivel4,(650,460))
    screen.blit(nivel5,(650,510))
    screen.blit(exit,(650,560))
    
    
def figuras_n1(screen):

    _4x3.main()
 
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    
def figuras_n2(screen):

    _4x4.main()
   
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (BLACK))

    screen.blit(exit,(110,560))
    

def figuras_n3(screen):
    
    
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (BLACK))

    screen.blit(exit,(110,560))
    
def figuras_n4(screen):
    
    buttom(screen, 100, 550, 100, 50, YELLOW, RED,"menu")
    buttom(screen, 390, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 520, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 650, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 780, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 390, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 520, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 650, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 780, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 390, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 520, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 650, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 780, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 390, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 520, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 650, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 780, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 910, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 910, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 910, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 910, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 1040, 70, 80, 100, GREEN, WHITE)
    buttom(screen, 1040, 195, 80, 100, GREEN, WHITE)
    buttom(screen, 1040, 320, 80, 100, GREEN, WHITE)
    buttom(screen, 1040, 445, 80, 100, GREEN, WHITE)
    buttom(screen, 1040, 570, 80, 100, GREEN, WHITE)
    buttom(screen, 910, 570, 80, 100, GREEN, WHITE)
    buttom(screen, 780, 570, 80, 100, GREEN, WHITE)
    buttom(screen, 650, 570, 80, 100, GREEN, WHITE)
    buttom(screen, 520, 570, 80, 100, GREEN, WHITE)
    buttom(screen, 390, 570, 80, 100, GREEN, WHITE)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (BLACK))

    screen.blit(exit,(110,560))
    
def figuras_n5(screen):
    
    buttom(screen, 100, 550, 100, 50, YELLOW, RED,"menu")
    buttom(screen, 390, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 390, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 390, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 390, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 40, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 140, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 240, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 340, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 390, 440, 60, 90, GREEN, WHITE)
    buttom(screen, 1040, 540, 60, 90, GREEN, WHITE)
    buttom(screen, 910, 540, 60, 90, GREEN, WHITE)
    buttom(screen, 780, 540, 60, 90, GREEN, WHITE)
    buttom(screen, 650, 540, 60, 90, GREEN, WHITE)
    buttom(screen, 520, 540, 60, 90, GREEN, WHITE)
    buttom(screen, 390, 540, 60, 90, GREEN, WHITE)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (BLACK))

    screen.blit(exit,(110,560))
    
def main():
    # INICIATE PYGAME
    pygame.init()
    
    # CREATE A WINDOW 
    size_x = 1300
    size_y = 700
    screen = pygame.display.set_mode((size_x, size_y))
    #WINDOW
    screen.fill((0, 0, 20))

    #WINDOW NAME
    pygame.display.set_caption('Shuffle')
    

    #IMAGE ON THE MENU
    image = pygame.image.load("shuffle.png")
    
   

    #Game loop, runs forever
    while (True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            pygame.display.update()
        screen.fill((0,0,20))  
        if(jogo.menuVisible == True):
            screen.blit(image,(200, 0))
            menu(screen)
        else:
            if jogo.game == 0:
                figuras_n1(screen)
            elif jogo.game == 1:
                figuras_n2(screen)
            elif jogo.game == 2:
                figuras_n3(screen)
            elif jogo.game == 3:
                figuras_n4(screen)
            elif jogo.game == 4:
                figuras_n5(screen)
        pygame.display.flip()
main()

