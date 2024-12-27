
import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Sirve para manejar las balas disparadas desde la nave"""
    def __init__(self, ai_configuraciones, pantalla, nave):
        super(Bala, self).__init__()
        self.pantalla = pantalla

        # Crea una bala rect en (0, 0) y luego establece la posición correcta
        self.rect = pygame.Rect(0, 0, ai_configuraciones.bala_width, ai_configuraciones.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Almecena la posición de la bala como un valor decimal 
        self.y = float(self.rect.y)

        self.color = ai_configuraciones.bala_color
        self.factor_velocidad = ai_configuraciones.bala_factor_velocidad
        
























