import pygame


def rot(image, angle):
    '''
    переварачивает картинку пушки
    :param image: изображение пушки
    :param angle: угол, на которыц нужно повернуть
    :return: перевернутую картинку
    '''
    proses = image.get_rect().center
    sprite = pygame.transform.rotate(image, angle)
    sprite.get_rect().center = proses
    return sprite


class Gun():
    '''
    класс пушки
    '''
    def __init__(self, screen):
        '''
        инициализация пушки
        :param screen: экран
        '''
        self.screen = screen
        self.image = pygame.image.load('image/K00.png')
        self.image = rot(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centery)
        self.rect.left = self.screen_rect.left
        self.high = False
        self.low = False

    def output(self):
        '''
        вывод пушки на экран
        :return: картику пушки на фоне игры
        '''
        self.screen.blit(self.image, self.rect)

    def move_gun(self):
        '''
        передвижение пушки по своей оси
        :return: положение пушки относительно оси
        '''
        if self.high and self.rect.bottom <= self.screen_rect.bottom:
            self.center += 0.2
        if self.low and self.rect.top >= self.screen_rect.top:
            self.center -= 0.2
        self.rect.centery = self.center
