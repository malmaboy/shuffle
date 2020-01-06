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

class myy:
    def __init__(self):
        self.visible = True
        
myy = myy()



def buttom(screen, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                myy.visible = False
                print(myy.visible)
                figuras(screen)
            elif action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))


def menu(screen):   
    # Desenha o menu(X,Y, Largura e Altura, cor inativa, cor ativa)
    buttom(screen, 600, 550, 150, 50, yellow, red,"exit")
    buttom(screen, 600, 500, 150, 50, yellow, white,"play")
    buttom(screen, 600, 500, 150, 50, yellow, white,"play")
    buttom(screen, 600, 450, 150, 50, yellow, white,"play")
    buttom(screen, 600, 450, 150, 50, yellow, white,"play")
    buttom(screen, 600, 400, 150, 50, yellow, white,"play")
    buttom(screen, 600, 350, 150, 50, yellow, white,"play")
    buttom(screen, 600, 300, 150, 50, yellow, white,"play")

    
    
def figuras(screen):
    
    #desenha as figuras

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

    #Põe os niveis no menu
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    nivel1 = font.render("3x4", True, (black))
    nivel2 = font.render("4x4", True, (black))
    nivel3 = font.render("5x4", True, (black))
    nivel4= font.render("6x5", True, (black))
    nivel5 = font.render("6x6", True, (black))
    exit = font.render("Exit", True, (black))
    

    #Pôe a imagem no menu

    
   

    #Game loop, runs forever
    while (True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            pygame.display.update()
        screen.fill((0,0,20))  

         # função desenha as figuras e texto
        # menusVisible = False
        if(myy.visible == True):
            menu(screen)
        else:
            figuras(screen)
            #desenha as letras no menu
        screen.blit(nivel1,(650,310))
        screen.blit(nivel2,(650,360))
        screen.blit(nivel3,(650,410))
        screen.blit(nivel4,(650,460))
        screen.blit(nivel5,(650,510))
        screen.blit(exit,(650,560))
        pygame.display.flip()
main()











