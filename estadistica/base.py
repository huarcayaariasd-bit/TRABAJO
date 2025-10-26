class EstadisticaBase:
    """
    Clase base para estadísticas.
    Define la estructura básica que deben seguir todas las subclases.
    """
    def __init__(self, datos):
        self.datos = datos

    def resumen(self):
        """
        Método que debe ser implementado en las subclases.
        """
        raise NotImplementedError("Debe implementarse en las subclases")
