
class Estadisticas():
    """Seguimiento de las estadísticas de Invasión Alienígena"""
    def __init__(self, ai_configuraciones):
        """Inicializa las estadisticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()

        # Inicia Invasión Alienígena en un estado activo
        self.game_active = False

        # La puntuación alta nunca debe restablecerse
        self.alto_puntaje = 0

    def reset_stats(self):
        """Inicializa estadísitcas que pueden cambiar durante el juego"""
        self.naves_restantes = self.ai_configuraciones.cantidad_naves
        self.puntaje = 0
        self.nivel = 1






