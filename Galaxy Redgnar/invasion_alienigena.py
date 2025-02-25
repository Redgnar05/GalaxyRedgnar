import pygame 
from configuraciones import Configuraciones  
import funciones_juego as fj
from pygame.sprite import Group
from estadisticas import Estadisticas
from marcador import Marcador
from button import Button
from nave import Nave

def run_game():
    # Inicilizar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invasión alienígena")

    # Crea el botón Play
    play_button = Button(ai_configuraciones, pantalla, "Play")

    # Crea una instancia para almacenar estadisticas del juego y crea un marcador
    estadisticas = Estadisticas(ai_configuraciones)
    marcador = Marcador(ai_configuraciones, pantalla, estadisticas)

    # Crea una nave, un grupo de balas y un grupo de aliens 
    nave = Nave(ai_configuraciones, pantalla)
    balas = Group()
    aliens = Group()

    # Crea la flota de alíenigenas 
    fj.crear_flota(ai_configuraciones, pantalla, nave, aliens)

    # Iniciar el bucle principal del juego
    while True:
        # Escuchar eventos de teclado o de ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, estadisticas, marcador, play_button, nave, aliens, balas)

        if estadisticas.game_active:
            nave.update()
            fj.update_balas(ai_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas)
            fj.update_aliens(ai_configuraciones, estadisticas, pantalla, marcador, nave, aliens, balas)
            
        fj.actualizar_pantalla(ai_configuraciones, pantalla, estadisticas, marcador, nave, aliens, balas, play_button)

run_game()




















































