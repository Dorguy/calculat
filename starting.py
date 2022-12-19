import pygame, controls
from gun import Gun
from pygame.sprite import Group
import sys
import os, signal
width = 854
height = 480


def go():
    '''
    функция, которая запускает игру, в ней находится все данные, которые необходимы для того, чтобы игра работала
    :param width: длина окна
    :param height: высота окна
    :return: движения на экране
    '''
    pygame.init()
    screen = pygame.display.set_mode((854, 480))
    pygame.display.set_caption('Стрелялка')
    back_image = pygame.image.load('image/back.png').convert()
    play = True
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.do_army(screen, enemies)
    while play:
        controls.events(screen, gun, bullets)
        gun.move_gun()
        controls.kill_bul(bullets, screen, enemies)
        controls.update_screen(back_image, screen, gun, enemies, bullets)
        if len(enemies) == 0:
            play = False
    sc = pygame.display.set_mode((300, 200))
    sc.fill((0, 0, 0))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Игра завершена', True, (180, 180, 0))
    play = True
    sc.blit(text1, (10, 50))
    pygame.display.update()
    pygame.display.flip()
    while play:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                play = False
                pygame.quit()


#go()
