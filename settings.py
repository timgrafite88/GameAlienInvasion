class Settings:
    """Класс для хранения всех настроек игры Инопланетное вторжение"""

    def __init__(self):
        """Инициализируем настройки игры"""
        #Параметр экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5

