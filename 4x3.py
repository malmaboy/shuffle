import pygame
import sys
import random
import pygame.freetype

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 100, 10)
purple = (240, 0 , 230)
pink = (255, 100, 180)
black = (0,0,0)

#funtion buttom (screen, X, Y, wight(largura), height(altura), inactive color, active color )
def buttom(screen, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                figuras_1(screen)
            elif action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))


def figuras_1(screen):
    buttom(screen, 415, 120, 50, 50, purple, purple)
    
    
    
    
def figuras(screen):
    
    #desenha as figuras (screen, X, Y, largura, altura, cor inativa, cor ativa)

    buttom(screen, 390, 80, 100, 150, green, white, "play")
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
    buttom(screen, 100, 550, 100, 50, yellow, red,"exit")
   
    
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
