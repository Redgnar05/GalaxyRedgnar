
import pygame 
from configuraciones import Configuraciones 
from nave import Nave 
import funciones_juego as fj

def run_game():
    # Inicilizar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invasión alienígena")

    # Crea una nave
    nave = Nave(ai_configuraciones, pantalla)

    # Iniciar el bucle principal del juego
    while True:
        # Escuchar eventos de teclado o de ratón
        fj.verificar_eventos(nave)
        nave.update()
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave)

run_game()



















































