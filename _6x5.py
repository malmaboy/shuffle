import pygame
import sys
import random

#cores
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 100, 10)
purple = (240, 0 , 230)
pink = (255, 100, 180)
black = (0, 0, 0)

def buttom(screen, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                figuras()
            elif action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

def figuras(screen):
    
    
   # Desenha o menu(X,Y, Largura e Altura, cor inativa, cor ativa)
    buttom(screen, 100, 550, 100, 50, yellow, red,"exit")
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
    
    
def main():
    pygame.init()


    size_x = 1300
    size_y = 700
    screen = pygame.display.set_mode((size_x, size_y))

    screen.fill((0, 0, 20))
    
    font = pygame.font.SysFont("NotoSans-Regular.ttf",50)
    exit = font.render("Exit", True, (black))



    while (True):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    exit()
                pygame.display.update()

            figuras(screen)
            screen.blit(exit,(110,560))
            pygame.display.flip()
main()