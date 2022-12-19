

import pygame
from bullets import Bullet
from enemy import Enemy
import sys
a = 1
def events(screen, gun, bullets):
    global a
    """
    отслеживание действий и реагирование на них
    :param screen: то, что находится на экране
    :param gun: экземпляр пушки
    :param bullets: класс пуль
    :return: отслеживает действия и реагирует на них
    """
    if a == 1:
        for doings in pygame.event.get():
            if doings.type == pygame.QUIT:
                pygame.quit()
                a = 0
                sys.exit()
            elif doings.type == pygame.KEYDOWN:
                if doings.key == pygame.K_s:
                    gun.high = True
                elif doings.key == pygame.K_w:
                    gun.low = True
                elif doings.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
            elif doings.type == pygame.KEYUP:
                if doings.key == pygame.K_s:
                    gun.high = False
                elif doings.key == pygame.K_w:
                    gun.low = False


def update_screen(back_image, screen, gun, enemies, bullets):
    '''
Обновляет экран
    :param back_image: задний фон
    :param screen: для доступа к экрану, чтобы можно было отрисовать
    :param gun: инициализация пушки
    :param enemies: класс врагов
    :param bullets: класс пуль
    :return:на экране происходят события
    '''
    if a == 1:
        screen.blit(back_image, [0, 0])
        for bullet in bullets.sprites():
            bullet.draw_bul()
        gun.output()
        enemies.draw(screen)
        pygame.display.flip()


def kill_bul(bullets, screen, enemies):
    '''
    удаление пуль и столкновение с врагом
    :param bullets: класс пуль
    :param screen: доступ к экрану, чтобы отрисовать
    :param enemies: класс врагов
    :return: удаление пуль, когда они выходят за рамки окна, при столкновении пуль с врагами удаляются и пули и враги
    '''

    if a == 1:
        bullets.update()
        screen_rect = screen.get_rect()
        for bullet in bullets.copy():
            if bullet.rect.left >= screen_rect.right:
                bullets.remove(bullet)
        pygame.sprite.groupcollide(bullets, enemies, True, True)


def do_army(screen, enemies):
    '''
    данная функция создает армию. Для этого надо создать одного и взять с него параметры
    :param screen: доступ к экрану
    :param enemies: класс инопланетян
    :return: создание армии
    '''
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    number_enemy_y = int((480 - 2 * enemy_height) / enemy_height + 1)
    for enemy_number in range(number_enemy_y):
        enemy = Enemy(screen)
        enemy.y = enemy_height + enemy_height * enemy_number
        enemy.rect.y = enemy.y
        enemies.add(enemy)
