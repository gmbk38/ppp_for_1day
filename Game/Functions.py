import pygame
import time
from Textures import Textures

def Menu(screen):
    bullet_2 = Textures.bullet_lvl2_for_menu
    bullet_3 = Textures.bullet_lvl3_for_menu
    zero = Textures.zero
    one = Textures.one
    zero = zero.convert_alpha()
    one = one.convert_alpha()
    screen.blit(bullet_2,(130,40))
    screen.blit(one,(170,40))
    screen.blit(zero,(210,40))
    screen.blit(zero,(250,40))
    screen.blit(zero,(290,40))
    screen.blit(bullet_3,(90,100))
    screen.blit(one,(130,100))
    screen.blit(zero,(170,100))
    screen.blit(zero,(210,100))
    screen.blit(zero,(250,100))
    screen.blit(zero,(290,100)) 
    return screen

def Lives(screen, lives):
    one = Textures.one
    two = Textures.two
    three = Textures.three
    hp_line = Textures.hp_line.convert_alpha()
    if lives == 3:
        screen.blit(three,(40,500))
    elif lives == 2:
        screen.blit(two,(40,500))
    elif lives == 1:
        screen.blit(one,(40,500))
    
    for i in range (0,lives):
        screen.blit(hp_line,(8+32*i,8))

    return screen

def Live_control (lives):
    if lives > 5:
        lives = 5
    return lives