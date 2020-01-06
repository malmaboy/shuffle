import pygame, sys, random
import pygame.freetype

#cores
white = (255, 255, 255) 
green = (0, 200, 0) 
blue = (0, 0, 128)
red = (200, 0, 0)
yellow = (255, 255, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
black = (0,0,0)

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
    buttom(screen, 600, 550, 150, 50, yellow, red,"exit")
    buttom(screen, 600, 500, 150, 50, yellow, white,"nivel5")
    buttom(screen, 600, 450, 150, 50, yellow, white,"nivel4")
    buttom(screen, 600, 400, 150, 50, yellow, white,"nivel3")
    buttom(screen, 600, 350, 150, 50, yellow, white,"nivel2")
    buttom(screen, 600, 300, 150, 50, yellow, white,"nivel1")
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    nivel1 = font.render("3x4", True, (black))
    nivel2 = font.render("4x4", True, (black))
    nivel3 = font.render("5x4", True, (black))
    nivel4= font.render("6x5", True, (black))
    nivel5 = font.render("6x6", True, (black))
    exit = font.render("Exit", True, (black))
    
    screen.blit(nivel1,(650,310))
    screen.blit(nivel2,(650,360))
    screen.blit(nivel3,(650,410))
    screen.blit(nivel4,(650,460))
    screen.blit(nivel5,(650,510))
    screen.blit(exit,(650,560))
    
    
def figuras_n1(screen):
    
    #desenha as figuras
    buttom(screen, 100, 550, 100, 50, yellow, red,"menu")
    buttom(screen, 390, 80, 100, 150, green, white)
    buttom(screen, 550, 80, 100, 150, green, white)
    buttom(screen, 710, 80, 100, 150, green, white)
    buttom(screen, 870, 80, 100, 150, green, white)
    buttom(screen, 390, 245, 100, 150, green, white)
    buttom(screen, 550, 245, 100, 150, green, white)
    buttom(screen, 710, 245, 100, 150, green, white)
    buttom(screen, 870, 245, 100, 150, green, white)
    buttom(screen, 390, 410, 100, 150, green, white)
    buttom(screen, 550, 410, 100, 150, green, white)
    buttom(screen, 710, 410, 100, 150, green, white)
    buttom(screen, 870, 410, 100, 150, green, white)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    
def figuras_n2(screen):
    buttom(screen, 100, 550, 100, 50, yellow, red,"menu")
    buttom(screen, 390, 80, 100, 130, green, white)
    buttom(screen, 550, 80, 100, 130, green, white)
    buttom(screen, 710, 80, 100, 130, green, white)
    buttom(screen, 870, 80, 100, 130, green, white)
    buttom(screen, 390, 225, 100, 130, green, white)
    buttom(screen, 550, 225, 100, 130, green, white)
    buttom(screen, 710, 225, 100, 130, green, white)
    buttom(screen, 870, 225, 100, 130, green, white)
    buttom(screen, 390, 370, 100, 130, green, white)
    buttom(screen, 550, 370, 100, 130, green, white)
    buttom(screen, 710, 370, 100, 130, green, white)
    buttom(screen, 870, 370, 100, 130, green, white)
    buttom(screen, 390, 515, 100, 130, green, white)
    buttom(screen, 550, 515, 100, 130, green, white)
    buttom(screen, 710, 515, 100, 130, green, white)
    buttom(screen, 870, 515, 100, 130, green, white)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    

def figuras_n3(screen):
    
    buttom(screen, 100, 550, 100, 50, yellow, red,"menu")
    buttom(screen, 390, 80, 100, 130, green, white)
    buttom(screen, 520, 80, 100, 130, green, white)
    buttom(screen, 650, 80, 100, 130, green, white)
    buttom(screen, 780, 80, 100, 130, green, white)
    buttom(screen, 390, 225, 100, 130, green, white)
    buttom(screen, 520, 225, 100, 130, green, white)
    buttom(screen, 650, 225, 100, 130, green, white)
    buttom(screen, 780, 225, 100, 130, green, white)
    buttom(screen, 390, 370, 100, 130, green, white)
    buttom(screen, 520, 370, 100, 130, green, white)
    buttom(screen, 650, 370, 100, 130, green, white)
    buttom(screen, 780, 370, 100, 130, green, white)
    buttom(screen, 390, 515, 100, 130, green, white)
    buttom(screen, 520, 515, 100, 130, green, white)
    buttom(screen, 650, 515, 100, 130, green, white)
    buttom(screen, 780, 515, 100, 130, green, white)
    buttom(screen, 910, 80, 100, 130, green, white)
    buttom(screen, 910, 225, 100, 130, green, white)
    buttom(screen, 910, 370, 100, 130, green, white)
    buttom(screen, 910, 515, 100, 130, green, white)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    
def figuras_n4(screen):
    
    buttom(screen, 100, 550, 100, 50, yellow, red,"menu")
    buttom(screen, 390, 70, 80, 100, green, white)
    buttom(screen, 520, 70, 80, 100, green, white)
    buttom(screen, 650, 70, 80, 100, green, white)
    buttom(screen, 780, 70, 80, 100, green, white)
    buttom(screen, 390, 195, 80, 100, green, white)
    buttom(screen, 520, 195, 80, 100, green, white)
    buttom(screen, 650, 195, 80, 100, green, white)
    buttom(screen, 780, 195, 80, 100, green, white)
    buttom(screen, 390, 320, 80, 100, green, white)
    buttom(screen, 520, 320, 80, 100, green, white)
    buttom(screen, 650, 320, 80, 100, green, white)
    buttom(screen, 780, 320, 80, 100, green, white)
    buttom(screen, 390, 445, 80, 100, green, white)
    buttom(screen, 520, 445, 80, 100, green, white)
    buttom(screen, 650, 445, 80, 100, green, white)
    buttom(screen, 780, 445, 80, 100, green, white)
    buttom(screen, 910, 70, 80, 100, green, white)
    buttom(screen, 910, 195, 80, 100, green, white)
    buttom(screen, 910, 320, 80, 100, green, white)
    buttom(screen, 910, 445, 80, 100, green, white)
    buttom(screen, 1040, 70, 80, 100, green, white)
    buttom(screen, 1040, 195, 80, 100, green, white)
    buttom(screen, 1040, 320, 80, 100, green, white)
    buttom(screen, 1040, 445, 80, 100, green, white)
    buttom(screen, 1040, 570, 80, 100, green, white)
    buttom(screen, 910, 570, 80, 100, green, white)
    buttom(screen, 780, 570, 80, 100, green, white)
    buttom(screen, 650, 570, 80, 100, green, white)
    buttom(screen, 520, 570, 80, 100, green, white)
    buttom(screen, 390, 570, 80, 100, green, white)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    
def figuras_n5(screen):
    
    buttom(screen, 100, 550, 100, 50, yellow, red,"menu")
    buttom(screen, 390, 40, 60, 90, green, white)
    buttom(screen, 520, 40, 60, 90, green, white)
    buttom(screen, 650, 40, 60, 90, green, white)
    buttom(screen, 780, 40, 60, 90, green, white)
    buttom(screen, 390, 140, 60, 90, green, white)
    buttom(screen, 520, 140, 60, 90, green, white)
    buttom(screen, 650, 140, 60, 90, green, white)
    buttom(screen, 780, 140, 60, 90, green, white)
    buttom(screen, 390, 240, 60, 90, green, white)
    buttom(screen, 520, 240, 60, 90, green, white)
    buttom(screen, 650, 240, 60, 90, green, white)
    buttom(screen, 780, 240, 60, 90, green, white)
    buttom(screen, 390, 340, 60, 90, green, white)
    buttom(screen, 520, 340, 60, 90, green, white)
    buttom(screen, 650, 340, 60, 90, green, white)
    buttom(screen, 780, 340, 60, 90, green, white)
    buttom(screen, 910, 40, 60, 90, green, white)
    buttom(screen, 910, 140, 60, 90, green, white)
    buttom(screen, 910, 240, 60, 90, green, white)
    buttom(screen, 910, 340, 60, 90, green, white)
    buttom(screen, 1040, 40, 60, 90, green, white)
    buttom(screen, 1040, 140, 60, 90, green, white)
    buttom(screen, 1040, 240, 60, 90, green, white)
    buttom(screen, 1040, 340, 60, 90, green, white)
    buttom(screen, 1040, 440, 60, 90, green, white)
    buttom(screen, 910, 440, 60, 90, green, white)
    buttom(screen, 780, 440, 60, 90, green, white)
    buttom(screen, 650, 440, 60, 90, green, white)
    buttom(screen, 520, 440, 60, 90, green, white)
    buttom(screen, 390, 440, 60, 90, green, white)
    buttom(screen, 1040, 540, 60, 90, green, white)
    buttom(screen, 910, 540, 60, 90, green, white)
    buttom(screen, 780, 540, 60, 90, green, white)
    buttom(screen, 650, 540, 60, 90, green, white)
    buttom(screen, 520, 540, 60, 90, green, white)
    buttom(screen, 390, 540, 60, 90, green, white)
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))

    screen.blit(exit,(110,560))
    
def main():
    # Inicia a o Pygame
    pygame.init()

    #Cores
    white = (255, 255, 255) 
    green = (0, 200, 0) 
    blue = (0, 0, 128)
    red = (200, 0, 0)
    yellow = (255, 255, 0)
    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)
    
    # Criação de uma janela 
    size_x = 1300
    size_y = 700
    screen = pygame.display.set_mode((size_x, size_y))
    #Limpar a janela, cor: azul claro
    screen.fill((0, 0, 20))

    #Põe o nome da janela
    pygame.display.set_caption('Shuffle')
    

    #Pôe a imagem no menu
    image = pygame.image.load("shuffle.png")
    
   

    #Game loop, runs forever
    while (True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            pygame.display.update()
        screen.fill((0,0,20))  
         # função desenha as figuras e texto
        # menusmenuVisible = False
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











