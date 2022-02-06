"""
Author : AUBRY Paul
Date : 18/01/22
Main file of DeepChess project
"""
import pygame
from board import *
from soupsieve import select

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800,60 * 8))
pygame.display.set_caption("Deep Chess")

#Load Image
bg = pygame.image.load("assets/chessboard.png").convert()
sidebg = pygame.image.load("assets/woodsidemenu.jpeg").convert()
myfont = pygame.font.Font("assets/Roboto-Black.ttf",30)

player = 1 #1 for the Human, 0 for the AIe

board = Board()

global sprites, all_sprites_list
all_spirites_list = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]

clock = pygame.time.Clock()

def welcome():
    """
    Display a welcome screen
    """
    menubg = pygame.image.load("assets/menubg.jpeg").convert()
    screen.blit(menubg,(0,0))
    bigfont = pygame.font.Font("assets/Roboto-Black.ttf",80)
    textsurface = bigfont.render("Deep Chess",False,(255,255,255))
    screen.blit(textsurface,(30,10))

    medfont = pygame.font.Font("assets/Roboto-Black.ttf",50)
    textsurface = medfont.render("Aubry Corporation",False,(255,255,255))
    screen.blit(textsurface,(100,100))
    textsurface = myfont.render("Press any key to start !",False,(255,255,255))
    screen.blit(textsurface,(250,170))
    
    running = True

    pygame.display.update()
    pygame.event.clear()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN:
                return
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

def run_game():
    """
    Main loop of the game
    """
    global player
    gameover = False
    selected = False

    while not gameover:
        #Human turn
        if player == 1:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and not selected:
                    piece = select_piece("w")

        
        screen.blit(bg,(0,0))
        pygame.display.update()
        clock.tick(60)


def select_piece(color):
    """
    Select a piece on the chessboard. Only returns if a valid piece was
    selected based on the color
    """
    pos = pygame.mouse.get_pos()
    clicked_spirit = [s for s in sprites if s.rect.collidepoint(pos)]

if __name__ == "__main__":
    welcome()
    run_game()