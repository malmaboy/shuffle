import pygame
import pygame.freetype
import random

def menu(screen):
    # Desenha o menu  (cores),(X,Y, Largura e Altura)
    pygame.draw.rect(screen, (255, 255, 0), (600, 550, 150, 50), 2)
    pygame.draw.rect(screen, (255, 255, 0), (600, 500, 150, 50), 2)
    pygame.draw.rect(screen, (255, 255, 0), (600, 450, 150, 50), 2)
    pygame.draw.rect(screen, (255, 255, 0), (600, 400, 150, 50), 2)
    pygame.draw.rect(screen, (255, 255, 0), (600, 350, 150, 50), 2)
    pygame.draw.rect(screen, (255, 255, 0), (600, 300, 150, 50), 2)
    
def main():
    # Inicia a o Pygame
    pygame.init()

    #Cores
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128)
    red = (255, 0, 0)
    yellow = (255, 255, 0)

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
    texto = font.render("3x4", True, (yellow))
    texto1 = font.render("4x4", True, (yellow))
    texto2 = font.render("5x4", True, (yellow))
    texto3 = font.render("6x5", True, (yellow))
    texto4 = font.render("6x6", True, (yellow))
    texto5 = font.render("Exit", True, (yellow))
   

    #Game loop, runs forever
    while (True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
            pygame.display.update()     

         # função desenha as figuras e texto
        menu(screen)
        pygame.display.flip()
        screen.blit(texto,(650,310))
        screen.blit(texto1,(650,360))
        screen.blit(texto2,(650,410))
        screen.blit(texto3,(650,460))
        screen.blit(texto4,(650,510))
        screen.blit(texto5,(650,560))
main()



