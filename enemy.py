import pygame


class Enemy(pygame.sprite.Sprite):
    '''
    класс пришельца
    '''
    def __init__(self, screen):
        '''
инициализация пришельца
        :param screen: экран
        создает объект, как прямоугольник
        '''
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/prived.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.x = float(self.rect.centery)
        self.y = float(self.rect.right)
