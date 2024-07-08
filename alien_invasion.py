import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициилизирует игру и создает игповые ресурсы"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Инопланетное вторжение")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right == False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left == False

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра запуска игры
    ai = AlienInvasion()
    ai.run_game()