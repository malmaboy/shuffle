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