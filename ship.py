import pygame

class Ship:
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        #Инициализируется корабль и задает его начальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        #каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флагов"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        #рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)